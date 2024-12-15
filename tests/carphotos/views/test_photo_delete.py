from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ConnextoSocial.carphotos.models import CarPhoto

UserModel = get_user_model()


class TestPhotoDelete(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            email='test@test.com',
            password='12admin34',
        )

        self.other_user = UserModel.objects.create_user(
            email='test2@test.com',
            password='12admin34',
        )

        self.photo = CarPhoto.objects.create(
            car_photo="my_photo.png",
            description="Awesome Car Photo",
            location="Test",
            user=self.user,
        )

        self.client.login(
            email='test@test.com',
            password='12admin34',
        )

    def test_photo_delete_from_author_user__expect_in_success(self):
        self.assertTrue(CarPhoto.objects.filter(pk=self.photo.pk).exists())

        response = self.client.post(
            reverse('photo-delete', kwargs={'pk': self.photo.pk})
        )
        self.assertFalse(CarPhoto.objects.filter(pk=self.photo.pk).exists())
        self.assertRedirects(response, reverse('home page'))

    def test_photo_delete__from_non_author_user__expect_photo_to_not_be_deleted(self):
        self.client.login(
            email='test2@test.com',
            password='12admin34',
        )

        response = self.client.post(
            reverse('photo-delete', kwargs={'pk': self.photo.pk})
        )

        self.assertTrue(CarPhoto.objects.filter(pk=self.photo.pk).exists())
        self.assertRedirects(response, reverse('home page'))

    def test_photo_delete__from_anonymous_user__expect_redirect_to_login(self):
        self.client.logout()

        response = self.client.post(
            reverse('photo-delete', kwargs={'pk': self.photo.pk})
        )

        self.assertTrue(CarPhoto.objects.filter(pk=self.photo.pk).exists())
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('photo-delete', kwargs={'pk': self.photo.pk})}")
