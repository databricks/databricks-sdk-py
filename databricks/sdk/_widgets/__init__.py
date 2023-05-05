import os
try:
    from .IPyWidgetUtils import IPyWidgetUtil
    from IPython.core.getipython import get_ipython

    if len(list(filter(lambda i: i.__name__ == 'ZMQInteractiveShell', get_ipython().__class__.__mro__))) == 0:
        raise ModuleNotFoundError("Not in interactive shell")
    
    _widget_impl = IPyWidgetUtil

except:
    from .WidgetUtils import DefaultWidgetUtils
    _widget_impl = DefaultWidgetUtils
