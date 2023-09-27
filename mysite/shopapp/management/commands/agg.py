from typing import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg, Max, Min, Count, Sum
from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo aggregate")

        #result = Product.objects.filter(
        #    name__contains="Smartphone"
        #).aggregate(
        #    Avg("price"),
        #    Max("price"),
        #    min_price=Min("price"),
        #    count=Count("price"),
        #)

        #print(result)

        orders = Order.objects.annotate(
            total=Sum("products__price", default=0),
            products_count=Count("products")
        )

        for order in orders:
            print(
                f"Order #{order.id} "
                f"with {order.products_count} "
                f"products worth {order.total}"
            )

        self.stdout.write(f"Done")
