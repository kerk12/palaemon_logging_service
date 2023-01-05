from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title"]

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = "__all__"
    
    def to_representation(self, instance):
        out = super().to_representation(instance)
        if instance.category is not None:
            out["category"] = instance.category.title
        return out

    def to_internal_value(self, data):
        if "category" in data:
            data["category"] = get_object_or_404(Category, title__iexact=data["category"]).pk

        out = super().to_internal_value(data)
        return out