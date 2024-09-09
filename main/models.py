from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    ukuran = models.TextField()
    aroma = models.TextField()
    top_notes = models.TextField()
    middle_notes = models.TextField()
    base_notes = models.TextField()