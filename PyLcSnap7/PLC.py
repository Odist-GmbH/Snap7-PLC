import snap7
import math
from PyLcSnap7.Smarttags import SmartTags

from PyLcSnap7.DataTypes import *


class S7:
    def __init__(self, ip='192.168.0.4', plcname='Default'):
        self.ip = ip
        self.plcname = plcname
        self.port = 102
        self.rack = 0
        self.slot = 0
        self.client = snap7.client.Client()
        self.SmartTags = SmartTags(self)

    def connect(self):
        if self.client.get_connected():
            return True
        else:
            try:
                self.client.connect(self.ip, self.rack, self.slot, self.port)
                return True
            except Exception as e:
                return False

    def readBool(self, db, start, offset):
        return Bool(self.client, db, start, offset).read()

    def writeBool(self, db, start, offset, value):
        return Bool(self.client, db, start, offset).write(value)

    def readByte(self, db, start):
        return Byte(self.client, db, start).read()

    def writeByte(self, db, start, value):
        return Byte(self.client, db, start).write(value)

    def readWord(self, db, start):
        return Word(self.client, db, start).read()

    def writeWord(self, db, start, value):
        return Word(self.client, db, start).write(value)

    def readDWord(self, db, start):
        return DWord(self.client, db, start).read()

    def writeDWord(self, db, start, value):
        return DWord(self.client, db, start).write(value)

    def readLWord(self, db, start):
        return LWord(self.client, db, start).read()

    def writeLWord(self, db, start, value):
        return LWord(self.client, db, start).write(value)

    def readSInt(self, db, start):
        return SInt(self.client, db, start).read()

    def writeSInt(self, db, start, value):
        return SInt(self.client, db, start).write(value)

    def readInt(self, db, start):
        return Int(self.client, db, start).read()

    def writeInt(self, db, start, value):
        return Int(self.client, db, start).write(value)

    def readDInt(self, db, start):
        return DInt(self.client, db, start).read()

    def writeDInt(self, db, start, value):
        return DInt(self.client, db, start).write(value)

    def readUSInt(self, db, start):
        return USInt(self.client, db, start).read()

    def writeUSInt(self, db, start, value):
        return USInt(self.client, db, start).write(value)

    def readUInt(self, db, start):
        return UInt(self.client, db, start).read()

    def writeUInt(self, db, start, value):
        return UInt(self.client, db, start).write(value)

    def readUDInt(self, db, start):
        return UDInt(self.client, db, start).read()

    def writeUDInt(self, db, start, value):
        return UDInt(self.client, db, start).write(value)

    def readLInt(self, db, start):
        return LInt(self.client, db, start).read()

    def writeLInt(self, db, start, value):
        return LInt(self.client, db, start).write(value)

    def readULInt(self, db, start):
        return ULInt(self.client, db, start).read()

    def writeULInt(self, db, start, value):
        return ULInt(self.client, db, start).write(value)

    def readReal(self, db, start):
        return Real(self.client, db, start).read()

    def writeReal(self, db, start, value):
        return Real(self.client, db, start).write(value)

    def readLReal(self, db, start):
        return LReal(self.client, db, start).read()

    def writeLReal(self, db, start, value):
        return LReal(self.client, db, start).write(value)

    def readTime(self, db, start):
        return Time(self.client, db, start).read()

    def writeTime(self, db, start, value):
        return Time(self.client, db, start).write(value)

    def readLTime(self, db, start):
        return LTime(self.client, db, start).read()

    def writeLTime(self, db, start, value):
        return LTime(self.client, db, start).write(value)

    def readChar(self, db, start):
        return Char(self.client, db, start).read()

    def writeChar(self, db, start, value):
        return Char(self.client, db, start).write(value)

    def readWChar(self, db, start):
        return WChar(self.client, db, start).read()

    def writeWChar(self, db, start, value):
        return WChar(self.client, db, start).write(value)

    def readString(self, db, start, length=255):
        return String(self.client, db, start, length).read()

    def writeString(self, db, start, value, length=255):
        return String(self.client, db, start, length).write(value)

    def readWString(self, db, start, length=255):
        return WString(self.client, db, start, length).read()

    def writeWString(self, db, start, value, length=255):
        return WString(self.client, db, start, length).write(value)

    def readDate(self, db, start):
        return Date(self.client, db, start).read()

    def writeDate(self, db, start, value):
        return Date(self.client, db, start).write(value)

    def readTOD(self, db, start):
        return TOD(self.client, db, start).read()

    def writeTOD(self, db, start, value):
        return TOD(self.client, db, start).write(value)

    def readLTOD(self, db, start):
        return LTOD(self.client, db, start).read()

    def writeLTOD(self, db, start, value):
        return LTOD(self.client, db, start).write(value)

    def readDT(self, db, start):
        return DT(self.client, db, start).read()

    def writeDT(self, db, start, value):
        return DT(self.client, db, start).write(value)

    ######

    ######

    def readBoolArray(self, db, start, lenght):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, math.ceil(lenght / 8) + 1)
            data = []
            for b in range(math.ceil(lenght / 8) + 1):
                for x in range(0, 8):
                    data.append(snap7.util.get_bool(reading, b, x))
            return data[:lenght + 1]
        else:
            return self.readRealArray(db, start, lenght)

    def readRealArray(self, db, start, lenght):
        if self.connect():
            bytelength = 4
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, bytelength * (lenght + 1))
            array = [snap7.util.get_real(reading, i * bytelength) for i in range(0, lenght + 1)]
            return array
        else:
            return self.readRealArray(db, start, lenght)

    def writeRealArray(self, db, start, data):
        if self.connect():
            bytelength = 4
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start * bytelength, bytelength * (len(data)))
            for index, d in enumerate(data):
                snap7.util.set_real(reading, index * bytelength, d)
            self.client.db_write(db, start * bytelength, reading)
        else:
            return self.writeRealArray(db, start, data)

    def disconnect(self):
        self.client.disconnect()

    def __repr__(self):
        return f"{self.plcname if self.plcname else 'NoName'}@{self.ip}"


if __name__ == '__main__':
    x = S7('192.168.0.4', 'SandBoxCpu')
    x.connect()

    y = x.readDate(100,3440)
    y = x.readDT(100,3510)

    print(2)
