import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    ukuran = models.TextField()
    aroma = models.TextField()
    top_notes = models.TextField()
    middle_notes = models.TextField()
    base_notes = models.TextField()