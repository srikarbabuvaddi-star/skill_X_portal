from django.db import models
from django.contrib.auth.models import User

class CourseMaterial(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_materials')
    title = models.CharField(max_length=200)
    resource_link = models.URLField(help_text="Link to uploaded document, drive asset, or file repo")

    def __str__(self):
        return self.title