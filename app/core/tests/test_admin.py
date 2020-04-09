from django.test import TestCase, Client

from django.contrib.auth import get_user_model
# from django.url import reverse
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        email = "admin@gmail.com"
        email2 = "admin2@gmail.com"
        password = "BlaBla pass"
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            first_name="Ad",
            last_name = "Last n",
            email=email,
            password=password
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            first_name="Ad",
            last_name = "Last n",
            email=email2,
            password=password
        )
    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res,self.user.first_name)
        self.assertContains(res,self.user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change',args={self.user.pk})
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
    def test_user_create_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
