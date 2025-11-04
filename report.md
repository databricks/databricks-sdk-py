# Bug Report: TypeError in RoundTrip Logger

## Summary
A `TypeError` occurs in the Databricks SDK Python library when the round trip logger attempts to call `len()` on a `_io.BytesIO` object. This happens during error handling when the SDK tries to generate debugging information for failed API requests.

## Error Details

**Error Type:** `TypeError: object of type '_io.BytesIO' has no len()`

**Stack Trace:**
1. `databricks/sdk/_base_client.py:296` in `_perform()` method
2. `databricks/sdk/errors/parser.py:87` in `get_api_error()` method  
3. `databricks/sdk/errors/parser.py:39` in `_unknown_error()` function
4. `databricks/sdk/logger/round_trip_logger.py:47` in `generate()` method
5. `databricks/sdk/logger/round_trip_logger.py:113` in `_redacted_dump()` method

## Root Cause Analysis

### The Immediate Bug
The `_redacted_dump()` method in `round_trip_logger.py` assumes that the `body` parameter is always a string and calls `len(body)` directly on line 113:

```python
def _redacted_dump(self, prefix: str, body: str) -> str:
    if len(body) == 0:  # ← This line causes the error
        return ""
```

### Why BytesIO Objects Are Present
In `_base_client.py` lines 167-169, the SDK wraps string and bytes data in `BytesIO` objects for retry functionality:

```python
# Wrap strings and bytes in a seekable stream so that we can rewind them.
if isinstance(data, (str, bytes)):
    data = io.BytesIO(data.encode("utf-8") if isinstance(data, str) else data)
```

When a request is made, this `BytesIO` object becomes the `request.body` in the requests library, which is then passed to the logging system when an error occurs.

### When the Error Occurs
This error happens when:
1. An API request contains a request body (originally string or bytes)
2. The request fails or returns an unparseable response
3. The error parser triggers `_unknown_error()` to generate debug information
4. The `RoundTrip` logger tries to log the request body
5. The `_redacted_dump()` method receives a `BytesIO` object instead of a string

### **LIKELY Root Cause: Protocol Mismatch - Sending JSON to RPC/Protobuf Endpoint**

**The SDK ONLY sends JSON, but may be hitting an endpoint that expects protobuf/RPC format.**

Critical evidence:
- **Line 290 in `_base_client.py`:** Uses `json=body` which ALWAYS serializes requests as JSON
- **All API calls:** Set `Content-Type: application/json` and `Accept: application/json` 
- **No protobuf serialization:** SDK has ZERO code to serialize requests as protobuf (no `SerializeToString` calls)
- **Protobuf only for internal types:** Only uses protobuf for `Duration`/`Timestamp` which are JSON-serialized
- **All error deserializers:** Expect text-based responses (JSON, HTML, or plain text with UTF-8)
- `google.rpc.status_pb2` binary module is **NOT available** in the SDK environment

**Most Likely Scenario:**

```
1. SDK sends JSON request to endpoint that expects protobuf/RPC
2. Server rejects the request (400 Bad Request or 415 Unsupported Media Type)
3. Server returns error response in protobuf binary format (or other non-JSON format)
4. SDK tries to parse the error response as JSON → ALL parsers fail
5. SDK triggers _unknown_error() to log debug info
6. BytesIO bug prevents logging → user sees TypeError instead of protocol mismatch error
```

**Alternative scenarios:**

- **Correct response in protobuf:** Server accepts JSON but responds in protobuf (unlikely - violates HTTP content negotiation)
- **Gateway/proxy errors:** Intermediate systems returning binary/non-JSON errors
- **Malformed response:** Response is corrupt, truncated, or has encoding issues

**The key insight:** We're sending the WRONG format to the server, and the error response we get back is also in a format we can't parse. The BytesIO bug masks what would otherwise reveal the protocol mismatch.

## Technical Impact

- **Error Masking:** The original API error is masked by this logging error, making debugging difficult
- **User Experience:** Users see a confusing `TypeError` instead of the actual API error
- **Debug Information Loss:** No useful debugging information is generated when this occurs

## Affected Components

- **Primary:** `databricks/sdk/logger/round_trip_logger.py` - The `_redacted_dump()` method
- **Secondary:** `databricks/sdk/_base_client.py` - The data wrapping logic that creates BytesIO objects
- **Impact:** Error handling and debugging across the entire SDK

## Recommended Fixes

### Fix 1: Handle BytesIO in Logger (Immediate)

The `_redacted_dump()` method should handle both string and `BytesIO` objects. Here's the recommended approach:

1. **Type checking:** Check if the body is a `BytesIO` object
2. **Content extraction:** If it's `BytesIO`, read its contents and get the length appropriately
3. **Rewind position:** Ensure the `BytesIO` position is reset after reading

Example fix for line 113 in `round_trip_logger.py`:
```python
def _redacted_dump(self, prefix: str, body) -> str:  # Remove str type hint
    # Handle both str and BytesIO objects
    if isinstance(body, io.BytesIO):
        current_pos = body.tell()  # Save current position
        body.seek(0)  # Go to start
        content = body.read().decode('utf-8', errors='replace')
        body.seek(current_pos)  # Restore position
        if len(content) == 0:
            return ""
        body_to_process = content
    else:
        if len(body) == 0:
            return ""
        body_to_process = body
    
    # Continue with existing logic using body_to_process
```

