from PyLcSnap7.DataTypes import *

class SmartTags:
    def __init__(self, client):
        """
        Wrapper around all Plc Datatypes
        :param client:
        """
        self._client = client

    def Bool(self, db, start, offset):
        return Bool(self._client.client, db, start, offset)

    def BoolArray(self, db, start, bool_count):
        return BoolArray(self._client.client, db, start, bool_count)

    def Byte(self, db, start):
        return Byte(self._client.client, db, start)

    def Word(self, db, start):
        return Word(self._client.client, db, start)

    def DWord(self, db, start):
        return DWord(self._client.client, db, start)

    def LWord(self, db, start):
        return LWord(self._client.client, db, start)

    def SInt(self, db, start):
        return SInt(self._client.client, db, start)

    def Int(self, db, start):
        return Int(self._client.client, db, start)

    def DInt(self, db, start):
        return DInt(self._client.client, db, start)

    def USInt(self, db, start):
        return USInt(self._client.client, db, start)

    def UInt(self, db, start):
        return UInt(self._client.client, db, start)

    def UDInt(self, db, start):
        return UDInt(self._client.client, db, start)

    def LInt(self, db, start):
        return LInt(self._client.client, db, start)

    def ULInt(self, db, start):
        return ULInt(self._client.client, db, start)

    def Real(self, db, start):
        return Real(self._client.client, db, start)

    def LReal(self, db, start):
        return LReal(self._client.client, db, start)

    def Time(self, db, start):
        return Time(self._client.client, db, start)

    def LTime(self, db, start):
        return LTime(self._client.client, db, start)

    def Char(self, db, start):
        return Char(self._client.client, db, start)

    def WChar(self, db, start):
        return WChar(self._client.client, db, start)

    def String(self, db, start):
        return String(self._client.client, db, start)

    def StringArray(self, db, start, string_count):
        return StringArray(self._client.client, db, start, string_count)

    def WString(self, db, start):
        return WString(self._client.client, db, start)

    def Date(self, db, start):
        return Date(self._client.client, db, start)

    def TOD(self, db, start):
        return TOD(self._client.client, db, start)

    def LTOD(self, db, start):
        return LTOD(self._client.client, db, start)

    def DT(self, db, start):
        return DT(self._client.client, db, start)

    def LDT(self, db, start):
        return LDT(self._client.client, db, start)

    def DTL(self, db, start):
        return DTL(self._client.client, db, start)