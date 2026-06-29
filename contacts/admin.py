from django.contrib import admin
from .models import Contact, EmergencyContact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ("name", "phone", "email", "user")

    search_fields = ("name", "phone", "email")


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):

    list_display = (
        "service",
        "city",
        "state",
        "country",
        "phone",
    )

    list_filter = (
        "service",
        "state",
        "country",
    )

    search_fields = (
        "city",
        "service",
        "phone",
    )

