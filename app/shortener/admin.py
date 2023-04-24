from django.contrib import admin

from shortener.models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = (
        'original_url',
        'short_code',
        'created_at',
        'owner',
        'number_of_transitions',
    )
    list_display_links = (
        'original_url',
        'short_code',
    )
    readonly_fields = (
        'original_url',
        'short_code',
        'created_at',
        'owner',
        'number_of_transitions',
    )
