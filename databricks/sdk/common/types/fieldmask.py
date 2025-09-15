class FieldMask(object):
    """Class for FieldMask message type."""

    def ToJsonString(self):
        """Converts FieldMask to string."""
        return ",".join(self.paths)

    def FromJsonString(self, value):
        """Converts string to FieldMask."""
        if not isinstance(value, str):
            raise ValueError("FieldMask JSON value not a string: {!r}".format(value))
        if value:
            self.paths = value.split(",")
        else:
            self.paths = []
