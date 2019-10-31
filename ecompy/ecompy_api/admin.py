from django.contrib import admin

from .models import Comment, User, Product

admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(User)
