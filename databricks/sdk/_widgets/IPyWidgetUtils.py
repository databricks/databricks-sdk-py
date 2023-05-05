import typing

from IPython.core.display_functions import display
from ipywidgets.widgets import (ValueWidget, Widget, widget_box,
                                widget_selection, widget_string)

from .WidgetUtils import _WidgetUtils


class DbUtilsWidget:

    def __init__(self, label: str, valueWidget: ValueWidget) -> None:
        self.lavelWidget = widget_string.Label(label)
        self.valueWidget = valueWidget
        self.box = widget_box.Box([self.lavelWidget, self.valueWidget])

    def display(self):
        display(self.box)

    def close(self):
        self.lavelWidget.close()
        self.valueWidget.close()
        self.box.close()

    def __del__(self):
        self.close()

    @property
    def value(self):
        value = self.valueWidget.value
        if type(value) == str or value is None:
            return value
        if type(value) == list or type(value) == tuple:
            return ','.join(value)

        raise ValueError("The returned value has invalid type (" + type(value) + ").")


class IPyWidgetUtil(_WidgetUtils):

    def __init__(self) -> None:
        self.__widgets: typing.Dict[str, DbUtilsWidget] = {}

    def __register(self, name: str, widget: ValueWidget, label: typing.Optional[str] = None):
        label = label if label is not None else name
        w = DbUtilsWidget(label, widget)
        self.__widgets[name] = w
        w.display()

    def text(self, name: str, defaultValue: str, label: typing.Optional[str] = None):
        self.__register(name, widget_string.Text(defaultValue), label)

    def dropdown(self,
                 name: str,
                 defaultValue: str,
                 choices: typing.List[str],
                 label: typing.Optional[str] = None):
        self.__register(name, widget_selection.Dropdown(value=defaultValue, options=choices), label)

    def combobox(self,
                 name: str,
                 defaultValue: str,
                 choices: typing.List[str],
                 label: typing.Optional[str] = None):
        self.__register(name, widget_string.Combobox(value=defaultValue, options=choices), label)

    def multiselect(self,
                    name: str,
                    defaultValue: str,
                    choices: typing.List[str],
                    label: typing.Optional[str] = None):
        self.__register(
            name,
            widget_selection.SelectMultiple(value=(defaultValue, ),
                                            options=[("__EMPTY__", ""), *list(zip(choices, choices))]), label)

    @property
    def _widgetNames(self) -> typing.List[str]:
        return list(self.__widgets.keys())

    def _get(self, name: str) -> str:
        return self.__widgets[name].value

    def _remove(self, name: str):
        del self.__widgets[name]

    def _removeAll(self):
        Widget.close_all()
        self.__widgets = {}
