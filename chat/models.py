from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    members = models.ManyToManyField('user.User', related_name='members')


class Messages(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    message = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
