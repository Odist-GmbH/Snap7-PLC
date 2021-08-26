import snap7
import Util
import struct
import datetime


# todo Arrays


class PlcVar:
    def __init__(self):
        print(1)


class Bool(PlcVar):
    """
    Breite (Bit): 1 (S7-1500 optimiert 1 Byte)
    Wertebereich: TRUE oder FALSE
    S71500: x
    S71200: x
    """
    _bytelength = 1

    def __init__(self, plc, db, start, offset):
        self.plc = plc
        self.db = db
        self.start = start
        self.offset = offset
        self._bytelength = Bool._bytelength
        super(Bool, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_bool(bytearr, 0, self.offset)

    def set(self, bytearr, value):
        snap7.util.set_bool(bytearr, 0, self.offset, bool(value))

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = False
        reading = self.plc.read(self.db, self.start, self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def toggle(self):
        flipped = not self.read()
        self.write(flipped)
        return flipped

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start} Offset: {self.offset} Value: {self.read()}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start} Offset: {self.offset} Value: {self.read()}"


class Byte(PlcVar):
    """
    Breite (Bit): 8
    Wertebereich: B#16#00 bis B#16#FF
    S71500: x
    S71200: x
    """
    _bytelength = 1

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = Byte._bytelength
        super(Byte, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_byte(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_byte(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class Word(PlcVar):
    """
    Breite (Bit): 16
    Wertebereich: B#16#0000 bis B#16#FFFF
    S71500: x
    S71200: x
    """
    _bytelength = 2

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = Word._bytelength
        super(Word, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_word(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_word(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class DWord(PlcVar):
    """
    Breite (Bit): 32
    Wertebereich: B#16#0000_0000 bis B#16#FFFF_FFFF
    S71500: x
    S71200: x
    """
    _bytelength = 4

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = DWord._bytelength
        super(DWord, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_dword(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_dword(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class LWord(PlcVar):
    """
    Breite (Bit): 64
    Wertebereich: B#16#0000_0000_0000_0000 bis B#16#FFFF_FFFF_FFFF_FFFF
    S71500: x
    S71200:
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = LWord._bytelength
        super(LWord, self).__init__()

    def get(self, bytearr):
        return Util.get_lword(bytearr, 0)

    def set(self, bytearr, value):
        Util.set_lword(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class SInt(PlcVar):
    """
    Breite (Bit): 8
    Wertebereich: -128 bis 127
    S71500: x
    S71200: x
    """
    _bytelength = 1

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = SInt._bytelength
        super(SInt, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_sint(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_sint(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class Int(PlcVar):
    """
    Breite (Bit): 16
    Wertebereich: -32768 bis 37767
    S71500: x
    S71200: x
    """
    _bytelength = 2

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = Int._bytelength
        super(Int, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_int(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_int(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value == None:
            value = True
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class DInt(PlcVar):
    """
    Breite (Bit): 32
    Wertebereich: -2147483648 bis 2147483647
    S71500: x
    S71200: x
    """
    _bytelength = 4

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = DInt._bytelength
        super(DInt, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_dint(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_dint(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class USInt(PlcVar):
    """
    Breite (Bit): 8
    Wertebereich: 0 bis 255
    S71500: x
    S71200: x
    """
    _bytelength = 1

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = USInt._bytelength
        super(USInt, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_usint(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_usint(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class UInt(PlcVar):
    """
    Breite (Bit): 16
    Wertebereich: 0 bis 65535
    S71500: x
    S71200: x
    """
    _bytelength = 2

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = UInt._bytelength
        super(UInt, self).__init__()

    def get(self, bytearr):
        return Util.get_uint(bytearr, 0)

    def set(self, bytearr, value):
        Util.set_uint(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class UDInt(PlcVar):
    """
    Breite (Bit): 32
    Wertebereich: 0 bis 4294967295
    S71500: x
    S71200: x
    """
    _bytelength = 4

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = UDInt._bytelength
        super(UDInt, self).__init__()

    def get(self, bytearr):
        return Util.get_udint(bytearr, 0)

    def set(self, bytearr, value):
        Util.set_udint(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class LInt(PlcVar):
    """
    Breite (Bit): 64
    Wertebereich: -9223372036854775808 bis 9223372036854775807
    S71500: x
    S71200:
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = LInt._bytelength
        super(LInt, self).__init__()

    def get(self, bytearr):
        return Util.get_lint(bytearr, 0)

    def set(self, bytearr, value):
        Util.set_lint(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class ULInt(PlcVar):
    """
    Breite (Bit): 64
    Wertebereich: 0 bis 18446744073709551615
    S71500: x
    S71200:
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = ULInt._bytelength
        super(ULInt, self).__init__()

    def get(self, bytearr):
        return Util.get_ulint(bytearr, 0)

    def set(self, bytearr, value):
        Util.set_ulint(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class Real(PlcVar):
    """
    Breite (Bit): 32
    Wertebereich:   -3.402823e+38 bis -1.175 495e-38
                                    ±0
                    +1.175 495e-38 bis +3.402823e+38
    S71500: x
    S71200: x
    """
    _bytelength = 4

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = Real._bytelength
        super(Real, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_real(bytearr, 0)

    def set(self, bytearr, value):
        snap7.util.set_real(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0.0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class RealArray(PlcVar):
    """
    Breite (Bit): 32 * n
    Wertebereich:   -3.402823e+38 bis -1.175 495e-38
                                    ±0
                    +1.175 495e-38 bis +3.402823e+38
    S71500: x
    S71200: x
    """
    _bytelength = 4

    def __init__(self, plc, db, start, length):
        self.plc = plc
        self.db = db
        self.start = start
        self.length = length
        self._bytelength = Real._bytelength
        super(RealArray, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength * (self.length + 1))
        return [snap7.util.get_real(reading, i) for i in range(0, (self.length + 1) * 4, self._bytelength)]

    def write(self, values):
        if len(values) > self.length:
            raise ValueError('Index out of range')

        reading = self.plc.read(self.db, self.start, self._bytelength * (self.length + 1))
        for e, r in enumerate(values + ([0] * (self.length - len(values)))):
            snap7.util.set_real(reading, e * self._bytelength, r)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class LReal(PlcVar):
    """
    Breite (Bit): 64
    Wertebereich:   -1.7976931348623158e+308 bis -2.2250738585072014e-308
                                            ±0
                    +2.2250738585072014e-308 bis +1.7976931348623158e+308
    S71500: x
    S71200: x
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = LReal._bytelength
        super(LReal, self).__init__()

    def get(self, bytearr):
        Util.get_lreal(bytearr, 0)

    def set(self, bytearr, value):
        Util.set_lreal(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = 0.0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class Time(PlcVar):
    """
    Breite (Bit): 32
    Wertebereich:   T#-24d20h31m23s648ms bis T#+24d20h31m23s647ms
    S71500: x
    S71200: x
    """
    _bytelength = 4

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = Time._bytelength
        super(Time, self).__init__()

    def get(self, reading):
        return snap7.util.get_dint(reading, 0)

    def set(self, reading, value):
        snap7.util.set_dint(reading, 0, value)

    def read(self):
        # 1 unit == 1 ms
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        # 1 unit == 1 ms
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class LTime(PlcVar):
    """
    Breite (Bit): 64
    Wertebereich:   LT#-106751d23h47m16s854ms775us808ns bis LT#+106751d23h47m16s854ms775us807ns
    S71500: x
    S71200:
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = LTime._bytelength
        super(LTime, self).__init__()

    def get(self, reading):
        return Util.get_lint(reading, 0)

    def set(self, reading, value):
        Util.set_lint(reading, 0, value)

    def read(self):
        # 1 unit == 1 ns
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        # 1 unit == 1 ns
        if value is None:
            value = 0
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class Char(PlcVar):
    """
    Breite (Bit): 8
    Wertebereich: ASCII
    S71500: x
    S71200: x
    """
    _bytelength = 1

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = Char._bytelength
        super(Char, self).__init__()

    def get(self, bytearr):
        return bytearr.decode('utf-8')[:1]

    def set(self, bytearr, value):
        bytearr[0] = ord(value[:1].encode())

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = ''
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class WChar(PlcVar):
    """
    Breite (Bit): 16
    Wertebereich: ASCII
    S71500: x
    S71200: x
    """
    _bytelength = 2

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = WChar._bytelength
        super(WChar, self).__init__()

    def get(self, bytearr):
        return Util.get_wchar(bytearr, 0)

    def set(self, bytearr, value):
        Util.set_wchar(bytearr, 0, value)

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = ''
        reading = bytearray(self._bytelength)
        self.set(reading, value[:1])
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class String(PlcVar):
    """
    Breite (Byte): n+2 (current len, max len)
    Wertebereich: 0 bis 254 Zeichen (n)
    S71500: x
    S71200: x
    """

    def __init__(self, plc, db, start, length=255):
        self.plc = plc
        self.db = db
        self.start = start
        self.length = length
        self._bytelength = self.length + 2
        super(String, self).__init__()

    def get(self, bytearr):
        return snap7.util.get_string(bytearr, 0, self.length)

    def set(self, bytearr, value):
        snap7.util.set_string(bytearr, 0, value, self._bytelength)
        bytearr[0] = self.length

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        return self.get(reading)

    def write(self, value):
        if value is None:
            value = ''
        reading = bytearray(self._bytelength)
        self.set(reading, value)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class WString(PlcVar):
    """
    Breite (Word): n+2 (current len, max len)
    Wertebereich: 0 bis 16382 Zeichen (n)
    S71500: x
    S71200: x
    """

    def __init__(self, plc, db, start, length=255):
        raise NotImplementedError
        self.plc = plc
        self.db = db
        self.start = start
        self.length = length
        self._bytelength = (self.length + 2) * 2
        super(WString, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        pre_reading = self.plc.read(self.db, self.start, 4)
        current_size = int().from_bytes(pre_reading[2:4], 'big', signed=False)
        max_size = int().from_bytes(pre_reading[:2], 'big', signed=False)
        reading = self.plc.read(self.db, self.start + 4, current_size * 2)

        return struct.unpack(f">{current_size * 2}s", reading)[0].decode('utf-16')

    def write(self, value):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class Date(PlcVar):
    """
    Breite (Bit): 16
    Wertebereich: D#1990-01-01 bis D#2168-12-31
    S71500: x
    S71200: x
    """
    _bytelength = 2

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = Date._bytelength
        super(Date, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        day_offset = int().from_bytes(reading, 'big', signed=False)
        return datetime.date(1990, 1, 1) + datetime.timedelta(days=day_offset)

    def write(self, date):
        reading = int((date - datetime.date(1990, 1, 1)).days).to_bytes(self._bytelength, 'big', signed=False)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class TOD(PlcVar):
    """
    Breite (Bit): 32
    Wertebereich: TOD#00:00:00.000 bis TOD#23:59:59.999
    S71500: x
    S71200: x
    """
    _bytelength = 4

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = TOD._bytelength
        super(TOD, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        ms = int().from_bytes(reading, 'big', signed=False)
        return (datetime.datetime.min + datetime.timedelta(milliseconds=ms)).time()

    def write(self, time):
        ms = (time.hour * 60 * 60 * 1000) + (time.minute * 60 * 1000) + (time.second * 1000) + (
                time.microsecond // 1000)
        reading = int(ms).to_bytes(self._bytelength, 'big', signed=False)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class LTOD(PlcVar):
    """
    Breite (Bit): 64
    Wertebereich: LTOD#00:00:00.000000000 bis LTOD#23:59:59.999999999
    S71500: x
    S71200:
    todo time obj from ns base
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = LTOD._bytelength
        super(LTOD, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        ns = int().from_bytes(reading, 'big', signed=False)
        return ns

    def write(self, ns):
        reading = int(ns).to_bytes(self._bytelength, 'big', signed=False)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class DT(PlcVar):
    """
    todo DT
    Breite (Bit): 64
    Wertebereich: Min.: DT#1990-01-01-0:0:0 Max.: DT#2089-12-31-23:59:59.999
    S71500: x
    S71200:
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = DT._bytelength
        super(DT, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        ms = int().from_bytes(reading, 'big', signed=False)
        return ms

    def write(self, ns):
        reading = int(ns).to_bytes(self._bytelength, 'big', signed=False)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class LDT(PlcVar):
    """
    todo LDT
    Breite (Bit): 64
    Wertebereich: Min.: DT#1990-01-01-0:0:0 Max.: DT#2089-12-31-23:59:59.999
    S71500: x
    S71200:
    """
    _bytelength = 8

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = LDT._bytelength
        super(LDT, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        ms = int().from_bytes(reading, 'big', signed=False)
        return ms

    def write(self, ns):
        reading = int(ns).to_bytes(self._bytelength, 'big', signed=False)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"


class DTL(PlcVar):
    """
    Breite (Bit): 96
    Wertebereich: Min.: DTL#1970-01-01-00:00:00.0 Max.: DTL#2554-12-31-23:59:59.999999999
    S71500: x
    S71200: x
    """
    _bytelength = 12

    def __init__(self, plc, db, start):
        self.plc = plc
        self.db = db
        self.start = start
        self._bytelength = DTL._bytelength
        super(DTL, self).__init__()

    def get(self):
        pass

    def set(self):
        pass

    def read(self):
        reading = self.plc.read(self.db, self.start, self._bytelength)
        year = int().from_bytes(reading[:2], 'big', signed=False)
        month = int().from_bytes(reading[2:3], 'big', signed=False)
        day = int().from_bytes(reading[3:4], 'big', signed=False)
        weekday = int().from_bytes(reading[4:5], 'big', signed=False)
        hour = int().from_bytes(reading[5:6], 'big', signed=False)
        minute = int().from_bytes(reading[6:7], 'big', signed=False)
        second = int().from_bytes(reading[7:8], 'big', signed=False)
        nanosecond = int().from_bytes(reading[8:12], 'big', signed=False)
        return (year, month, day, weekday, hour, minute, second, nanosecond)

    def write(self, year, month, day, weekday, hour, minute, second, nanosecond):
        reading = int(year).to_bytes(2, 'big', signed=False)
        reading += int(month).to_bytes(1, 'big', signed=False)
        reading += int(day).to_bytes(1, 'big', signed=False)
        reading += int(weekday).to_bytes(1, 'big', signed=False)
        reading += int(hour).to_bytes(1, 'big', signed=False)
        reading += int(minute).to_bytes(1, 'big', signed=False)
        reading += int(second).to_bytes(1, 'big', signed=False)
        reading += int(nanosecond).to_bytes(4, 'big', signed=False)
        self.plc.write(self.db, self.start, reading)

    def __repr__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"

    def __str__(self):
        return f"PLC: {self.plc} DB: {self.db} Start: {self.start}"
