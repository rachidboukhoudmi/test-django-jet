import random
from django.core.management.base import BaseCommand
from core.models import Category, Product, Customer, Order, OrderItem

class Command(BaseCommand):
    help = 'Seeds database with fake data for testing Django JET'

    def handle(self, *args, **kwargs):
        self.stdout.write("Generating categories...")
        categories = [Category.objects.create(name=f"Category {i}") for i in range(20)]

        self.stdout.write("Generating products...")
        products = [
            Product.objects.create(
                category=random.choice(categories),
                name=f"Product {i}",
                sku=f"SKU-{i}-{random.randint(1000, 9999)}",
                price=random.uniform(10.0, 500.0),
                stock=random.randint(0, 100),
                available=random.choice([True, False])
            ) for i in range(200)
        ]

        self.stdout.write("Generating customers...")
        customers = [
            Customer.objects.create(
                first_name=f"First{i}",
                last_name=f"Last{i}",
                email=f"customer{i}@example.com",
            ) for i in range(50)
        ]

        self.stdout.write("Generating orders...")
        statuses = ['pending', 'processed', 'shipped', 'delivered', 'cancelled']
        for i in range(100):
            order = Order.objects.create(
                customer=random.choice(customers),
                status=random.choice(statuses),
                total_amount=0 
            )
            
            # Add items to order
            total = 0
            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                qty = random.randint(1, 3)
                OrderItem.objects.create(order=order, product=product, quantity=qty, price=product.price)
                total += product.price * qty
            
            order.total_amount = total
            order.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))