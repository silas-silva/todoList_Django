from turtle import title
from django.db import models
from uuid import uuid4

# Create your models here.

class todo(models.Model):
    id_todo = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    done = models.BooleanField()