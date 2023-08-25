from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from django.utils.translation import gettext as _


class IngredientsTypes(models.Choices):
    Dough = 'Dough'
    Spicery = 'Spicery'
    Sauce = 'Sauce'
    Meat_products = 'Meat_products'
    Cheese = 'Cheese'

    def __str__(self):
        return self.name


# Create your models here.
class Ingredients(models.Model):
    class Meta:
        db_table = 'ingredient'
        verbose_name = _('Ingredients')
        verbose_name_plural = _('Ingredients')

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=IngredientsTypes.choices)
    time = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="photo")
    quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.name
