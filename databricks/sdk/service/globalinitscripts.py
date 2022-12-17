# Code generated from OpenAPI specs by Databricks SDK Generator. DO NOT EDIT.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Any


# all definitions in this file are in alphabetical order


@dataclass
class CreateResponse:

    # The global init script ID.
    script_id: str

    def as_dict(self) -> dict:
        body = {}
        if self.script_id:
            body["script_id"] = self.script_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "CreateResponse":
        return cls(
            script_id=d.get("script_id", None),
        )


@dataclass
class Delete:
    """Delete init script"""

    # The ID of the global init script.
    script_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.script_id:
            body["script_id"] = self.script_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Delete":
        return cls(
            script_id=d.get("script_id", None),
        )


@dataclass
class Get:
    """Get an init script"""

    # The ID of the global init script.
    script_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.script_id:
            body["script_id"] = self.script_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "Get":
        return cls(
            script_id=d.get("script_id", None),
        )


@dataclass
class GlobalInitScriptCreateRequest:

    # Specifies whether the script is enabled. The script runs only if enabled.
    enabled: bool
    # The name of the script
    name: str
    # The position of a global init script, where 0 represents the first script to run, 1 is the second script to run,
    # in ascending order.
    #
    # If you omit the numeric position for a new global init script, it defaults to last position. It will run after all
    # current scripts. Setting any value greater than the position of the last script is equivalent to the last
    # position. Example: Take three existing scripts with positions 0, 1, and 2. Any position of (3) or greater puts the
    # script in the last position. If an explicit position value conflicts with an existing script value, your request
    # succeeds, but the original script at that position and all later scripts have their positions incremented by 1.
    position: int
    # The Base64-encoded content of the script.
    script: str

    def as_dict(self) -> dict:
        body = {}
        if self.enabled:
            body["enabled"] = self.enabled
        if self.name:
            body["name"] = self.name
        if self.position:
            body["position"] = self.position
        if self.script:
            body["script"] = self.script

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GlobalInitScriptCreateRequest":
        return cls(
            enabled=d.get("enabled", None),
            name=d.get("name", None),
            position=d.get("position", None),
            script=d.get("script", None),
        )


