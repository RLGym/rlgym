
def auto_init_slots(cls):
    # Utility wrapper to create a default __init__ function for a class with slots
    slots = getattr(cls, "__slots__", ())

    def __init__(self):
        for attr in slots:
            setattr(self, attr, None)

    cls.__init__ = __init__
    return cls
