from rest_framework.serializers import Serializer, FileField, JSONField

# Serializers define the API representation.


class UploadSerializer(Serializer):
    file_uploaded = FileField(required=True)

    class Meta:
        fields = ['file_uploaded']


class UploadFillSerializer(Serializer):
    file_uploaded = FileField(required=True)
    keys = JSONField(required=True)

    class Meta:
        fields = ['file_uploaded', 'keys']
