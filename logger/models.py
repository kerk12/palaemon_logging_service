from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=128)

class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    contents = models.TextField()
