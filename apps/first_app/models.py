from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['show_title']) < 2:
            errors["show_title"] = "Title should be at least 2 characters"
        if len(postData['show_network']) < 10:
            errors["show_network"] = "Network should be at least 10 characters"
        if len(postData['show_description']) < 10:
            errors["show_description"] = "Description should be at least 10 characters"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    releaseDate = models.DateField()
    description = models.TextField()
    objects = ShowManager()

