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
    r"get-templates-uploaded-by-advisor", views.UploadTemplateCreatedByAdvisorViewSetForStudentViewSet, basename="templates-uploaded-by-advisor"
)
router.register(
    r"get-templates-for-advisor", views.TemplateForAdvisorViewSet, basename='templates-for-advisor'
)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls))
]