### Fix 2: Improve Binary Response Handling (Investigate Root Cause)

Add a fallback deserializer that provides better error messages for binary/unparseable responses:

Create a new `_BinaryResponseDeserializer` in `deserializer.py`:
```python
class _BinaryResponseDeserializer(_ErrorDeserializer):
    """Handles binary or unparseable responses by providing diagnostic information."""
    
    def deserialize_error(self, response: requests.Response, response_body: bytes) -> Optional[dict]:
        # This is a catch-all for responses that couldn't be parsed by other deserializers
        # Always return a result to provide diagnostic information
        
        content_type = response.headers.get('Content-Type', 'unknown')
        content_preview = response_body[:100].hex() if len(response_body) > 0 else "empty"
        
        # Try to determine if it's binary
        try:
            response_body.decode('utf-8')
            is_binary = False
        except UnicodeDecodeError:
            is_binary = True
        
        message = (
            f"Unable to parse response. "
            f"Content-Type: {content_type}, "
            f"Length: {len(response_body)} bytes, "
            f"Binary: {is_binary}, "
            f"Preview (hex): {content_preview}"
        )
        
        return {
            "message": message,
            "error_code": "UNPARSEABLE_RESPONSE",
        }
```

Add it as the **last** deserializer in `parser.py`:
```python
_error_deserializers = [
    _EmptyDeserializer(),
    _StandardErrorDeserializer(),
    _StringErrorDeserializer(),
    _HtmlErrorDeserializer(),
    _BinaryResponseDeserializer(),  # Catch-all, must be last
]
```

This will prevent the `_unknown_error()` path from being triggered and provide diagnostic information about what the response actually contains.

## Testing Recommendations

1. **Unit tests for BytesIO handling:** Add tests that pass `BytesIO` objects to `_redacted_dump()`
2. **Integration tests:** Test error scenarios with request bodies containing string/bytes data
3. **Edge cases:** Test with empty `BytesIO` objects and various encodings
4. **Binary response testing:** Create test cases with binary/non-UTF8 responses
5. **Content-Type validation:** Test responses with unexpected content types (e.g., `application/octet-stream`)
6. **Malformed response testing:** Test with truncated JSON, invalid encoding, etc.

## Investigation Required

To confirm the protocol mismatch hypothesis:
1. **Apply Fix 1 first:** This will allow logging to work and reveal response details
2. **Check response headers:** Look for `Content-Type: application/x-protobuf` or `application/grpc`
3. **Inspect response bytes:** Check if response starts with protobuf binary markers
4. **Check HTTP status code:** Look for 400 (Bad Request) or 415 (Unsupported Media Type)
5. **Identify the endpoint:** Determine which Databricks API endpoint is being called
6. **Verify endpoint requirements:** Check if the endpoint has both REST/JSON and gRPC/protobuf versions
7. **Review request URL:** Ensure using the correct URL path for REST/JSON API

## If Protocol Mismatch is Confirmed

**The SDK does NOT support protobuf/gRPC requests.** It is a REST/JSON-only SDK.

If the endpoint requires protobuf:
1. **Check for REST alternative:** Most Databricks APIs have REST/JSON endpoints
2. **Verify endpoint URL:** Ensure you're calling the REST API path, not a gRPC endpoint
3. **Contact Databricks support:** If only protobuf is available, request REST/JSON support
4. **Use different SDK:** Consider if there's a gRPC-compatible SDK available
5. **Consider feature request:** File an issue to add protobuf support to the Python SDK

## Priority
**Critical** - This bug has multiple levels:
- **Immediate:** Prevents proper error reporting and debugging (Fix 1) - **REQUIRED**
- **Diagnostics:** Add better error messages for unparseable responses (Fix 2) - **Recommended**
- **Root cause:** Likely protocol mismatch - SDK sending JSON to protobuf endpoint - **Needs investigation**

## Files to Modify
- `databricks/sdk/logger/round_trip_logger.py` (Fix 1 - immediate, required)
- `databricks/sdk/errors/deserializer.py` (Fix 2 - add binary response handler, recommended)
- `databricks/sdk/errors/parser.py` (Fix 2 - register new deserializer, recommended)
- Add test cases in relevant test files

## Additional Notes
- **Fix 1** should maintain backward compatibility with string inputs
- Consider adding type hints that accurately reflect the method can accept both strings and BytesIO
- The position management for BytesIO is crucial to avoid affecting retry logic
- **Fix 2** provides diagnostic information for unparseable responses instead of failing silently
- The SDK handles `google.rpc` types as JSON structures (via `@type` fields), not binary protobuf
- `google.rpc.status_pb2` is NOT available in the SDK environment (verified)

---

## Summary

**What happened:** User got a `TypeError: object of type '_io.BytesIO' has no len()` instead of seeing the actual API error.

**Why it happened:** 
1. **Immediate cause:** Logger tried to call `len()` on a `BytesIO` object
2. **Underlying cause:** SDK likely sent JSON to an endpoint expecting protobuf, got unparseable error response
3. **SDK limitation:** SDK is REST/JSON-only, has NO protobuf serialization capability

**What needs to be done:**
1. **Fix the logger** (Fix 1) - Required to see actual errors
2. **Add binary response handler** (Fix 2) - Recommended for better diagnostics  
3. **Investigate the endpoint** - Verify if protocol mismatch is the root cause
4. **User action:** Ensure using correct REST/JSON endpoint, not gRPC/protobuf endpoint
