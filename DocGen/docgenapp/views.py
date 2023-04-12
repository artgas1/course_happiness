from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import subprocess
from rest_framework.permissions import IsAuthenticated


from wsgiref.util import FileWrapper

from docgenapp import serializers
from docgenapp import models
from docxtpl import DocxTemplate

from rest_framework import generics, mixins, viewsets
from rest_framework import filters


import uuid


# ViewSets define the view behavior.
class ValidateFileViewSet(ViewSet):
    serializer_class = serializers.UploadSerializer

    def create(self, request):
        file_uploaded = request.FILES.get("file_uploaded")

        tpl = DocxTemplate(file_uploaded)
        set_of_variables = tpl.get_undeclared_template_variables()
        return Response({"variables": set_of_variables})


class GenerateFileViewSet(ViewSet):
    def create(self, request):
        serializer = serializers.UploadFillSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        file_uuid_name = str(uuid.uuid4())
        tpl = DocxTemplate(serializer.validated_data["file_uploaded"])
        tpl.render(serializer.validated_data["keys"])
        tpl.save(f"downloads/{file_uuid_name}.docx")

        source_file = f"downloads/{file_uuid_name}.docx"  # original document
        output_folder = "downloads/"  # pdf files will be here

        convert_to_pdf = rf"libreoffice --headless --convert-to pdf {source_file} --outdir {output_folder}"

        subprocess.run(convert_to_pdf, shell=True)
        subprocess.run("ls downloads/", shell=True)

        file = open(f"downloads/{file_uuid_name}.pdf", "rb")

        response = HttpResponse(FileWrapper(file), content_type="application/pdf")

        file.close()

        return response


class UploadTemplateCreatedByAdvisorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.TemplateCreatedByAdvisorSerializer
    queryset = models.TemplateCreatedByAdvisor.objects.all()

    def perform_create(self, serializer):
        serializer.save(advisor=self.request.user)


class UploadTemplateCreatedByAdvisorListForStudents(generics.ListAPIView):
    serializer_class = serializers.TemplateCreatedByAdvisorSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """

        queryset = models.TemplateCreatedByAdvisor.objects.all()
        advisor_email = self.request.query_params.get("advisor_email")
        if advisor_email is not None:
            queryset = queryset.filter(advisor__email=advisor_email)
            return models.TemplateCreatedByAdvisor.objects.filter(
                advisor__email=advisor_email
            )
        else:
            return models.TemplateCreatedByAdvisor.objects.all()


class UploadTemplateCreatedByAdvisorViewSetForStudent(
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = serializers.TemplateCreatedByAdvisorSerializer
    queryset = models.TemplateCreatedByAdvisor.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["advisor__email"]
