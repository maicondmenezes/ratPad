import pytest
from accounts.models import User

pytestmark = pytest.mark.django_db

def test_create_user():
    user = User.objects.create_user(
        username='user_test', email='user_mail@example.com', password='passW0rd',        
    )

    assert user.username ==  'user_test'
    assert user.email == 'user_mail@example.com'
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superuser():
    user = User.objects.create_superuser(
        username='user_test', email='user_mail@example.com', password='passW0rd',        
    )

    assert user.username ==  'user_test'
    assert user.email == 'user_mail@example.com'
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser