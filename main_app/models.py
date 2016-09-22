from __future__ import unicode_literals

# Import Django's default User model:
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Parameters of the class indicate inheritance.
class Treasure(models.Model):
    # Mark the User model as a ForeignKey in the Treasure model:
    user = models.ForeignKey(User)
    # Database types follow the model instance:
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # upload_to is the location in the media directory where we will add the images.
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
