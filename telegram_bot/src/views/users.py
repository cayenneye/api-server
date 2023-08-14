from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from models import User
from views import View

__all__ = ('UserSettingsView',)


class UserSettingsView(View):

    def __init__(self, user: User, is_anonymous_messaging_enabled: bool):
        self.__user = user
        self.__is_anonymous_messaging_enabled = is_anonymous_messaging_enabled

    def get_text(self) -> str:
        is_premium_emoji = '✅' if self.__user.is_premium else '❌'
        can_be_added_to_contacts_emoji = (
            '✅' if self.__user.can_be_added_to_contacts else '❌'
        )
        is_anonymous_messaging_enabled_emoji = (
            '✅' if self.__is_anonymous_messaging_enabled else '❌'
        )
        return (
            f'🙎🏿‍♂️ Имя: {self.__user.fullname}\n'
            f'✨ Премиум: {is_premium_emoji}\n'
            '📲 Могут ли пользователи добавлять меня в контакты:'
            f' {can_be_added_to_contacts_emoji}\n'
            '🔒 Режим анонимных сообщений:'
            f' {is_anonymous_messaging_enabled_emoji}\n'
        )

    def get_reply_markup(self) -> ReplyKeyboardMarkup:
        can_be_added_to_contacts_toggle_button_text = (
            '❌ Запретить добавление в контакты'
            if self.__user.can_be_added_to_contacts
            else '✅ Разрешить добавление в контакты'
        )
        return ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=[
                [
                    KeyboardButton(can_be_added_to_contacts_toggle_button_text),
                ],
                [
                    KeyboardButton('🖼️ Отправить секретное медиа'),
                ],
                [
                    KeyboardButton('🎨 Тема'),
                    KeyboardButton('👥 Мои контакты'),
                ],
            ],
        )