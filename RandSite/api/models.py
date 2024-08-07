from django.db import models


class Predictions(models.Model):
    name = models.CharField(max_length=1024)
