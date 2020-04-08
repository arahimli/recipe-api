from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """ Test create user with email successfull """
        email = "ataxanr1@gmail.com"
        password = "BlaBla pass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_normailized(self):
        """ Test create user with email successfull """
        email = "ataxannr@gmail.com"
        password = "BlaBla pass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))


    def test_create_super_user(self):
        """ Test create user with email successfull """
        email = "ataxannr@gmail.com"
        password = "BlaBla pass"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
