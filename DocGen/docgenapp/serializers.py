from rest_framework import serializers
from docgenapp import models


# Serializers define the API representation.


class UploadSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField(required=True)

    class Meta:
        fields = ["file_uploaded"]


class UploadFillSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField(required=True)
    keys = serializers.JSONField(required=True)

    class Meta:
        fields = ["file_uploaded", "keys"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("email", "username", "first_name", "last_name")


class TemplateCreatedByAdvisorSerializer(serializers.ModelSerializer):
    advisor = UserSerializer(required=False)

    class Meta:
        model = models.TemplateCreatedByAdvisor
        fields = ("id", "name", "docx_template", "json_template", "advisor")
        read_only_fields = ("id", "advisor")
        

class DocumentTemplateForAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocumentTemplateForAdvisor
        fields = ('name', 'description', 'file')
        read_only_fields = ("id",)
