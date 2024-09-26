from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for user registration
from django.contrib.auth.models import User  # Import the User model
from django import forms  # Import forms module for creating forms

class RegisterUserForm(UserCreationForm):
    # Define an email field with specific widget attributes
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    # Define first name field with max length and widget attributes
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # Define last name field with max length and widget attributes
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Specify the User model as the model for this form
        # Specify which fields from the User model to include in the form
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method to initialize the form
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        # Add a CSS class to the username field for styling
        self.fields['username'].widget.attrs['class'] = 'form-control'
        
        # Add a CSS class to the password1 field for styling
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        
        # Add a CSS class to the password2 field for styling
        self.fields['password2'].widget.attrs['class'] = 'form-control'
