from snap7.client import Client
from snap7.exceptions import Snap7Exception
from snap7.types import Areas, WordLen, cpu_statuses, block_types
from PyLcSnap7.Smarttags import SmartTags
from loguru import logger


class PLC:
    def __init__(self, ip='127.0.0.1', name='Default Plc'):
        self.ip = ip
        self.name = name
        self.read_client = Client()
        self.write_client = Client()
        self.SmartTags = SmartTags(self)

    def __repr__(self):
        return f"{self.name} @ {self.ip}"

    def __str__(self):
        return f"{self.name} @ {self.ip}"

    def connect(self):
        if self.read_client.get_connected() and self.write_client.get_connected():
            return True
        try:
            if not self.read_client.get_connected():
                self.read_client.connect(self.ip, 0, 0)

            if not self.write_client.get_connected():
                self.write_client.connect(self.ip, 0, 0)
        except Snap7Exception as e:
            logger.error(str(e))
            return False

        return self.read_client.get_connected() and self.write_client.get_connected()

    def cpu_in_run(self):
        return self.read_client.get_cpu_state() == cpu_statuses[8]

    def cpu_info(self):
        return self.read_client.get_cpu_info()

    def disconnect(self):
        self.read_client.disconnect()
        self.write_client.disconnect()

    def read(self, db, start, length):
        try:
            return self.read_client.read_area(Areas.DB, db, start, length)
        except Exception as e:
            if 'CLI : Job pending' in str(e):
                return self.read(db, start, length)
            else:
                raise e

    def write(self, db, start, data):
        try:
            return self.read_client.write_area(Areas.DB, db, start, data)
        except  Exception as e:
            if 'CLI : Job pending' in str(e):
                return self.write(db, start, data)
            else:
                raise e


if __name__ == '__main__':
    s7 = PLC()
    s7.connect()

    # Bool
    bool = s7.SmartTags.Bool(107, 0, 0)
    bool.toggle()
    # Byte
    byte = s7.SmartTags.Byte(107, 1)
    byte.write(42)
    print(byte.read())
    # Word
    word = s7.SmartTags.Word(107, 372)
    word.write(60000)
    print(word.read())
    # DWord
    dword = s7.SmartTags.DWord(107, 30)
    dword.write(70000)
    print(dword.read())
    # LWord
    lword = s7.SmartTags.LWord(107, 76)
    lword.write(68719476736)
    print(lword.read())
    # SInt
    sint = s7.SmartTags.SInt(107, 88)
    sint.write(127)
    print(sint.read())
    # Int
    int = s7.SmartTags.Int(107, 34)
    int.write(-101)
    print(int.read())
    # DInt
    dint = s7.SmartTags.DInt(107, 6)
    dint.write(-100001)
    print(dint.read())
    # USInt
    usint = s7.SmartTags.USInt(107, 368)
    usint.write(255)
    print(usint.read())
    # UInt
    uint = s7.SmartTags.UInt(107, 358)
    uint.write(65000)
    print(uint.read())
    # UDInt
    udint = s7.SmartTags.UDInt(107, 354)
    udint.write(650000)
    print(udint.read())
    # LInt
    lint = s7.SmartTags.LInt(107, 44)
    lint.write(-10000000000)
    print(lint.read())
    # ULInt
    ulint = s7.SmartTags.ULInt(107, 360)
    ulint.write(1000000000005)
    print(ulint.read())
    # Real
    real = s7.SmartTags.Real(107, 84)
    real.write(3.123)
    print(real.read())
    # LReal
    lreal = s7.SmartTags.LReal(107, 52)
    lreal.write(-13241234123443.1)
    print(lreal.read())
    # Time
    time = s7.SmartTags.Time(107, 346)
    time.write(1*1000)
    print(time.read())
    # LTime
    ltime = s7.SmartTags.LTime(107, 60)
    ltime.write(1*1000*1000)
    print(ltime.read())
    # Char
    char = s7.SmartTags.Char(107, 2)
    char.write('abc')
    print(char.read())
    # WChar
    wchar = s7.SmartTags.WChar(107, 370)
    wchar.write('xya')
    print(wchar.read())
    # String
    string = s7.SmartTags.String(107, 90)
    string.write('test string test')
    print(string.read())

    print(s7)
