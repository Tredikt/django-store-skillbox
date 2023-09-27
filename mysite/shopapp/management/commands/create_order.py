from typing import Sequence

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from django.db import transaction
from shopapp.models import Order, Product


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Create order with products")
        user = User.objects.get(username="admin")
        # products: Sequence[Product] = Product.objects.defer("description", "price", "created_at").all() # в defer() указываются ненужные поля
        products: Sequence[Product] = Product.objects.only("pk").all() # в only() передаётся то, что нужно загрузить
        order, created = Order.objects.get_or_create(
            delivery_address="ul Key, d 8",
            promocode="promo4",
            user=user,
        )
        for product in products:
            order.products.add(product) # загрузка значений товаров в таблицу связи товаров
                                        # сначала идёт заказ order - id заказа, а затем id products
        self.stdout.write(f"Created order {order}")
