from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Item


class EditItemTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='test-pass-123')
        self.other_user = User.objects.create_user(username='other', password='test-pass-123')
        self.item = Item.objects.create(
            owner=self.owner,
            title='Lost keys',
            description='A set of keys',
            category='Others',
            status='Lost',
            location='Library',
            contact='owner@example.com',
        )

    def test_owner_can_edit_item(self):
        self.client.force_login(self.owner)

        page = self.client.get(reverse('edit_item', args=[self.item.pk]))
        self.assertEqual(page.status_code, 200)
        self.assertContains(page, 'Lost keys')

        response = self.client.post(
            reverse('edit_item', args=[self.item.pk]),
            {
                'title': 'Found keys',
                'description': 'Keys with a blue tag',
                'category': 'Others',
                'status': 'Found',
                'location': 'Cafeteria',
                'contact': 'owner@example.com',
            },
        )

        self.assertRedirects(response, reverse('item_detail', args=[self.item.pk]))
        self.item.refresh_from_db()
        self.assertEqual(self.item.title, 'Found keys')
        self.assertEqual(self.item.description, 'Keys with a blue tag')
        self.assertEqual(self.item.status, 'Found')
        self.assertEqual(self.item.location, 'Cafeteria')

    def test_non_owner_cannot_view_or_submit_edit(self):
        self.client.force_login(self.other_user)
        edit_url = reverse('edit_item', args=[self.item.pk])

        self.assertEqual(self.client.get(edit_url).status_code, 404)
        response = self.client.post(edit_url, {'title': 'Changed'})

        self.assertEqual(response.status_code, 404)
        self.item.refresh_from_db()
        self.assertEqual(self.item.title, 'Lost keys')

    def test_anonymous_user_is_redirected_from_edit_page(self):
        response = self.client.get(reverse('edit_item', args=[self.item.pk]))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('edit_item', args=[self.item.pk])}",
        )

    def test_posted_item_is_assigned_to_signed_in_user(self):
        self.client.force_login(self.owner)

        response = self.client.post(
            reverse('post_items'),
            {
                'title': 'Lost wallet',
                'description': 'Black wallet',
                'category': 'Others',
                'status': 'Lost',
                'location': 'Bus stop',
                'contact': 'owner@example.com',
            },
        )

        self.assertRedirects(response, reverse('home'))
        item = Item.objects.get(title='Lost wallet')
        self.assertEqual(item.owner, self.owner)

    def test_anonymous_user_cannot_create_unowned_item(self):
        response = self.client.post(
            reverse('post_items'),
            {
                'title': 'Lost wallet',
                'description': 'Black wallet',
                'category': 'Others',
                'status': 'Lost',
                'location': 'Bus stop',
                'contact': 'owner@example.com',
            },
        )

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('post_items')}",
        )
        self.assertFalse(Item.objects.filter(title='Lost wallet').exists())
