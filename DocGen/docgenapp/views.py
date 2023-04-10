
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
import subprocess

from wsgiref.util import FileWrapper

from .serializers import UploadSerializer, UploadFillSerializer
from docxtpl import DocxTemplate

import uuid


# ViewSets define the view behavior.
class ValidateFile(ViewSet):
    serializer_class = UploadSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        tpl = DocxTemplate(file_uploaded)
        set_of_variables = tpl.get_undeclared_template_variables()
        return Response({"variables": set_of_variables})


class GenerateFile(ViewSet):
    def create(self, request):
        serializer = UploadFillSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'errors':  serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        file_uuid_name = str(uuid.uuid4())
        tpl = DocxTemplate(serializer.validated_data['file_uploaded'])
        tpl.render(serializer.validated_data['keys'])
        tpl.save(f"downloads/{file_uuid_name}.docx")

        source_file = f"downloads/{file_uuid_name}.docx"   # original document
        output_folder = "downloads/"   # pdf files will be here

        convert_to_pdf = rf"libreoffice --headless --convert-to pdf {source_file} --outdir {output_folder}"

        subprocess.run(convert_to_pdf, shell=True)
        subprocess.run("ls downloads/", shell=True)

        file = open(f"downloads/{file_uuid_name}.pdf", 'rb')

        response = HttpResponse(FileWrapper(file),
                                content_type='application/pdf')

        file.close()

        return response
