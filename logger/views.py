from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django.db.models import Q
# Create your views here.

class LogEntryViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin):
  queryset = LogEntry.objects.all().order_by('-timestamp')
  serializer_class = LogEntrySerializer

  @action(detail=False, methods=['get'])
  def search(self, request):
    search_term = request.GET.get('q', None)
    return Response(LogEntrySerializer(LogEntry.objects.filter(
      Q(contents__icontains=search_term) | Q(category__title__icontains=search_term)
    ), many=True).data)

class CategoryViewSet(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer