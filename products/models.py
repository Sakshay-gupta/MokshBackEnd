
# Create your models here.
import uuid
from django.db import models
from django.conf import settings
#from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Product(models.Model):
    post_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    rating = models.FloatField()
    reviews = models.IntegerField()
    likes = models.IntegerField()
    size = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    #images= ArrayField(models.CharField(max_length=200, null=True, blank=True), default=list)

    def __str__(self):
        return self.name