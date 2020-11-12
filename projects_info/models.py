from django.db import models

# Create your models here.

class Monthly_expense(models.Model):
    amount = models.FloatField()
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=1)