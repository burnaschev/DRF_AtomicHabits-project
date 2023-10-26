from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsUser
from habits.serializers import HabitSerializers


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializers

    def perform_create(self, serializer):
        new_habit = serializer.save(user=self.request.user)
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsUser]


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsUser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsUser]
