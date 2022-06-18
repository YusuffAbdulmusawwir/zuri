from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
user=get_user_model()
class post(models.Model):
    title = models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(user, on_delete=models.CASCADE)
    published=models.DateTimeField()
