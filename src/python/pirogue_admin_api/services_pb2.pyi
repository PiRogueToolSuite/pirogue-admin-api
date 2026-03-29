from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DashboardConfiguration(_message.Message):
    __slots__ = ["password"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...

class DeviceMonitoring(_message.Message):
    __slots__ = ["auth_header_name", "auth_token", "auth_type", "bulk_size", "enable", "filters", "headers", "mode", "name", "periodic_interval", "periodic_rate", "retry_count", "retry_delay", "timeout", "url", "verify_ssl"]
    class HeadersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AUTH_HEADER_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    BULK_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_RATE_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SSL_FIELD_NUMBER: _ClassVar[int]
    auth_header_name: str
    auth_token: str
    auth_type: str
    bulk_size: int
    enable: bool
    filters: _containers.RepeatedCompositeFieldContainer[DeviceMonitoringFilter]
    headers: _containers.ScalarMap[str, str]
    mode: str
    name: str
    periodic_interval: float
    periodic_rate: int
    retry_count: int
    retry_delay: float
    timeout: float
    url: str
    verify_ssl: bool
    def __init__(self, name: _Optional[str] = ..., enable: bool = ..., url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., filters: _Optional[_Iterable[_Union[DeviceMonitoringFilter, _Mapping]]] = ..., mode: _Optional[str] = ..., bulk_size: _Optional[int] = ..., periodic_interval: _Optional[float] = ..., periodic_rate: _Optional[int] = ..., retry_count: _Optional[int] = ..., retry_delay: _Optional[float] = ..., timeout: _Optional[float] = ..., verify_ssl: bool = ..., auth_type: _Optional[str] = ..., auth_token: _Optional[str] = ..., auth_header_name: _Optional[str] = ...) -> None: ...

class DeviceMonitoringFilter(_message.Message):
    __slots__ = ["attribute", "values"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    attribute: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, attribute: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class DeviceMonitorings(_message.Message):
    __slots__ = ["monitorings"]
    MONITORINGS_FIELD_NUMBER: _ClassVar[int]
    monitorings: _containers.RepeatedCompositeFieldContainer[DeviceMonitoring]
    def __init__(self, monitorings: _Optional[_Iterable[_Union[DeviceMonitoring, _Mapping]]] = ...) -> None: ...

class SuricataRulesSource(_message.Message):
    __slots__ = ["enabled", "license", "name", "parameters", "summary", "system", "url", "vendor"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    license: str
    name: str
    parameters: _containers.ScalarMap[str, str]
    summary: str
    system: bool
    url: str
    vendor: str
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., enabled: bool = ..., system: bool = ..., parameters: _Optional[_Mapping[str, str]] = ..., summary: _Optional[str] = ..., vendor: _Optional[str] = ..., license: _Optional[str] = ...) -> None: ...

class SuricataRulesSources(_message.Message):
    __slots__ = ["sources"]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[SuricataRulesSource]
    def __init__(self, sources: _Optional[_Iterable[_Union[SuricataRulesSource, _Mapping]]] = ...) -> None: ...
