from common.utils import get_profile

class SingleObjectMixin:
    def get_object(self, queryset=None):
        return get_profile()


class ReadOnlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
