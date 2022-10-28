from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50, unique=True)
    phone_no = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
