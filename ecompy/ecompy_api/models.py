from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Comment(models.Model):

    class Meta:
        verbose_name_plural = "entries"
        app_label = 'ecompy_api'

    objects = None
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title


class User(models.Model):
    objects = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, editable=False)
    availability = models.IntegerField(validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)])

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
