from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    is_purchased = models.BooleanField(default=False)
