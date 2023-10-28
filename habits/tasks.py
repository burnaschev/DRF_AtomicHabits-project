from datetime import datetime

from celery import shared_task
from django.conf import settings
from telebot import TeleBot

from habits.models import Habit

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


@shared_task
def send_notifications():
    habits = Habit.objects.all()
    current_time = datetime.now().time()
    current_date = datetime.now().date()

    for habit in habits:
        if habit.time == current_time:
            if habit.user.chat_id:
                days_passed = (current_date - habit.send_time.date()).days
                if days_passed >= habit.period:
                    bot.send_message(chat_id=habit.user.chat_id, text=f'Вам нужно сделать {habit.action} в {habit.place} в {habit.time}')
                    habit.send_time = datetime.now()
                    habit.save()
