from rest_framework.serializers import ValidationError


class AssociatedHabitAndRewardValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        associated_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if associated_habit and reward:
            raise ValidationError(f"Нельзя одновременно выбирать {self.field1} и {self.field2}")


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)

        if duration > 120:
            raise ValidationError(f"Время выполнения должно быть не больше 120 секунд")


class AssociatedHabitValidator:
    def __init__(self, field):
        self.field1 = field

    def __call__(self, value):
        associated_habit = dict(value).get(self.field)

        if not associated_habit.is_pleasurable:
            raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")


class IsPleasurableValidator:
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        associated_habit = dict(value).get(self.field1)
        is_pleasurable = dict(value).get(self.field2)
        reward = dict(value).get(self.field3)

        if is_pleasurable and (reward or associated_habit):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")


class DurationPeriodValidator:
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, value):
        period = dict(value).get(self.field1)

        if period > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
