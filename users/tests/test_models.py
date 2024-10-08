from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    def test_create_regular_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="regular_user",
            password="password")
        self.assertEqual(user.email, "regular_user")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="admin_user",
            password="password")
        self.assertEqual(admin_user.email, "admin_user")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="admin_user",
                password="password",
                is_superuser=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="admin_user",
                password="password",
                is_staff=False)
        