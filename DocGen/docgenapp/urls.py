from django.urls import path, include, re_path
from rest_framework import routers
from docgenapp import views

router = routers.DefaultRouter()
router.register(r"validate-file", views.ValidateFileViewSet, basename="upload")
router.register(r"generate-file", views.GenerateFileViewSet, basename="generate")
router.register(
    r"upload-template-created-by-advisor",
    views.UploadTemplateCreatedByAdvisorViewSet,
    basename="upload-template-created-by-advisor",
)
router.register(
    r"keking", views.UploadTemplateCreatedByAdvisorViewSetForStudent, basename="kek"
)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "advisor_templates/",
        views.UploadTemplateCreatedByAdvisorListForStudents.as_view(),
        name="UploadTemplateCreatedByAdvisorListForStudents",
    ),
]
