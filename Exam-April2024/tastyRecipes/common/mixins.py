from common.utils import get_profile

class SingleObjectMixin:
    def get_object(self, queryset=None):
        return get_profile()
