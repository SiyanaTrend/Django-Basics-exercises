class ReadOnlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True


# option 2 - readonly and disabled, with option to choose, which fields to be disabled and readonly
# class ReadOnlyMixin:
#     read_only_fields = []
#
#     def make_fields_readonly(self):
#         for field_name in self.read_only_fields:
#             if field_name in self.fields:
#                 self.fields[field_name].widget.attrs['readonly'] = True
#                 self.fields[field_name].widget.attrs['disabled'] = True  # for better protection
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.make_fields_readonly()
