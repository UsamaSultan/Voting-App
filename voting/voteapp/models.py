import django
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Restaurant(models.Model):
    full_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    mobile = models.CharField(
        validators=[phone_regex], max_length=10, blank=True)
    about = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.full_name


class Menu(models.Model):
    belongsTo = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True, default='')
    item_name = models.CharField(max_length=50)
    price = models.IntegerField(blank=False)
    about = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.item_name


class Voting(models.Model):
    date = models.DateField(default=django.utils.timezone.now)
    likes = models.ManyToManyField(
        User, related_name='related_likes', blank=True, default='')
    links_to_menu = models.OneToOneField(
        Menu, on_delete=models.CASCADE, related_name='related_links', blank=True, default='')
    result = models.PositiveIntegerField(blank=False)
