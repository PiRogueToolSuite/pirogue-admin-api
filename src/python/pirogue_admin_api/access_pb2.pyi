from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MethodAccess(_message.Message):
    __slots__ = ["permission"]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permission: _Optional[_Iterable[str]] = ...) -> None: ...

class PermissionChanges(_message.Message):
    __slots__ = ["adds", "removes", "sets", "user_access_idx"]
    ADDS_FIELD_NUMBER: _ClassVar[int]
    REMOVES_FIELD_NUMBER: _ClassVar[int]
    SETS_FIELD_NUMBER: _ClassVar[int]
    USER_ACCESS_IDX_FIELD_NUMBER: _ClassVar[int]
    adds: ServiceAccess
    removes: ServiceAccess
    sets: ServiceAccess
    user_access_idx: int
    def __init__(self, user_access_idx: _Optional[int] = ..., sets: _Optional[_Union[ServiceAccess, _Mapping]] = ..., adds: _Optional[_Union[ServiceAccess, _Mapping]] = ..., removes: _Optional[_Union[ServiceAccess, _Mapping]] = ...) -> None: ...

class ServiceAccess(_message.Message):
    __slots__ = ["services"]
    class ServicesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MethodAccess
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MethodAccess, _Mapping]] = ...) -> None: ...
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.MessageMap[str, MethodAccess]
    def __init__(self, services: _Optional[_Mapping[str, MethodAccess]] = ...) -> None: ...

class UserAccess(_message.Message):
    __slots__ = ["idx", "permissions", "token"]
    IDX_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    idx: int
    permissions: ServiceAccess
    token: str
    def __init__(self, idx: _Optional[int] = ..., token: _Optional[str] = ..., permissions: _Optional[_Union[ServiceAccess, _Mapping]] = ...) -> None: ...

class UserAccessList(_message.Message):
    __slots__ = ["user_accesses"]
    USER_ACCESSES_FIELD_NUMBER: _ClassVar[int]
    user_accesses: _containers.RepeatedCompositeFieldContainer[UserAccess]
    def __init__(self, user_accesses: _Optional[_Iterable[_Union[UserAccess, _Mapping]]] = ...) -> None: ...
