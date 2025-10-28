from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10)
