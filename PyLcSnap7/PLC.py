import snap7
import math
import struct
import numpy
import datetime
from PyLcSnap7.Smarttags import SmartTags

from PyLcSnap7.DataTypes import *


class S7Conn:
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







    def readChar(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 2)
            return reading.decode('utf-8')
        else:
            return self.readChar(db, start)

    def writeChar(self, db, start, value):
        if self.connect():
            reading = value[:2].encode()
            self.client.write_area(snap7.snap7types.S7AreaDB, db, start, reading)
        else:
            return self.writeChar(db, start, value)

    def readWChar(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 2)
            return reading.decode('utf-16')
        else:
            return self.readWChar(db, start)

    def writeWChar(self, db, start, value):
        if self.connect():
            reading = value[:2].encode()
            self.client.write_area(snap7.snap7types.S7AreaDB, db, start, reading)
        else:
            return self.writeWChar(db, start, value)

    def readString(self, db, start, len=255):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, len)
            return snap7.util.get_string(reading, 0, len)
        else:
            return self.readString(db, start, len)

    def writeString(self, db, start, value):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 255)
            snap7.util.set_string(reading, 0, value, 255)
            self.client.db_write(db, start, reading)
        else:
            return self.writeString(db, start, value)

    def readWString(self, db, start):
        pass

    def writeWString(self, db, start, value):
        pass

    def readDate(self, db, start):
        pass

    def writeDate(self, db, start, value):
        pass

    def readTod(self, db, start):
        pass

    def writeTod(self, db, start, value):
        pass

    def readLTod(self, db, start):
        pass

    def writeLTod(self, db, start, value):
        pass

    def readDT(self, db, start):
        pass

    def writeDT(self, db, start, value):
        pass

    def readLDT(self, db, start):
        pass

    def writeLDT(self, db, start, value):
        pass

    def readDTL(self, db, start):
        pass

    def writeDTL(self, db, start, value):
        pass

    def disconnect(self):
        self.client.disconnect()

    def __repr__(self):
        return f"{self.plcname if self.plcname else 'NoName'}@{self.ip}"


if __name__ == '__main__':
    x = S7Conn('192.168.0.4', 'SandBoxCpu')
    x.connect()
    y = x.readBool(100, 0, 0)
    y = x.readLReal(100,252)
    x.writeLTime(100,312,1001)
    y = x.readLTime(100,312)

    print(2)
