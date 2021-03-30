from PyLcSnap7.DataTypes import *


class SmartTagsArray:
    def __init__(self, plc):
        self._plc = plc

    def Bool(self, db, start, length):
        raise NotImplementedError
        return Bool(self._plc, db, start)

    def Byte(self, db, start):
        raise NotImplementedError
        return Byte(self._plc, db, start)

    def Word(self, db, start):
        raise NotImplementedError
        return Word(self._plc, db, start)

    def DWord(self, db, start):
        raise NotImplementedError
        return DWord(self._plc, db, start)

    def LWord(self, db, start):
        raise NotImplementedError
        return LWord(self._plc, db, start)

    def SInt(self, db, start):
        raise NotImplementedError
        return SInt(self._plc, db, start)

    def Int(self, db, start):
        raise NotImplementedError
        return Int(self._plc, db, start)

    def DInt(self, db, start):
        raise NotImplementedError
        return DInt(self._plc, db, start)

    def USInt(self, db, start):
        raise NotImplementedError
        return USInt(self._plc, db, start)

    def UInt(self, db, start):
        raise NotImplementedError
        return UInt(self._plc, db, start)

    def UDInt(self, db, start):
        raise NotImplementedError
        return UDInt(self._plc, db, start)

    def LInt(self, db, start):
        raise NotImplementedError
        return LInt(self._plc, db, start)

    def Real(self, db, start, length):
        return RealArray(self._plc, db, start, length)

    def LReal(self, db, start):
        raise NotImplementedError
        return LReal(self._plc, db, start)

    def Time(self, db, start):
        raise NotImplementedError
        return Time(self._plc, db, start)

    def LTime(self, db, start):
        raise NotImplementedError
        return LTime(self._plc, db, start)

    def Char(self, db, start):
        raise NotImplementedError
        return Char(self._plc, db, start)

    def WChar(self, db, start):
        raise NotImplementedError
        return WChar(self._plc, db, start)

    def String(self, db, start, length=255):
        raise NotImplementedError
        return String(self._plc, db, start, length=length)

    def WString(self, db, start, length=255):
        raise NotImplementedError
        return WString(self._plc, db, start, length=length)

    def Date(self, db, start):
        raise NotImplementedError
        return Date(self._plc, db, start)

    def TOD(self, db, start):
        raise NotImplementedError
        return TOD(self._plc, db, start)

    def LTOD(self, db, start):
        raise NotImplementedError
        return LTOD(self._plc, db, start)

    def DT(self, db, start):
        raise NotImplementedError
        return DT(self._plc, db, start)

    def LDT(self, db, start):
        raise NotImplementedError
        return LDT(self._plc, db, start)

    def DTL(self, db, start):
        raise NotImplementedError
        return DTL(self._plc, db, start)


class SmartTags:
    def __init__(self, plc):
        """
        Wrapper around all Plc Datatypes
        :param plc:
        """
        self._plc = plc
        self.ArrayOf = SmartTagsArray(self._plc)

    def Bool(self, db, start, offset):
        return Bool(self._plc, db, start, offset)

    def Byte(self, db, start):
        return Byte(self._plc, db, start)

    def Word(self, db, start):
        return Word(self._plc, db, start)

    def DWord(self, db, start):
        return DWord(self._plc, db, start)

    def LWord(self, db, start):
        return LWord(self._plc, db, start)

    def SInt(self, db, start):
        return SInt(self._plc, db, start)

    def Int(self, db, start):
        return Int(self._plc, db, start)

    def DInt(self, db, start):
        return DInt(self._plc, db, start)

    def USInt(self, db, start):
        return USInt(self._plc, db, start)

    def UInt(self, db, start):
        return UInt(self._plc, db, start)

    def UDInt(self, db, start):
        return UDInt(self._plc, db, start)

    def LInt(self, db, start):
        return LInt(self._plc, db, start)

    def Real(self, db, start):
        return Real(self._plc, db, start)

    def LReal(self, db, start):
        return LReal(self._plc, db, start)

    def Time(self, db, start):
        return Time(self._plc, db, start)

    def LTime(self, db, start):
        return LTime(self._plc, db, start)

    def Char(self, db, start):
        return Char(self._plc, db, start)

    def WChar(self, db, start):
        return WChar(self._plc, db, start)

    def String(self, db, start, length=255):
        return String(self._plc, db, start, length=length)

    def WString(self, db, start, length=255):
        return WString(self._plc, db, start, length=length)

    def Date(self, db, start):
        return Date(self._plc, db, start)

    def TOD(self, db, start):
        return TOD(self._plc, db, start)

    def LTOD(self, db, start):
        return LTOD(self._plc, db, start)

    def DT(self, db, start):
        return DT(self._plc, db, start)

    def LDT(self, db, start):
        return LDT(self._plc, db, start)

    def DTL(self, db, start):
        return DTL(self._plc, db, start)
