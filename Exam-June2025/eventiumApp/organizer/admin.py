from django.contrib import admin

from organizer.models import Organizer


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    pass