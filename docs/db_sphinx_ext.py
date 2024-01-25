def remove_class_signature(app, what, name, obj, options, signature, return_annotation):
    if what == "class":
        # Set the signature to None for classes. Otherwise, there is duplication of the dataclass parameters and
        # documentation, and there is far too much visual noise.
        return (None, return_annotation)
    return (signature, return_annotation)

def setup(app):
    app.connect('autodoc-process-signature', remove_class_signature)
