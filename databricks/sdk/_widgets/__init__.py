try:
    from .IPyWidgetUtils import IPyWidgetUtil
    _widget_impl = IPyWidgetUtil
except:
    from .WidgetUtils import DefaultWidgetUtils
    _widget_impl = DefaultWidgetUtils
