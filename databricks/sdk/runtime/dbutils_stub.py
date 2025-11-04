import typing
from collections import namedtuple


class FileInfo(namedtuple("FileInfo", ["path", "name", "size", "modificationTime"])):
    pass


class MountInfo(namedtuple("MountInfo", ["mountPoint", "source", "encryptionType"])):
    pass


class SecretScope(namedtuple("SecretScope", ["name"])):

    def getName(self):  # type: ignore[no-untyped-def]
        return self.name


class SecretMetadata(namedtuple("SecretMetadata", ["key"])):
    pass


class dbutils:

    class credentials:
        """
        Utilities for interacting with credentials within notebooks
        """

        @staticmethod
        def assumeRole(role: str) -> bool:  # type: ignore[empty-body]
            """
            Sets the role ARN to assume when looking for credentials to authenticate with S3
            """
            ...

        @staticmethod
        def showCurrentRole() -> typing.List[str]:  # type: ignore[empty-body]
            """
            Shows the currently set role
            """
            ...

        @staticmethod
        def showRoles() -> typing.List[str]:  # type: ignore[empty-body]
            """
            Shows the set of possibly assumed roles
            """
            ...

        @staticmethod
        def getCurrentCredentials() -> typing.Mapping[str, str]: ...  # type: ignore[empty-body]

    class data:
        """
        Utilities for understanding and interacting with datasets (EXPERIMENTAL)
        """

        @staticmethod
        def summarize(df: any, precise: bool = False) -> None:  # type: ignore[valid-type]
            """Summarize a Spark/pandas/Koalas DataFrame and visualize the statistics to get quick insights.

            Example: dbutils.data.summarize(df)

            :param df: A pyspark.sql.DataFrame, pyspark.pandas.DataFrame, databricks.koalas.DataFrame
            or pandas.DataFrame object to summarize. Streaming dataframes are not supported.
            :param precise: If false, percentiles, distinct item counts, and frequent item counts
            will be computed approximately to reduce the run time.
            If true, distinct item counts and frequent item counts will be computed exactly,
            and percentiles will be computed with high precision.

            :return: visualization of the computed summmary statistics.
            """
            ...

    class fs:
        """
        Manipulates the Databricks filesystem (DBFS) from the console
        """

        @staticmethod
        def cp(source: str, dest: str, recurse: bool = False) -> bool:  # type: ignore[empty-body]
            """
            Copies a file or directory, possibly across FileSystems
            """
            ...

        @staticmethod
        def head(file: str, max_bytes: int = 65536) -> str:  # type: ignore[empty-body]
            """
            Returns up to the first 'maxBytes' bytes of the given file as a String encoded in UTF-8
            """
            ...

        @staticmethod
        def ls(path: str) -> typing.List[FileInfo]:  # type: ignore[empty-body]
            """
            Lists the contents of a directory
            """
            ...

        @staticmethod
        def mkdirs(dir: str) -> bool:  # type: ignore[empty-body]
            """
            Creates the given directory if it does not exist, also creating any necessary parent directories
            """
            ...

        @staticmethod
        def mv(source: str, dest: str, recurse: bool = False) -> bool:  # type: ignore[empty-body]
            """
            Moves a file or directory, possibly across FileSystems
            """
            ...

        @staticmethod
        def put(file: str, contents: str, overwrite: bool = False) -> bool:  # type: ignore[empty-body]
            """
            Writes the given String out to a file, encoded in UTF-8
            """
            ...

        @staticmethod
        def rm(dir: str, recurse: bool = False) -> bool:  # type: ignore[empty-body]
            """
            Removes a file or directory
            """
            ...

        @staticmethod
        def cacheFiles(*files): ...  # type: ignore[no-untyped-def]

        @staticmethod
        def cacheTable(name: str): ...  # type: ignore[no-untyped-def]

        @staticmethod
        def uncacheFiles(*files): ...  # type: ignore[no-untyped-def]

        @staticmethod
        def uncacheTable(name: str): ...  # type: ignore[no-untyped-def]

        @staticmethod
        def mount(  # type: ignore[empty-body]
            source: str,
            mount_point: str,
            encryption_type: str = "",
            owner: typing.Optional[str] = None,
            extra_configs: typing.Mapping[str, str] = {},
        ) -> bool:
            """
            Mounts the given source directory into DBFS at the given mount point
            """
            ...

        @staticmethod
        def updateMount(  # type: ignore[empty-body]
            source: str,
            mount_point: str,
            encryption_type: str = "",
            owner: typing.Optional[str] = None,
            extra_configs: typing.Mapping[str, str] = {},
        ) -> bool:
            """
            Similar to mount(), but updates an existing mount point (if present) instead of creating a new one
            """
            ...

        @staticmethod
        def mounts() -> typing.List[MountInfo]:  # type: ignore[empty-body]
            """
            Displays information about what is mounted within DBFS
            """
            ...

        @staticmethod
        def refreshMounts() -> bool:  # type: ignore[empty-body]
            """
            Forces all machines in this cluster to refresh their mount cache, ensuring they receive the most recent information
            """
            ...

        @staticmethod
        def unmount(mount_point: str) -> bool:  # type: ignore[empty-body]
            """
            Deletes a DBFS mount point
            """
            ...

    class jobs:
        """
        Utilities for leveraging jobs features
        """

        class taskValues:
            """
            Provides utilities for leveraging job task values
            """

            @staticmethod
            def get(
                taskKey: str,
                key: str,
                default: any = None,  # type: ignore[valid-type]
                debugValue: any = None,  # type: ignore[valid-type]
            ) -> None:
                """
                Returns the latest task value that belongs to the current job run
                """
                ...

            @staticmethod
            def set(key: str, value: any) -> None:  # type: ignore[valid-type]
                """
                Sets a task value on the current task run
                """
                ...

    class library:
        """
        Utilities for session isolated libraries
        """

        @staticmethod
        def restartPython() -> None:
            """
            Restart python process for the current notebook session
            """
            ...

    class notebook:
        """
        Utilities for the control flow of a notebook (EXPERIMENTAL)
        """

        @staticmethod
        def exit(value: str) -> None:
            """
            This method lets you exit a notebook with a value
            """
            ...

        @staticmethod
        def run(  # type: ignore[empty-body]
            path: str,
            timeout_seconds: int,
            arguments: typing.Mapping[str, str],
        ) -> str:
            """
            This method runs a notebook and returns its exit value
            """
            ...

    class secrets:
        """
        Provides utilities for leveraging secrets within notebooks
        """

        @staticmethod
        def get(scope: str, key: str) -> str:  # type: ignore[empty-body]
            """
            Gets the string representation of a secret value with scope and key
            """
            ...

        @staticmethod
        def getBytes(self, scope: str, key: str) -> bytes:  # type: ignore[empty-body, no-untyped-def]
            """Gets the bytes representation of a secret value for the specified scope and key."""

        @staticmethod
        def list(scope: str) -> typing.List[SecretMetadata]:  # type: ignore[empty-body]
            """
            Lists secret metadata for secrets within a scope
            """
            ...

        @staticmethod
        def listScopes() -> typing.List[SecretScope]:  # type: ignore[empty-body]
            """
            Lists secret scopes
            """
            ...

    class widgets:
        """
        provides utilities for working with notebook widgets. You can create different types of widgets and get their bound value
        """

        @staticmethod
        def get(name: str) -> str:  # type: ignore[empty-body]
            """Returns the current value of a widget with give name.
            :param name: Name of the argument to be accessed
            :return: Current value of the widget or default value
            """
            ...

        @staticmethod
        def getArgument(name: str, defaultValue: typing.Optional[str] = None) -> typing.Optional[str]:
            """Returns the current value of a widget with give name.
            :param name: Name of the argument to be accessed
            :param defaultValue: (Deprecated) default value
            :return: Current value of the widget or default value
            """
            ...

        @staticmethod
        def text(name: str, defaultValue: str, label: str = None):  # type: ignore[assignment, no-untyped-def]
            """Creates a text input widget with given name, default value and optional label for
            display
            :param name: Name of argument associated with the new input widget
            :param defaultValue: Default value of the input widget
            :param label: Optional label string for display in notebook and dashboard
            """
            ...

        @staticmethod
        def dropdown(  # type: ignore[no-untyped-def]
            name: str,
            defaultValue: str,
            choices: typing.List[str],
            label: str = None,  # type: ignore[assignment]
        ):
            """Creates a dropdown input widget with given specification.
            :param name: Name of argument associated with the new input widget
            :param defaultValue: Default value of the input widget (must be one of choices)
            :param choices: List of choices for the dropdown input widget
            :param label: Optional label string for display in notebook and dashboard
            """
            ...

        @staticmethod
        def combobox(  # type: ignore[no-untyped-def]
            name: str,
            defaultValue: str,
            choices: typing.List[str],
            label: typing.Optional[str] = None,
        ):
            """Creates a combobox input widget with given specification.
            :param name: Name of argument associated with the new input widget
            :param defaultValue: Default value of the input widget
            :param choices: List of choices for the dropdown input widget
            :param label: Optional label string for display in notebook and dashboard
            """
            ...

        @staticmethod
        def multiselect(  # type: ignore[no-untyped-def]
            name: str,
            defaultValue: str,
            choices: typing.List[str],
            label: typing.Optional[str] = None,
        ):
            """Creates a multiselect input widget with given specification.
            :param name: Name of argument associated with the new input widget
            :param defaultValue: Default value of the input widget (must be one of choices)
            :param choices: List of choices for the dropdown input widget
            :param label: Optional label string for display in notebook and dashboard
            """
            ...

        @staticmethod
        def remove(name: str):  # type: ignore[no-untyped-def]
            """Removes given input widget. If widget does not exist it will throw an error.
            :param name: Name of argument associated with input widget to be removed
            """
            ...

        @staticmethod
        def removeAll():  # type: ignore[no-untyped-def]
            """Removes all input widgets in the notebook."""
            ...


getArgument = dbutils.widgets.getArgument
