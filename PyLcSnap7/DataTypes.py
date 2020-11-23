import snap7
import struct


# todo Arrays

class Bool:
    """
    Breite (Bit): 1 (S7-1500 optimiert 1 Byte)
    Wertebereich: TRUE oder FALSE
    S71500: x
    S71200: x
    """

    def __init__(self, client: snap7.client.Client, db, start, offset):
        self.client = client
        self.db = db
        self.start = start
        self.offset = offset
        self._bytelength = 1

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return snap7.util.get_bool(reading, 0, self.offset)

    def write(self, value):
        reading = self.client.db_read(self.db, self.start, self._bytelength)
        snap7.util.set_bool(reading, 0, self.offset, value)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start} Offset: {self.offset}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start} Offset: {self.offset}"


class Byte:
    """
    Breite (Bit): 8
    Wertebereich: B#16#00 bis B#16#FF
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 1

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class Word:
    """
    Breite (Bit): 16
    Wertebereich: B#16#0000 bis B#16#FFFF
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 2

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class DWord:
    """
    Breite (Bit): 32
    Wertebereich: B#16#0000_0000 bis B#16#FFFF_FFFF
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 4

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class LWord:
    """
    Breite (Bit): 64
    Wertebereich: B#16#0000_0000_0000_0000 bis B#16#FFFF_FFFF_FFFF_FFFF
    S71500: x
    S71200:
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 8

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class SInt:
    """
    Breite (Bit): 8
    Wertebereich: -128 bis 127
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 1

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=True)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=True)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class Int:
    """
    Breite (Bit): 16
    Wertebereich: -32768 bis 37767
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 2

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=True)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=True)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class DInt:
    """
    Breite (Bit): 32
    Wertebereich: -2147483648 bis 2147483647
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 4

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=True)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=True)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class USInt:
    """
    Breite (Bit): 8
    Wertebereich: 0 bis 255
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 1

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class UInt:
    """
    Breite (Bit): 16
    Wertebereich: 0 bis 65535
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 2

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class UDInt:
    """
    Breite (Bit): 32
    Wertebereich: 0 bis 4294967295
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 4

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class LInt:
    """
    Breite (Bit): 64
    Wertebereich: -9223372036854775808 bis 9223372036854775807
    S71500: x
    S71200:
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 8

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=True)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=True)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class ULInt:
    """
    Breite (Bit): 64
    Wertebereich: 0 bis 18446744073709551615
    S71500: x
    S71200:
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 8

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=True)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=True)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class Real:
    """
    Breite (Bit): 32
    Wertebereich:   -3.402823e+38 bis -1.175 495e-38
                                    ±0
                    +1.175 495e-38 bis +3.402823e+38
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 4

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return snap7.util.get_real(reading, 0)

    def write(self, value):
        reading = self.client.db_read(self.db, self.start, self._bytelength)
        snap7.util.set_real(reading, 0, value)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class LReal:
    """
    Breite (Bit): 64
    Wertebereich:   -1.7976931348623158e+308 bis -2.2250738585072014e-308
                                            ±0
                    +2.2250738585072014e-308 bis +1.7976931348623158e+308
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 8

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return struct.unpack(">d", reading)[0]

    def write(self, value):
        reading = struct.pack(">d", value)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class Time:
    """
    Breite (Bit): 32
    Wertebereich:   T#-24d20h31m23s648ms bis T#+24d20h31m23s647ms
    S71500: x
    S71200: x
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 4

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return int().from_bytes(reading, 'big', signed=False)

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"


class LTime:
    """
    Breite (Bit): 64
    Wertebereich:   LT#-106751d23h47m16s854ms775us808ns bis LT#+106751d23h47m16s854ms775us807ns
    S71500: x
    S71200:
    """

    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start
        self._bytelength = 8

    def read(self):
        reading = self.client.read_area(snap7.snap7types.S7AreaDB, self.db, self.start, self._bytelength)
        return struct.unpack('>q', struct.pack('8B', *reading))[0]

    def write(self, value):
        reading = int(value).to_bytes(self._bytelength, 'big', signed=False)
        self.client.db_write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start}"