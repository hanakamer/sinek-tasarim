from django.db import models
from django.conf import settings
from colorful.fields import RGBColorField
from django.template.defaultfilters import truncatewords

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='static/media/')
    tags = models.ManyToManyField('Tag', related_name='products')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    wish_list = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_list')
    color_tags = models.ManyToManyField('ColorTag', related_name='products_of_color')
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    def __str__(self):
        return self.title
    @property
    def description_short(self):
        return truncatewords(self.description, 10)

    def liked_user_ids(self):
        return self.likes.values_list("id", flat=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, related_name='sub_tags', blank=True)
    def __str__(self):
        return self.name

class ColorTag(models.Model):
    color = RGBColorField()
    parent = models.ForeignKey('self', null=True, related_name='sub_colors', blank=True)
    def __str__(self):
        return self.color



