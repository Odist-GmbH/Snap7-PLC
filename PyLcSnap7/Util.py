import datetime
import math
import struct


def get_lword(bytearray_: bytearray, byte_index: int) -> int:
    """ Gets the lword from the buffer.
    """
    data = bytearray_[byte_index:byte_index + 8]
    dword = struct.unpack('>Q', struct.pack('8B', *data))[0]
    return dword


def set_lword(bytearray_: bytearray, byte_index: int, dword: int):
    """Set a LWORD to the buffer.
    """
    dword = int(dword)
    _bytes = struct.unpack('8B', struct.pack('>Q', dword))
    for i, b in enumerate(_bytes):
        bytearray_[byte_index + i] = b


def set_uint(bytearray_: bytearray, byte_index: int, _int: int) -> bytearray:
    """set unsigned  int
    """
    _int = int(_int)
    _bytes = struct.unpack('2B', struct.pack('>H', _int))
    bytearray_[byte_index:byte_index + 2] = _bytes
    return bytearray_


def get_uint(bytearray_: bytearray, byte_index: int) -> int:
    """Get the unsigned int from the bytearray
    """
    data = bytearray_[byte_index:byte_index + 2]
    data[1] = data[1] & 0xff
    data[0] = data[0] & 0xff
    packed = struct.pack('2B', *data)
    value = struct.unpack('>H', packed)[0]
    return value


def set_udint(bytearray_: bytearray, byte_index: int, _int: int):
    """set unsigned double int
    """
    _bytes = struct.unpack('4B', struct.pack('>I', _int))
    for i, b in enumerate(_bytes):
        bytearray_[byte_index + i] = b


def get_udint(bytearray_: bytearray, byte_index: int) -> int:
    """Get the unsigned double int from the bytearray
    """
    data = bytearray_[byte_index:byte_index + 4]
    dword = struct.unpack('>I', struct.pack('4B', *data))[0]
    return dword


def set_lint(bytearray_: bytearray, byte_index: int, _int: int):
    """Set value in bytearray to long int
    """
    # make sure were dealing with an int
    _int = int(_int)
    _bytes = struct.unpack('8B', struct.pack('>q', _int))
    bytearray_[byte_index:byte_index + 8] = _bytes
    return bytearray_


def get_lint(bytearray_: bytearray, byte_index: int) -> int:
    """Get long int value from bytearray.
    """
    data = bytearray_[byte_index:byte_index + 8]
    data[1] = data[1] & 0xff
    data[0] = data[0] & 0xff
    packed = struct.pack('8B', *data)
    value = struct.unpack('>q', packed)[0]
    return value


def set_ulint(bytearray_: bytearray, byte_index: int, _int: int):
    """set unsigned double int
    """
    _bytes = struct.unpack('8B', struct.pack('>Q', _int))
    for i, b in enumerate(_bytes):
        bytearray_[byte_index + i] = b


def get_ulint(bytearray_: bytearray, byte_index: int) -> int:
    """Get the unsigned double int from the bytearray
    """
    data = bytearray_[byte_index:byte_index + 8]
    dword = struct.unpack('>Q', struct.pack('8B', *data))[0]
    return dword


def set_lreal(bytearray_: bytearray, byte_index: int, real) -> bytearray:
    """Set LReal value
    """
    real = float(real)
    real = struct.pack('>d', real)
    _bytes = struct.unpack('8B', real)
    for i, b in enumerate(_bytes):
        bytearray_[byte_index + i] = b
    return bytearray_


def get_lreal(bytearray_: bytearray, byte_index: int) -> float:
    """Get lreal value.
    """
    x = bytearray_[byte_index:byte_index + 8]
    real = struct.unpack('>d', struct.pack('8B', *x))[0]
    return real


