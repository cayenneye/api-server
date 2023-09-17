from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from secret_messages.models.secret_medias import SecretMedia
from secret_messages.models.secret_message_themes import SecretMessageTheme
from secret_messages.models.secret_messages import SecretMessage


class SecretMessageThemeResource(resources.ModelResource):

    def get_export_fields(self):
        return [
            field for field in super().get_export_fields()
            if field.column_name in ('description_template_text', 'button_text')
        ]

    class Meta:
        model = SecretMessageTheme


class SecretMessageResource(resources.ModelResource):

    class Meta:
        model = SecretMessage


class SecretMediaResource(resources.ModelResource):

    class Meta:
        model = SecretMedia


@admin.register(SecretMessageTheme)
class SecretMessageThemeAdmin(ImportExportModelAdmin):
    resource_class = SecretMessageThemeResource
    list_filter = ('is_hidden',)
    list_display = ('description_template_text', 'button_text')
    ordering = ('-created_at',)


@admin.register(SecretMessage)
class SecretMessageAdmin(ImportExportModelAdmin):
    resource_class = SecretMessageResource
    ordering = ('-created_at',)
    list_display = ('id', 'created_at', 'text')
    sortable_by = ('created_at',)
    search_fields = ('text',)
    search_help_text = 'Search by text content'
    date_hierarchy = 'created_at'


@admin.register(SecretMedia)
class SecretMediaAdmin(ImportExportModelAdmin):
    resource_class = SecretMediaResource
    list_filter = ('contact', 'media_type')
    list_display = ('id', 'media_type', 'contact')
    ordering = ('-created_at',)
