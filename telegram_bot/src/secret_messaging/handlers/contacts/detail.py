from aiogram import Dispatcher
from aiogram.types import CallbackQuery, ChatType

from common.repositories import HTTPClientFactory
from common.views import edit_message_by_view
from secret_messaging.callback_data import ContactDetailCallbackData
from secret_messaging.repositories import ContactRepository
from secret_messaging.views import ContactDetailView

__all__ = ('register_handlers',)


async def on_show_contact_detail(
        callback_query: CallbackQuery,
        callback_data: dict,
        closing_http_client_factory: HTTPClientFactory,
) -> None:
    contact_id: int = callback_data['contact_id']

    async with closing_http_client_factory() as http_client:
        contact_repository = ContactRepository(http_client)
        contact = await contact_repository.get_by_id(contact_id)

    view = ContactDetailView(contact)
    await edit_message_by_view(
        message=callback_query.message,
        view=view,
    )


def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.register_callback_query_handler(
        on_show_contact_detail,
        ContactDetailCallbackData().filter(),
        chat_type=ChatType.PRIVATE,
        state='*',
    )
