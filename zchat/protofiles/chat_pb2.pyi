from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["id", "name", "email"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class UserCreated(_message.Message):
    __slots__ = ["confirmation", "user"]
    CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    confirmation: str
    user: User
    def __init__(self, confirmation: _Optional[str] = ..., user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class CreateChatRequest(_message.Message):
    __slots__ = ["user1", "user2"]
    USER1_FIELD_NUMBER: _ClassVar[int]
    USER2_FIELD_NUMBER: _ClassVar[int]
    user1: User
    user2: User
    def __init__(self, user1: _Optional[_Union[User, _Mapping]] = ..., user2: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class Chat(_message.Message):
    __slots__ = ["chat_id", "chat_name", "user1", "user2"]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_NAME_FIELD_NUMBER: _ClassVar[int]
    USER1_FIELD_NUMBER: _ClassVar[int]
    USER2_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    chat_name: str
    user1: int
    user2: int
    def __init__(self, chat_id: _Optional[int] = ..., chat_name: _Optional[str] = ..., user1: _Optional[int] = ..., user2: _Optional[int] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["chat_id", "sender_id", "receiver_id", "message_id", "text", "timestamp"]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    sender_id: int
    receiver_id: int
    message_id: int
    text: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, chat_id: _Optional[int] = ..., sender_id: _Optional[int] = ..., receiver_id: _Optional[int] = ..., message_id: _Optional[int] = ..., text: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["message", "error"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    message: str
    error: str
    def __init__(self, message: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
