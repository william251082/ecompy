from django.test import TestCase

from .models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name="ipad", description="Sedutperspiciatis", availability=3, user_id=1)
        Product.objects.create(name="earphone", description="perspiciatis", availability=3, user_id=1)

    def test_string_representation(self):
        product = Product(name="My product name")
        self.assertEqual(str(product), product.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Product._meta.verbose_name_plural), "products")
