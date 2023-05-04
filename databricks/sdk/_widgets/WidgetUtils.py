

from abc import ABC, abstractmethod
import typing


class _WidgetUtils(ABC):

    @property
    @abstractmethod
    def _widgetNames(self) -> typing.List[str]:
        pass

    def get(self, name: str):
        return self._get(name)

    def getArgument(self, name: str, defaultValue: typing.Optional[str] = None):
        try:
            return self.get(name)
        except Exception as e:
            return defaultValue

    @abstractmethod
    def _get(self, name: str) -> str:
        pass

    def remove(self, name: str):
        self._remove(name)

    @abstractmethod
    def _remove(self, name: str):
        pass

    def removeAll(self):
        self._removeAll()

    @abstractmethod
    def _removeAll(self):
        pass


class DefaultWidgetUtils(_WidgetUtils):
    def __init__(self) -> None:
        self.__widgets: typing.Dict[str, str] = {}

    def text(self, name: str, defaultValue: str, label: typing.Optional[str] = None):
        self.__widgets[name] = defaultValue

    def dropdown(self,
                 name: str,
                 defaultValue: str,
                 choices: typing.List[str],
                 label: typing.Optional[str] = None):
        self.__widgets[name] = defaultValue

    def combobox(self,
                 name: str,
                 defaultValue: str,
                 choices: typing.List[str],
                 label: typing.Optional[str] = None):
        self.__widgets[name] = defaultValue

    def multiselect(self,
                    name: str,
                    defaultValue: str,
                    choices: typing.List[str],
                    label: typing.Optional[str] = None):
        self.__widgets[name] = defaultValue

 
    def _get(self, name: str) -> str:
        return self.__widgets[name]
    
    def _remove(self, name: str):
        del self.__widgets[name]

    def _removeAll(self):
        self.__widgets = {}
