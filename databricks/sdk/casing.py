class _Name(object):
    """Parses a name in camelCase, PascalCase, snake_case, or kebab-case into its segments."""

    def __init__(self, raw_name: str):
        #
        self._segments = []
        segment = []
        prev_upper = False

        for i, ch in enumerate(raw_name):
            if ch.isupper():
                # Check if next character is lowercase (if exists)
                next_is_lower = i + 1 < len(raw_name) and raw_name[i + 1].islower()

                # Start new segment if:
                # 1. We have content in current segment AND
                # 2. Either previous char was not upper OR next char is lower
                if segment and (not prev_upper or next_is_lower):
                    self._segments.append("".join(segment))
                    segment = [ch.lower()]
                else:
                    segment.append(ch.lower())
                prev_upper = True
            elif ch.islower():
                segment.append(ch)
                prev_upper = False
            else:
                if segment:
                    self._segments.append("".join(segment))
                segment = []
                prev_upper = False
        if segment:
            self._segments.append("".join(segment))

    def to_snake_case(self) -> str:
        return "_".join(self._segments)

    def to_header_case(self) -> str:
        return "-".join([s.capitalize() for s in self._segments])


class Casing(object):

    @staticmethod
    def to_header_case(name: str) -> str:
        """
        Convert a name from camelCase, PascalCase, snake_case, or kebab-case to header-case.
        :param name:
        :return:
        """
        return _Name(name).to_header_case()

    @staticmethod
    def title_case_to_snake_case(name: str) -> str:
        """
        Convert a name from TitleCase/PascalCase to snake_case.

        Example:
            AgentBricksAPI -> agent_bricks_api
            ClustersAPI -> clusters_api

        :param name: The name to convert
        :return: The name in snake_case
        """
        return _Name(name).to_snake_case()


def get_resources(service):
    """
    Get all API resource classes from a service module.

    This function inspects a service module and extracts all classes that end with "API",
    returning their class names along with the corresponding snake_case resource names
    (with "API" suffix removed).

    Example:
        >>> import databricks.sdk.service.agentbricks as agentbricks
        >>> resources = get_resources(agentbricks)
        >>> # Returns: [{"class_name": "AgentBricksAPI", "resource_name": "agent_bricks"}]

    :param service: The service module to inspect
    :return: A list of dictionaries containing class_name and resource_name
    """
    import inspect

    resources = []

    # Get all members of the module
    for name, obj in inspect.getmembers(service):
        # Check if it's a class and ends with "API"
        if inspect.isclass(obj) and name.endswith("API"):
            class_name = name
            # Remove "API" suffix and convert to snake_case
            name_without_api = name[:-3]  # Remove last 3 characters ("API")
            resource_name = Casing.title_case_to_snake_case(name_without_api)

            resources.append({
                "class_name": class_name,
                "resource_name": resource_name
            })

    return resources
