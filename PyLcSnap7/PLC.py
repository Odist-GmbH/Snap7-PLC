import snap7
import math
import struct
import numpy
import datetime
from PyLcSnap7.Smarttags import SmartTags


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
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 1)
            return snap7.util.get_bool(reading, 0, offset)
        else:
            return self.readBool(db, start, offset)

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

    def writeBool(self, db, start, offset, value):
        if self.connect():
            reading = self.client.db_read(db, start, 1)
            snap7.util.set_bool(reading, 0, offset, value)
            self.client.db_write(db, start, reading)
        else:
            return self.writeBool(db, start, offset, value)

    def readByte(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 1)
            return int().from_bytes(reading, 'big')
        else:
            return self.readByte(db, start)

    def writeByte(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(1, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeByte(db, start, value)

    def readWord(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 2)
            return int().from_bytes(reading, 'big')
        else:
            return self.readWord(db, start)

    def writeWord(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(2, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeWord(db, start, value)

    def readDWord(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 4)
            return int().from_bytes(reading, 'big')
        else:
            return self.readDWord(db, start)

    def writeDWord(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(4, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeDWord(db, start, value)

    def readLWord(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 8)
            return int().from_bytes(reading, 'big')
        else:
            return self.readLWord(db, start)

    def writeLWord(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(8, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeLWord(db, start, value)

    def readSInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 1)
            return int().from_bytes(reading, 'big', signed=True)
        else:
            return self.readSInt(db, start)

    def writeSInt(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(1, byteorder='big', signed=True)
            self.client.db_write(db, start, reading)
        else:
            return self.writeSInt(db, start, value)

    def readInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 2)
            return snap7.util.get_int(reading, 0)
        else:
            return self.readInt(db, start)

    def writeInt(self, db, start, value):
        if self.connect():
            reading = self.client.db_read(db, start, 2)
            snap7.util.set_int(reading, 0, value)
            self.client.db_write(db, start, reading)
        else:
            return self.writeInt(db, start, value)

    def readDInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 4)
            return int().from_bytes(reading, 'big', signed=True)
        else:
            return self.readDInt(db, start)

    def writeDInt(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(4, byteorder='big', signed=True)
            self.client.db_write(db, start, reading)
        else:
            return self.writeDInt(db, start, value)

    def readUSInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 1)
            return int().from_bytes(reading, 'big')
        else:
            return self.readUSInt(db, start)

    def writeUSInt(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(1, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeUSInt(db, start, value)

    def readUInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 2)
            return int().from_bytes(reading, 'big')
        else:
            return self.readUInt(db, start)

    def writeUInt(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(2, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeUInt(db, start, value)

    def readUDInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 4)
            return int().from_bytes(reading, 'big')
        else:
            return self.readUDInt(db, start)

    def writeUDInt(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(4, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeUDInt(db, start, value)

    def readLInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 8)
            return int().from_bytes(reading, 'big', signed=True)
        else:
            return self.readLInt(db, start)

    def writeLInt(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(8, byteorder='big', signed=True)
            self.client.db_write(db, start, reading)
        else:
            return self.writeLInt(db, start, value)

    def readULInt(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 8)
            return int().from_bytes(reading, 'big')
        else:
            return self.readULInt(db, start)

    def writeULInt(self, db, start, value):
        if self.connect():
            reading = int(value).to_bytes(8, byteorder='big')
            self.client.db_write(db, start, reading)
        else:
            return self.writeULInt(db, start, value)

    def readReal(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 4)
            return snap7.util.get_real(reading, 0)
        else:
            return self.readReal(db, start)

    def readRealArray(self, db, start, lenght):
        if self.connect():
            bytelength = 4
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, bytelength * (lenght + 1))
            array = [snap7.util.get_real(reading, i * bytelength) for i in range(0, lenght + 1)]
            return array
        else:
            return self.readRealArray(db, start, lenght)

    def writeReal(self, db, start, value):
        if self.connect():
            reading = self.client.db_read(db, start, 4)
            snap7.util.set_real(reading, 0, value)
            self.client.db_write(db, start, reading)
        else:
            return self.writeReal(db, start, value)

    def writeRealArray(self, db, start, data):
        if self.connect():
            bytelength = 4
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start * bytelength, bytelength * (len(data)))
            for index, d in enumerate(data):
                snap7.util.set_real(reading, index * bytelength, d)
            self.client.db_write(db, start * bytelength, reading)
        else:
            return self.writeRealArray(db, start, data)

    def readLReal(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 8)
            return struct.unpack(">d",reading)
        else:
            return self.readLReal(db, start)

    def writeLReal(self, db, start, value):
        if self.connect():
            reading = struct.pack(">d", value)
            self.client.db_write(db, start, reading)
        else:
            return self.writeLReal(db, start, value)

    def readTime(self, db, start):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 4)
            return numpy.timedelta64(int().from_bytes(reading,'big'), 'ms')
        else:
            return self.readTime(db, start)

    def writeTime(self, db, start, value):
        pass

    def readLTime(self, db, start, getdt=False):
        if self.connect():
            reading = self.client.read_area(snap7.snap7types.S7AreaDB, db, start, 8)
            value = struct.unpack('>q', struct.pack('8B', *reading))[0]
            if getdt:
                td = numpy.timedelta64(value, 'ns')
                return datetime.timedelta(microseconds=td.tolist() / 1e3)
            else:
                return value

        else:
            return self.readLTime(db, start)

    def writeLTime(self, db, start, value):
        pass

    def readChar(self, db, start):
        pass

    def writeChar(self, db, start, value):
        pass

    def readWChar(self, db, start):
        pass

    def writeWChar(self, db, start, value):
        pass

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
    y = x.SmartTags.Bool(100, 0, 0)
    y.read()
    c = x.readWord(100, 10)
    c = x.readLReal(100,252)



    print(2)
