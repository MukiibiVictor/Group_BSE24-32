import pytest
from django.contrib.auth.models import User
from cakestore.forms import RegisterUserForm  

@pytest.mark.django_db  # This tells pytest that this test interacts with the database
def test_register_form_valid_data():
    form_data = {
        'username': 'testuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'password1': 'Testpassword123',
        'password2': 'Testpassword123'
    }
    form = RegisterUserForm(data=form_data)
    
    assert form.is_valid()  # Assert that the form is valid
    
    user = form.save()
    assert User.objects.count() == 1  # Ensure a user is created
    assert user.username == 'testuser'
    assert user.email == 'john@example.com'


@pytest.mark.django_db
def test_register_form_missing_fields():
    form_data = {
        'username': '',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'password1': 'Testpassword123',
        'password2': 'Testpassword123'
    }
    form = RegisterUserForm(data=form_data)
    
    assert not form.is_valid()  # Assert that the form is invalid
    assert 'username' in form.errors  # Check that the error is in the username field


@pytest.mark.django_db
def test_register_form_invalid_email():
    form_data = {
        'username': 'testuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'invalid-email',
        'password1': 'Testpassword123',
        'password2': 'Testpassword123'
    }
    form = RegisterUserForm(data=form_data)
    
    assert not form.is_valid()  # Assert that the form is invalid
    assert 'email' in form.errors  # Check that the error is in the email field


@pytest.mark.django_db
def test_register_form_password_mismatch():
    form_data = {
        'username': 'testuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'password1': 'Testpassword123',
        'password2': 'DifferentPassword'
    }
    form = RegisterUserForm(data=form_data)
    
    assert not form.is_valid()  # Assert that the form is invalid
    assert 'password2' in form.errors  # Check that the error is in the password confirmation field


@pytest.mark.django_db
def test_register_form_empty_email():
    form_data = {
        'username': 'testuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': '',
        'password1': 'Testpassword123',
        'password2': 'Testpassword123'
    }
    form = RegisterUserForm(data=form_data)
    
    assert not form.is_valid()  # Assert that the form is invalid
    assert 'email' in form.errors  # Check that the error is in the email field



