from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Item, Cart, cartItem, Order, orderItem

class CategoryModelTests(TestCase):
    
    def test_string_representation(self):
        category = Category(name="Electronics")
        self.assertEqual(str(category), category.name)


class ItemModelTests(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(
            category=self.category,
            name="Laptop",
            price=999.99,
            description="A high-performance laptop."
        )

    def test_string_representation(self):
        self.assertEqual(str(self.item), self.item.name)

    def test_item_creation(self):
        self.assertEqual(self.item.category, self.category)
        self.assertEqual(self.item.price, 999.99)
        self.assertEqual(self.item.description, "A high-performance laptop.")


class CartModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(category=self.category, name="Laptop", price=999.99)
        self.cart = Cart.objects.create(item=self.item, quantity=2)

    def test_string_representation(self):
        self.assertEqual(str(self.cart), self.cart.item.name)

    def test_total_ordering(self):
        self.assertEqual(self.cart.total_odering, 1999.98)


class CartItemModelTests(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(category=self.category, name="Laptop", price=999.99)
        self.cart = Cart.objects.create(item=self.item, quantity=2)
        self.cart_item = cartItem.objects.create(cart=self.cart, item=self.item, quantity=3)

    def test_string_representation(self):
        self.assertEqual(str(self.cart_item), self.cart_item.item.name)


class OrderModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(category=self.category, name="Laptop", price=999.99)
        self.order = Order.objects.create(User=self.user, item=self.item, quantity=1)

    def test_string_representation(self):
        self.assertEqual(str(self.order), str(self.order.item))

    def test_total_ordering(self):
        self.assertEqual(self.order.total_odering, 999.99)


class OrderItemModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(category=self.category, name="Laptop", price=999.99)
        self.order = Order.objects.create(User=self.user, item=self.item, quantity=1)
        self.order_item = orderItem.objects.create(order=self.order, item=self.item, quantity=2)

    def test_string_representation(self):
        self.assertEqual(str(self.order_item), self.order_item.item.name)

