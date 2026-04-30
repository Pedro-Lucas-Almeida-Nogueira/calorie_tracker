from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeasuresViewSet

router = DefaultRouter()
router.register('measures', MeasuresViewSet)

urlpatterns = [
    path('', include(router.urls))
]

