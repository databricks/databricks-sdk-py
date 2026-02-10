### 4. Generate Provider

This step transforms the split OpenAPI service specs into a fully-functional StackQL provider by applying the resource and method mappings defined in your CSV file.

```bash
npm run generate-provider -- \
  --provider-name okta \
  --input-dir provider-dev/source \
  --output-dir provider-dev/openapi/src/okta \
  --config-path provider-dev/config/all_services.csv \
  --servers '[{"url": "https://{subdomain}.okta.com/", "variables": {"subdomain": {"default": "my-org","description": "The domain of your organization. This can be a provided subdomain of an official okta domain (okta.com, oktapreview.com, etc) or one of your configured custom domains."}}}]' \
  --provider-config '{"auth": {"credentialsenvvar": "OKTA_API_TOKEN","type": "api_key","valuePrefix": "SSWS "}}' \
  --skip-files _well_known.yaml \
  --overwrite
```
Make necessary updates to the output docs:

```bash
sh provider-dev/scripts/post_processing.sh
```

The `--servers` parameter defines the base URL pattern for API requests, with variables that users can customize. For Okta, this allows specifying different subdomains for different Okta instances.

The `--provider-config` parameter sets up the authentication method. For Okta, this configures an API token authentication scheme that:
- Looks for the API token in the `OKTA_API_TOKEN` environment variable
- Applies the `SSWS ` prefix required by Okta's API
- Uses the token as an API key in the Authorization header

The generated provider will be structured according to the StackQL conventions, with properly organized resources and methods that map to the underlying API operations.

After running this command, you'll have a complete provider structure in the `provider-dev/openapi/src` directory, ready for testing or packaging.

### 5. Test Provider

#### Starting the StackQL Server

Before running tests, start a StackQL server with your provider:

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/provider-dev/openapi"
npm run start-server -- --provider okta --registry $PROVIDER_REGISTRY_ROOT_DIR
```

#### Test Meta Routes

Test all metadata routes (services, resources, methods) in the provider:

```bash
npm run test-meta-routes -- okta --verbose
```
When you're done testing, stop the StackQL server:

```bash
npm run stop-server
```

use this command to view the server status:

```bash
npm run server-status
```

#### Run test queries

Run some test queries against the provider using the `stackql shell`:

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/provider-dev/openapi"
REG_STR='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}'", "verifyConfig": {"nopVerify": true}}'
./stackql shell --registry="${REG_STR}"
```

### 6. Publish the provider

To publish the provider push the `okta` dir to `providers/src` in a feature branch of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry).  Follow the [registry release flow](https://github.com/stackql/stackql-provider-registry/blob/dev/docs/build-and-deployment.md).  

Launch the StackQL shell:

```bash
export DEV_REG="{ \"url\": \"https://registry-dev.stackql.app/providers\", \"verifyConfig\": { \"nopVerify\": true }}"
./stackql --registry="${DEV_REG}" shell
```

pull the latest dev `okta` provider:

```sql
registry pull okta;
```

Run some test queries, for example...

```sql
SELECT
id,
activated,
created,
lastLogin,
lastUpdated,
passwordChanged,
JSON_EXTRACT(profile, '$.email') as email,
JSON_EXTRACT(profile, '$.firstName') as first_name,
JSON_EXTRACT(profile, '$.lastName') as last_name,
status,
statusChanged
FROM okta.users.users
WHERE subdomain = 'your-subdomain';
```

### 7. Generate web docs

```bash
npm run generate-docs -- \
  --provider-name okta \
  --provider-dir ./provider-dev/openapi/src/okta/v00.00.00000 \
  --output-dir ./website \
  --provider-data-dir ./provider-dev/docgen/provider-data
```  

### 8. Test web docs locally

```bash
cd website
# test build
yarn build

# run local dev server
yarn start
```

### 9. Publish web docs to GitHub Pages

Under __Pages__ in the repository, in the __Build and deployment__ section select __GitHub Actions__ as the __Source__.  In Netlify DNS create the following records:  

| Source Domain | Record Type  | Target |
|---------------|--------------|--------|
| okta-provider.stackql.io | CNAME | stackql.github.io |

## License

MIT

## Contributing

Contributions to the Okta provider are welcome! Please feel free to submit a Pull Request.