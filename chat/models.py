from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    members = models.ManyToManyField('user.User', related_name='members')
