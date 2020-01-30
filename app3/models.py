from django.db import models
from django.db.models import Model

# Create your models here.
class company(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    Phone=models.IntegerField(max_length=10)
    website=models.CharField(max_length=20)

    def  __str__(self):
        return self.name