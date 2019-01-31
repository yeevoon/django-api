from django.db import models
from datetime import datetime
from .validators import validate_file_extension

class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True) 

    def __str__(self):
        return self.title

class Uploads(models.Model):
    description = models.CharField(max_length=100, blank=True)
    uploaded_file = models.FileField(upload_to='image/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(default=datetime.now, blank=True)

