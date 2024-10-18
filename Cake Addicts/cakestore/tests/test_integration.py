'''# cakestore/tests/test_integration.py
from django.test import TestCase, Client
from django.urls import reverse
from cakestore.models import Item

class ProductIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()  # Django's test client
        self.product = Item.objects.create(
            name="Chocolate Cake",
            price=15.99,
            description="A delicious chocolate cake",
        )

    def test_product_list_view(self):
        # Test that the product list view returns the correct status code and template
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakestore/product_list.html')
        self.assertContains(response, self.product.name)

    def test_product_detail_view(self):
        # Test that the product detail view shows the correct product info
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.price)
'''

from django.test import TestCase, Client
from django.urls import reverse
from cakestore.models import Item, Cart, Order, orderItem, Category
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io


class CartIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create a test category and item
        self.category = Category.objects.create(name="Cakes")
        self.item = Item.objects.create(
            name="Test Cake",
            price=20.00,
            description="A delicious test cake",
            category=self.category
        )
        #Creating a dummy image file
        self.image = SimpleUploadedFile(
            "test_image.jpg", 
            b"image_content", 
            content_type="image/jpeg"
        )
        

        # Add an item to the cart
        self.cart_item = Cart.objects.create(item=self.item, quantity=2)
    
    def test_cart_view(self):
        """Test that the cart view loads correctly with the items in the cart."""
        response = self.client.get(reverse('Cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakestore/cart.html')
        self.assertContains(response, self.cart_item.item.name)  # Check if the item name appears
        self.assertContains(response, self.cart_item.quantity)  # Check if the item quantity appears
    
    def test_add_to_cart(self):
        """Test that an item can be added to the cart."""
        response = self.client.get(reverse('addCart', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)  # Expect a redirect after adding to cart
        self.assertTrue(Cart.objects.filter(item=self.item).exists())  # Check if the item is in the cart

    def test_delete_from_cart(self):
        """Test that an item can be removed from the cart."""
        cart = Cart.objects.create(item=self.item, quantity=1)
        response = self.client.get(reverse('delete_from_cart', args=[cart.id]))
        self.assertEqual(response.status_code, 302)  # Expect a redirect after deletion
        self.assertFalse(Cart.objects.filter(id=cart.id).exists())  # Check if the item was deleted
    
    def test_checkout_view(self):
        """Test that the checkout view loads correctly."""
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakestore/payments.html')
        # self.assertContains(response, 'https://checkout.stripe.com/checkout.js')  
    
    
class PaymentIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Create and login user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create a test item and cart item
        self.item = Item.objects.create(name="Test Cake", price=20.00, description="A delicious test cake")
        self.cart_item = Cart.objects.create(item=self.item, quantity=2)

    def test_payment_view(self):
        """Test that the payment view loads correctly."""
        response = self.client.get(reverse('payments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakestore/payments.html')
        self.assertContains(response, 'Total')  # Assuming the word 'Total' is in the template


class OrderIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Create and login user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create test items and an order
        self.item = Item.objects.create(name="Test Cake", price=20.00, description="A delicious test cake")
        self.cart_item = Cart.objects.create(item=self.item, quantity=2)
        self.order_item = orderItem.objects.create(item=self.item, quantity=2)
        self.order = Order.objects.create(User=self.user, item=self.item, quantity=2, total_ordering=40.00)

    def test_order_view(self):
        """Test that the order view displays placed orders."""
        response = self.client.get(reverse('orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cakestore/orders.html')
        self.assertContains(response, self.order.item.name)  # Check if order item is displayed
        self.assertContains(response, self.order.quantity)  # Check if order quantity is displayed

    def test_cash_on_delivery(self):
        """Test that an order is created via cash on delivery."""
        response = self.client.get(reverse('cash_on_delivery'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Order.objects.exists())  # Verify that an order was created
        self.assertTemplateUsed(response, 'cakestore/menu.html')
