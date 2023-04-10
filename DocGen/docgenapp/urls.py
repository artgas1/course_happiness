from django.urls import path, include
from rest_framework import routers
from .views import ValidateFile, GenerateFile

router = routers.DefaultRouter()
router.register(r'validate-file', ValidateFile, basename="upload")
router.register(r'generate-file', GenerateFile, basename="generate")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]