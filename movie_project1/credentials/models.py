from django.db import models
from django.contrib.auth.models import User

class Userdetails(models.Model):
    uuser=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20)