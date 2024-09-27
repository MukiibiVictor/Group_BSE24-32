from django.test import TestCase
from .models import Item, Category

class ItemModelTest(TestCase):
    
    def setUp(self):
        # Create a sample Category object for ForeignKey relation
        self.category = Category.objects.create(name='Electronics')
        
        # Create a sample Item object
        self.item = Item.objects.create(
            category=self.category,
            name='Smartphone',
            price=299.99,
            description='Latest model with advanced features',
            image=None
        )

    def test_item_creation(self):
        """Test if the Item object is created correctly"""
        item = self.item
        self.assertIsInstance(item, Item)
        self.assertEqual(item.name, 'Smartphone')
        self.assertEqual(item.price, 299.99)

    def test_item_string_representation(self):
        """Test the __str__ method of the Item model"""
        item = self.item
        self.assertEqual(str(item), 'Smartphone')

    def test_item_category(self):
        """Test the relationship between Item and Category"""
        item = self.item
        self.assertEqual(item.category.name, 'Electronics')
