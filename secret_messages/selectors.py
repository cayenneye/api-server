from uuid import UUID

from django.db.models import QuerySet

from secret_messages.exceptions import (
    SecretMessageDoesNotExistError,
    ThemeDoesNotExistError
)
from secret_messages.models.secret_medias import SecretMedia
from secret_messages.models.secret_message_themes import SecretMessageTheme
from secret_messages.models.secret_messages import SecretMessage

__all__ = (
    'get_secret_message_by_id',
    'get_secret_media_by_id',
    'get_visible_themes',
    'get_theme_by_id',
)


def get_secret_message_by_id(secret_message_id: UUID) -> SecretMessage:
    """Get secret message by ID.

    Args:
        secret_message_id: ID of the secret message.

    Returns:
        SecretMessage object.

    Raises:
        SecretMessageDoesNotExistError: If secret message with the given ID
    """
    try:
        return SecretMessage.objects.get(id=secret_message_id)
    except SecretMessage.DoesNotExist:
        raise SecretMessageDoesNotExistError(
            secret_message_id=secret_message_id,
        )


def get_secret_media_by_id(secret_media_id: UUID) -> SecretMedia:
    """Get secret media by id.

    Args:
        secret_media_id: ID of SecretMedia object.

    Returns:
        SecretMedia object.

    Raises:
        SecretMessageDoesNotExistError: If SecretMedia object does not exist.
    """
    try:
        return (
            SecretMedia.objects
            .select_related('contact', 'contact__of_user',
                            'contact__to_user')
            .get(id=secret_media_id)
        )
    except SecretMedia.DoesNotExist:
        raise SecretMessageDoesNotExistError(
            secret_message_id=secret_media_id,
        )


def get_visible_themes(
        *,
        limit: int,
        offset: int,
) -> QuerySet[SecretMessageTheme]:
    return (
        SecretMessageTheme
        .objects
        .exclude(is_hidden=True)
        .order_by('id')[offset:offset + limit]
    )


def get_theme_by_id(theme_id: int) -> SecretMessageTheme:
    """Retrieve theme by ID.

    Args:
        theme_id: ID of SecretMessageTheme object.

    Returns:
        SecretMessageTheme object.

    Raises:
        ThemeDoesNotExistError: If SecretMessageTheme object does not exist.
    """
    try:
        return SecretMessageTheme.objects.get(id=theme_id)
    except SecretMessageTheme.DoesNotExist:
        raise ThemeDoesNotExistError
