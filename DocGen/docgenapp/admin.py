from django.contrib import admin
from docgenapp.models import DocumentTemplateForAdvisor, TemplateCreatedByAdvisor

# Register your models here.


@admin.register(DocumentTemplateForAdvisor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "file"]


@admin.register(TemplateCreatedByAdvisor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "advisor", "docx_template", "json_template"]
