from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Item, Category, Cart
from django.db.models import Sum
from django.test import TestCase
from .models import Item, Cart, Category

class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # Setting up test data
        self.category = Category.objects.create(name="Cakes")
        self.item = Item.objects.create(
            category=self.category, 
            name="Chocolate Cake", 
            price=20.00
        )
        self.cart = Cart.objects.create(item=self.item, quantity=2)
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_showHome(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakestore/index.html')
        self.assertIn('items', response.context)
        self.assertIn('cart', response.context)

    def test_addCart(self):
        response = self.client.post(reverse('add_cart', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cart.objects.filter(item=self.item).count(), 1)

    def test_checkout_without_login(self):
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, '/login/?next=/checkout/')
    
    def test_checkout_with_login(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakestore/payments.html')

    def test_login_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_logout_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))


class IntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Drinks")
        self.item = Item.objects.create(
            category=self.category, 
            name="Lemonade", 
            price=5.00
        )
        self.user = User.objects.create_user(username='user1', password='password1')

    def test_add_cart_and_checkout_flow(self):
        # Step 1: Add item to cart
        self.client.post(reverse('add_cart', args=[self.item.id]))
        cart = Cart.objects.filter(item=self.item).first()
        self.assertIsNotNone(cart)
        self.assertEqual(cart.quantity, 1)

        # Step 2: Login and checkout
        self.client.login(username='user1', password='password1')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('key', response.context)
        self.assertIn('total', response.context)



class ModelsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Cakes")
        self.item = Item.objects.create(
            category=self.category, 
            name="Red Velvet Cake", 
            price=15.00
        )
        self.cart = Cart.objects.create(item=self.item, quantity=3)

    def test_item_string_representation(self):
        self.assertEqual(str(self.item), "Red Velvet Cake")

    def test_cart_total_ordering(self):
        self.assertEqual(self.cart.total_odering(), 45.00)  # 3 * 15 = 45


class ModelsIntegrationTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Beverages")
        self.item = Item.objects.create(
            category=self.category, 
            name="Tea", 
            price=3.00
        )
        self.cart = Cart.objects.create(item=self.item, quantity=2)

    def test_cart_and_item_interaction(self):
        self.assertEqual(self.cart.total_odering(), 6.00)
        self.assertEqual(self.item.category.name, "Beverages")

    
