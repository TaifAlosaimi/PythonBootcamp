from django.db import models


class Product(models.Model):
    quantity = models.IntegerField(default=0)
    code = models.CharField(max_length=30, unique=True)