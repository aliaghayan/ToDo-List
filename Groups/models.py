from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    description = models.TextField()
    icon = models.ImageField(upload_to='images/')
    status = models.BooleanField(default=False)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %y ')

    def __str__(self):
        return self.name

class Todo(models.Model):
    text = models.CharField(max_length=150)
    complete = models.BooleanField(default=False)
    assigned_to = models.CharField(max_length=40)

    def __str__(self):
        return self.text
