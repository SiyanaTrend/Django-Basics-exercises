class ReadOnlyFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():  # disabled all fields at once
            field.disabled = True
            # or
            # field.widget.attrs['readonly'] = True  # readonly for all fields at once
