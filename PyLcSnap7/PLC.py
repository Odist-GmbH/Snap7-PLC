from snap7.client import Client
from snap7.snap7exceptions import Snap7Exception
from snap7.snap7types import S7AreaDB
from loguru import logger
from PyLcSnap7.Smarttags import SmartTags


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

    def disconnect(self):
        self.read_client.disconnect()
        self.write_client.disconnect()

    def read(self, db, start, length):
        try:
            return self.read_client.read_area(S7AreaDB, db, start, length)
        except Exception as e:
            if 'CLI : Job pending' in str(e):
                return self.read(db, start, length)
            else:
                raise e

    def write(self, db, start, data):
        try:
            return self.read_client.write_area(S7AreaDB, db, start, data)
        except  Exception as e:
            if 'CLI : Job pending' in str(e):
                return self.write(db, start, data)
            else:
                raise e
