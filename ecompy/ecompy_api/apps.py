from django.apps import AppConfig


class EcompyApiConfig(AppConfig):
    name = 'ecompy_api'

    def ready(self):
        from ecompy_api.admin import Comment, Product, User