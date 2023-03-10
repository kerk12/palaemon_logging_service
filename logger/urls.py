from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
router = DefaultRouter()
router.register('entry', LogEntryViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
  path('', include(router.urls))
]
