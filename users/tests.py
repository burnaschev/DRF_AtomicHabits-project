from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        pass


    def test_user_register(self):
        """ Test created user """
        data = {
            "username": "admin",
            "password": "qwerty123qwerty",
            "tg_name": "Artur"
        }

        response = self.client.post(
            reverse('user:user_register'),
            data=data
        )
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)
        self.assertEquals(User.objects.all().count(),
                          1
                          )
