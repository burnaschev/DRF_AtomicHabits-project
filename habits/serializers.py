from rest_framework import serializers

from habits.models import Habit
from habits.validators import AssociatedHabitAndRewardValidator


class HabitSerializers(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}

        validators = [
            AssociatedHabitAndRewardValidator(field1='associated_habit', field2='reward'),

        ]