@dataclass
class GlobalInitScriptDetails:

    # Time when the script was created, represented as a Unix timestamp in milliseconds.
    created_at: int
    # The username of the user who created the script.
    created_by: str
    # Specifies whether the script is enabled. The script runs only if enabled.
    enabled: bool
    # The name of the script
    name: str
    # The position of a script, where 0 represents the first script to run, 1 is the second script to run, in ascending
    # order.
    position: int
    # The global init script ID.
    script_id: str
    # Time when the script was updated, represented as a Unix timestamp in milliseconds.
    updated_at: int
    # The username of the user who last updated the script
    updated_by: str

    def as_dict(self) -> dict:
        body = {}
        if self.created_at:
            body["created_at"] = self.created_at
        if self.created_by:
            body["created_by"] = self.created_by
        if self.enabled:
            body["enabled"] = self.enabled
        if self.name:
            body["name"] = self.name
        if self.position:
            body["position"] = self.position
        if self.script_id:
            body["script_id"] = self.script_id
        if self.updated_at:
            body["updated_at"] = self.updated_at
        if self.updated_by:
            body["updated_by"] = self.updated_by

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GlobalInitScriptDetails":
        return cls(
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            enabled=d.get("enabled", None),
            name=d.get("name", None),
            position=d.get("position", None),
            script_id=d.get("script_id", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class GlobalInitScriptDetailsWithContent:

    # Time when the script was created, represented as a Unix timestamp in milliseconds.
    created_at: int
    # The username of the user who created the script.
    created_by: str
    # Specifies whether the script is enabled. The script runs only if enabled.
    enabled: bool
    # The name of the script
    name: str
    # The position of a script, where 0 represents the first script to run, 1 is the second script to run, in ascending
    # order.
    position: int
    # The Base64-encoded content of the script.
    script: str
    # The global init script ID.
    script_id: str
    # Time when the script was updated, represented as a Unix timestamp in milliseconds.
    updated_at: int
    # The username of the user who last updated the script
    updated_by: str

    def as_dict(self) -> dict:
        body = {}
        if self.created_at:
            body["created_at"] = self.created_at
        if self.created_by:
            body["created_by"] = self.created_by
        if self.enabled:
            body["enabled"] = self.enabled
        if self.name:
            body["name"] = self.name
        if self.position:
            body["position"] = self.position
        if self.script:
            body["script"] = self.script
        if self.script_id:
            body["script_id"] = self.script_id
        if self.updated_at:
            body["updated_at"] = self.updated_at
        if self.updated_by:
            body["updated_by"] = self.updated_by

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GlobalInitScriptDetailsWithContent":
        return cls(
            created_at=d.get("created_at", None),
            created_by=d.get("created_by", None),
            enabled=d.get("enabled", None),
            name=d.get("name", None),
            position=d.get("position", None),
            script=d.get("script", None),
            script_id=d.get("script_id", None),
            updated_at=d.get("updated_at", None),
            updated_by=d.get("updated_by", None),
        )


@dataclass
class GlobalInitScriptUpdateRequest:

    # Specifies whether the script is enabled. The script runs only if enabled.
    enabled: bool
    # The name of the script
    name: str
    # The position of a script, where 0 represents the first script to run, 1 is the second script to run, in ascending
    # order. To move the script to run first, set its position to 0.
    #
    # To move the script to the end, set its position to any value greater or equal to the position of the last script.
    # Example, three existing scripts with positions 0, 1, and 2. Any position value of 2 or greater puts the script in
    # the last position (2).
    #
    # If an explicit position value conflicts with an existing script, your request succeeds, but the original script at
    # that position and all later scripts have their positions incremented by 1.
    position: int
    # The Base64-encoded content of the script.
    script: str
    # The ID of the global init script.
    script_id: str  # path

    def as_dict(self) -> dict:
        body = {}
        if self.enabled:
            body["enabled"] = self.enabled
        if self.name:
            body["name"] = self.name
        if self.position:
            body["position"] = self.position
        if self.script:
            body["script"] = self.script
        if self.script_id:
            body["script_id"] = self.script_id

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "GlobalInitScriptUpdateRequest":
        return cls(
            enabled=d.get("enabled", None),
            name=d.get("name", None),
            position=d.get("position", None),
            script=d.get("script", None),
            script_id=d.get("script_id", None),
        )


@dataclass
class ListGlobalInitScriptsResponse:

    scripts: "List[GlobalInitScriptDetails]"

    def as_dict(self) -> dict:
        body = {}
        if self.scripts:
            body["scripts"] = [v.as_dict() for v in self.scripts]

        return body

    @classmethod
    def from_dict(cls, d: Dict[str, any]) -> "ListGlobalInitScriptsResponse":
        return cls(
            scripts=[GlobalInitScriptDetails.from_dict(v) for v in d["scripts"]]
            if "scripts" in d
            else None,
        )


class GlobalInitScriptsAPI:
    def __init__(self, api_client):
        self._api = api_client

    def create(
        self,
        name: str,
        script: str,
        *,
        enabled: bool = None,
        position: int = None,
        **kwargs,
    ) -> CreateResponse:
        """Create init script.

        Creates a new global init script in this workspace."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GlobalInitScriptCreateRequest(
                enabled=enabled, name=name, position=position, script=script
            )
        body = request.as_dict()

        json = self._api.do("POST", "/api/2.0/global-init-scripts", body=body)
        return CreateResponse.from_dict(json)

    def delete(self, script_id: str, **kwargs):
        """Delete init script.

        Deletes a global init script."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Delete(script_id=script_id)

        self._api.do("DELETE", f"/api/2.0/global-init-scripts/{request.script_id}")

    def get(self, script_id: str, **kwargs) -> GlobalInitScriptDetailsWithContent:
        """Get an init script.

        Gets all the details of a script, including its Base64-encoded contents."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = Get(script_id=script_id)

        json = self._api.do("GET", f"/api/2.0/global-init-scripts/{request.script_id}")
        return GlobalInitScriptDetailsWithContent.from_dict(json)

    def list(self) -> ListGlobalInitScriptsResponse:
        """Get init scripts.

        "Get a list of all global init scripts for this workspace. This returns
        all properties for each script but **not** the script contents. To
        retrieve the contents of a script, use the [get a global init
        script](#operation/get-script) operation."""

        json = self._api.do("GET", "/api/2.0/global-init-scripts")
        return ListGlobalInitScriptsResponse.from_dict(json)

    def update(
        self,
        name: str,
        script: str,
        script_id: str,
        *,
        enabled: bool = None,
        position: int = None,
        **kwargs,
    ):
        """Update init script.

        Updates a global init script, specifying only the fields to change. All
        fields are optional. Unspecified fields retain their current value."""
        request = kwargs.get("request", None)
        if not request:  # request is not given through keyed args
            request = GlobalInitScriptUpdateRequest(
                enabled=enabled,
                name=name,
                position=position,
                script=script,
                script_id=script_id,
            )
        body = request.as_dict()

        self._api.do(
            "PATCH", f"/api/2.0/global-init-scripts/{request.script_id}", body=body
        )
