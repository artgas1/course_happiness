from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DocumentTemplateForAdvisor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    file = models.FileField(upload_to="templates_for_advisor")


class TemplateCreatedByAdvisor(models.Model):
    name = models.CharField(max_length=50)
    docx_template = models.FileField(upload_to="docx_templates_created_by_advisor")
    advisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    json_template = models.FileField(upload_to="json_templates_created_by_advisor")