def set_wchar(bytearray_: bytearray, byte_index: int, value: str):
    """Set wchar value
    """
    _int = ord(value)
    _bytes = struct.unpack('2B', struct.pack('>H', _int))
    bytearray_[byte_index:byte_index + 2] = _bytes
    return bytearray_


def get_wchar(bytearray_: bytearray, byte_index: int) -> str:
    """Get wchar from bytearray

    """
    data = bytearray_[byte_index:byte_index + 2]
    data[1] = data[1] & 0xff
    data[0] = data[0] & 0xff
    packed = struct.pack('2B', *data)
    value = struct.unpack('>H', packed)[0]
    return chr(value)


def set_date(bytearray_: bytearray, byte_index: int, value: datetime.date):
    _int = int((value - datetime.date(1990, 1, 1)).days)
    _bytes = struct.unpack('2B', struct.pack('>H', _int))
    bytearray_[byte_index:byte_index + 2] = _bytes
    return bytearray_


def get_date(bytearray_: bytearray, byte_index: int) -> datetime.date:
    data = bytearray_[byte_index:byte_index + 2]
    data[1] = data[1] & 0xff
    data[0] = data[0] & 0xff
    packed = struct.pack('2B', *data)
    value = struct.unpack('>H', packed)[0]
    return datetime.date(1990, 1, 1) + datetime.timedelta(days=value)


def set_tod(bytearray_: bytearray, byte_index: int, time: datetime.time):
    _int = (time.hour * 60 * 60 * 1000) + (time.minute * 60 * 1000) + (time.second * 1000) + (
            time.microsecond // 1000)
    _bytes = struct.unpack('4B', struct.pack('>I', _int))
    for i, b in enumerate(_bytes):
        bytearray_[byte_index + i] = b


def get_tod(bytearray_: bytearray, byte_index: int) -> datetime.time:
    data = bytearray_[byte_index:byte_index + 4]
    ms = struct.unpack('>I', struct.pack('4B', *data))[0]
    return (datetime.datetime.min + datetime.timedelta(milliseconds=ms)).time()


def set_ltime(bytearray_: bytearray, byte_index: int, time: datetime.time):
    raise NotImplementedError
    _int = (time.hour * 60 * 60 * 1000) + (time.minute * 60 * 1000) + (time.second * 1000) + (
            time.microsecond // 1000)
    _bytes = struct.unpack('8B', struct.pack('>I', _int))
    for i, b in enumerate(_bytes):
        bytearray_[byte_index + i] = b


def get_ltime(bytearray_: bytearray, byte_index: int) -> datetime.time:
    data = bytearray_[byte_index:byte_index + 8]
    us = struct.unpack('>Q', struct.pack('8B', *data))[0] / 1e3
    return (datetime.datetime.min + datetime.timedelta(microseconds=us)).time()


def set_dtl(bytearray_: bytearray, byte_index: int, time: datetime.time):
    raise NotImplementedError
    _int = (time.hour * 60 * 60 * 1000) + (time.minute * 60 * 1000) + (time.second * 1000) + (
            time.microsecond // 1000)
    _bytes = struct.unpack('8B', struct.pack('>I', _int))
    for i, b in enumerate(_bytes):
        bytearray_[byte_index + i] = b


def get_dtl(bytearray_: bytearray, byte_index: int) -> datetime.datetime:
    data = bytearray_[byte_index:byte_index + 12]

    year = int().from_bytes(data[:2], 'big', signed=False)
    month = int().from_bytes(data[2:3], 'big', signed=False)
    day = int().from_bytes(data[3:4], 'big', signed=False)
    weekday = int().from_bytes(data[4:5], 'big', signed=False)
    hour = int().from_bytes(data[5:6], 'big', signed=False)
    minute = int().from_bytes(data[6:7], 'big', signed=False)
    second = int().from_bytes(data[7:8], 'big', signed=False)
    nanosecond = int().from_bytes(data[8:12], 'big', signed=False)
    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second,
                             microsecond=math.floor(nanosecond / 1e3))
