# this mixin use field_name and make only first letter capitalize:

# class PlaceholderMixin:
#     def add_placeholders(self):
#         for field_name, field in self.fields.items():  # ('first_name': field_obj)
#             placeholder = field.label or field_name.replace('_', ' ').capitalize()
#             field.widget.attrs['placeholder'] = placeholder
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.add_placeholders()


class PlaceholderMixin:
    def add_placeholders(self):
        # get labels from Meta, if there are labels
        labels = getattr(self.Meta, 'labels', {}) if hasattr(self, 'Meta') else {}

        for field_name, field in self.fields.items():
            # Priority: label from Meta -> field.label -> generated from field_name
            placeholder = labels.get(field_name) or field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs.setdefault('placeholder', placeholder)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


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
