from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="test",
            password="2486",
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place="Спортзал",
            time="13:45:30",
            action="Жим лёжа",
            reward="Красаучик",
            user=self.user,
        )

    def test_get_list(self):
        """ Test for getting list fo habit """

        response = self.client.get(
            reverse('habits:habit_list')
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        response = self.client.get(
            reverse('habits:habit_list')
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.habit.id,
                        "place": self.habit.place,
                        "time": self.habit.time,
                        "action": self.habit.action,
                        "is_pleasurable": self.habit.is_pleasurable,
                        "period": self.habit.period,
                        "reward": self.habit.reward,
                        "duration": self.habit.duration,
                        "is_public": self.habit.is_public,
                        "send_time": str(self.habit.send_time),
                        "user": self.habit.user_id,
                        "associated_habit": self.habit.associated_habit
                    }
                ]
            }
        )

    def test_get_public_list(self):
        """ Test for getting list fo public habit """

        response = self.client.get(
            reverse('habits:habit_public_list')
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.habit.id,
                        "place": self.habit.place,
                        "time": self.habit.time,
                        "action": self.habit.action,
                        "is_pleasurable": self.habit.is_pleasurable,
                        "period": self.habit.period,
                        "reward": self.habit.reward,
                        "duration": self.habit.duration,
                        "is_public": self.habit.is_public,
                        "send_time": str(self.habit.send_time),
                        "user": self.habit.user_id,
                        "associated_habit": self.habit.associated_habit
                    }
                ]
            }
        )

    def test_habit_create(self):
        """ Test created habit """
        data = {
            "place": "Улица",
            "time": "19:45:30",
            "action": "Бег",
            "reward": "Мороженное",
            "is_public": True,
            "send_time": "12:38:00",
            "user": self.habit.user_id,
        }

        response = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED)

        self.assertEquals(Habit.objects.all().count(),
                          2
                          )

    def test_duration_validator_create(self):
        """ Test duration_validator create """
        data = {
            "place": "Улица",
            "time": "19:45:30",
            "action": "Бег",
            "reward": "Мороженное",
            "duration": 122,
        }

        response = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )
        print(response.json())
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST
                          )

    def test_update_habit(self):
        """ Test update habit """
        data = {
            "place": "Улица",
            "time": "19:45:30",
            "action": "Бег",
            "reward": "Мороженное",
            "is_public": True,
            "send_time": "12:38:00",
            "user": self.habit.user_id,
        }

        response = self.client.put(
            reverse('habits:habit_update', args=[self.habit.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        """ Test delete habit """

        response = self.client.delete(reverse('habits:habit_delete', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
