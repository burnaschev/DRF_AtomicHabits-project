from rest_framework import serializers

from habits.models import Habit
from habits.validators import AssociatedHabitAndRewardValidator, AssociatedHabitValidator, DurationValidator, \
    IsPleasurableValidator, DurationPeriodValidator


class HabitSerializers(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}

        validators = [
            AssociatedHabitAndRewardValidator(field1='associated_habit', field2='reward'),
            DurationValidator(field="duration"),
            AssociatedHabitValidator(field="associated_habit"),
            IsPleasurableValidator(field1="associated_habit", field2="is_pleasurable", field3="reward"),
            DurationPeriodValidator(field="period")
        ]
