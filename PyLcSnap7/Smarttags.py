from PyLcSnap7.DataTypes import *


class SmartTags:
    def __init__(self, client):
        """
        Wrapper around all Plc Datatypes:
            Bool
            Bool Array
            Byte
            Byte Array
            Word
            Word Array
            Dword
            Dword Array
            Lword
            Lword Array
            Sint
            Sint Array
            Int
            Int Array
            Dint
            Dint Array
            Usint
            Usint Array
            Uint
            Uint Array
            Udint
            Udint Array
            Lint
            Lint Array
            Ulint
            Ulint Array
            Real
            Real Array
            Lreal
            Lreal Array
            Time
            Time Array
            Ltime
            Ltime Array
            Char
            Char Array
            Wchar
            Wchar Array
            String
            String Array
            Wstring
            Wstring Array
            Date
            Date Array
            Tod
            Tod Array
            Ltod
            Ltod Array
            Dt
            Dt Array
            Ldt
            Ldt Array
            Dtl
            Dtl Array
        :param client:
        """
        self._client = client

    def Bool(self, db, start, offset):
        return Bool(self._client, db, start, offset)

    def BoolArray(self, db, start, length):
        return BoolArray(self._client, db, start, length)









