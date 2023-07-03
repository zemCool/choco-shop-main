import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

TYPE_BLACK = 'black'
TYPE_WHITE = 'white'
TYPE_MILKY = 'milky'
TYPE_BITTER = 'bitter'
TYPE_DESSERT = 'dessert'


def images_path():
    return os.path.join(settings.MEDIA_ROOT, 'images')


class User(AbstractUser):
    pass


class City(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Chocolate(models.Model):

    STATUS_CHOICES = [
        (TYPE_BLACK, 'black'),
        (TYPE_WHITE, 'white chocolate'),
        (TYPE_MILKY, 'milky chocolate'),
        (TYPE_BITTER, 'bitter chocolate'),
        (TYPE_DESSERT, 'dessert chocolate'),
    ]
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=STATUS_CHOICES, default=TYPE_BLACK)
    description = models.TextField(max_length=250, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to=images_path(), null=True)

    def __str__(self):
        return (
            f'{self.brand} {self.type}'
        ).format()


class Order(models.Model):

    user = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, default='Bishkek', null=True)
    street = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    chocolate = models.ForeignKey(Chocolate, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)




