from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    objects = None
    Name = models.CharField(max_length=255)


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    availability = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(5)])
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True
    )
