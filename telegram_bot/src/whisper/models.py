import enum
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

__all__ = (
    'User',
    'Contact',
    'SecretMessage',
    'Draft',
    'SecretMedia',
    'SecretMediaType',
)


class User(BaseModel):
    id: int
    fullname: str
    username: str | None
    is_premium: bool
    can_be_added_to_contacts: bool


class Contact(BaseModel):
    id: int
    private_name: str
    public_name: str
    created_at: datetime
    is_hidden: bool
    of_user: User
    to_user: User


@dataclass(frozen=True, slots=True)
class Draft:
    id: UUID
    text: str


class SecretMessage(BaseModel):
    id: UUID
    text: str


class SecretMediaType(enum.Enum):
    PHOTO = 1
    VOICE = 2
    VIDEO = 3
    AUDIO = 4
    ANIMATION = 5
    DOCUMENT = 6
    VIDEO_NOTE = 7
    STICKER = 8


class SecretMedia(BaseModel):
    id: UUID
    file_id: str
    name: str | None
    media_type: SecretMediaType
    contact: Contact