from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitPublicListAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitRetrieveAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('public/', HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('view/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_view'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),

]

