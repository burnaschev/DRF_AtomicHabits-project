from django.conf import settings
from django.core.management.base import BaseCommand
from telebot import TeleBot, types

from users.models import User

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подписаться", callback_data="subscribe")
    keyboard.add(url_button)
    bot.send_message(chat_id,
                     "Привет! Этот бот предназначен для напоминания о твоих привычках! Нажми кнопку ниже, чтобы подписаться!",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "subscribe":
        chat_id = call.message.chat.id
        try:
            user = User.objects.get(tg_name=call.message.chat.username)
            user.chat_id = chat_id
            user.save()
            bot.send_message(chat_id, f'Вы успешно подписались!'
                                      f' Добро пожаловать! {user.username}'
                                      f' Что бы отписаться от канала наберите команду /stop')
        except User.DoesNotExist:
            bot.send_message(chat_id, 'Вы не зарегистрированы в приложений "Атомные привычки"!'
                                      'Для начала пройдите регистрацию на сайте "..."')


@bot.message_handler(commands=['stop'])
def unsubscribe(message):
    chat_id = message.chat.id
    try:
        user = User.objects.get(chat_id=chat_id)
        user.chat_id = None
        user.save()
        bot.send_message(chat_id, 'Вы успешно отписались!')
    except User.DoesNotExist:
        bot.send_message(chat_id, 'Вы не были подписаны!')


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
