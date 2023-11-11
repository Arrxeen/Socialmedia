from django.db import models
from datetime import datetime
# from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    link = models.TextField()
    date = models.DateField(null=True,blank=True,default=datetime.utcnow)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"