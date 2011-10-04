from django.db import models
from database_files.manager import FileManager

class File(models.Model):
    name = models.TextField()
    content = models.TextField()
    size = models.IntegerField()
    
    objects = FileManager()

