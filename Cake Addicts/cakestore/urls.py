from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# URL patterns for handling user authentication, profile, menu, payments, etc.
urlpatterns = [
    # Login page
    path('login_user/', views.login_user, name="login"),

    # Logout page
    path('logout_user/', views.logout_user, name='logout'),

    # User registration page
    path('register_user/', views.register_user, name='register'),

    # Profile page (where users can view or edit their profile)
    path('profile/', views.profile, name='profile'),

    # Static page for 'About Us'
    path('about/', views.showAbout, name = 'about'),

    # Page for showing payment options or details
    path('payment/', views.showPayment, name ='payment'),

    # Menu page displaying all available items
    path('menu/', views.showMenu, name = 'menu'),

    # Home page (landing page)
    path('', views.showHome, name = 'home'),

    # Menu page displaying items filtered by a specific category
    path('menu/<category>/', views.menuByCategory, name = 'menuByCategory'),

    # Add an item to the cart by its ID
    path('addCart/<str:id>/', views.addCart, name='addCart'),

    # Cart page showing all items currently in the user's cart
    path('Cart/', views.display, name= 'Cart'),

    # Checkout page for processing purchases
    path('checkout/', views.checkout, name= 'checkout'),

    # Payments page for handling online payments
    path('payments/', views.payments, name= 'payments'),

    # Add one quantity of an item to the cart by its ID
    path('add/<int:id>/', views.add, name= 'add'),

    # Reduce the quantity of an item in the cart by its ID
    path('reduce/<int:id>/', views.reduce, name='reduce'),

    # Search for an item by name or other criteria
    path('search_item/', views.search_item, name='search_item'),

    # Remove an item from the cart by its ID
    path('delete/<str:id>/', views.delete_from_cart, name='delete_from_cart'),

    # Payment processing for charging a card
    path('charge/', views.charge, name="charge"),

    # Password reset page (using built-in Django view for handling password resets)
    path('reset-password/', auth_views.PasswordResetView.as_view(), name="password_reset"),

    # Page to display user's order history
    path('orders/', views.show_orders, name="orders"),

    # Option for cash on delivery (COD)
    path('cod/', views.cash_on_delivery, name='cash_on_delivery'),
]
