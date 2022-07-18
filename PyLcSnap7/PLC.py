import json
import logging

import zmq
from snap7.client import Client
from snap7.exceptions import Snap7Exception
from snap7.types import Areas, cpu_statuses, PingTimeout, SendTimeout, RecvTimeout

from PyLcSnap7 import Util
from PyLcSnap7.Smarttags import SmartTags

for name, logger in logging.root.manager.loggerDict.items():
    logger.disabled = True


class PLC:
    def __init__(self, ip='127.0.0.1', name='Default Plc', lib_location='./PyLcSnap7/bin/fixsnap764.dll'):
        self.ip = ip
        self.lib_location = lib_location
        self.name = name
        self._params = (
            (PingTimeout, 50),  # Default 750
            (SendTimeout, 20),  # Default 10
            (RecvTimeout, 100)  # Default 3000
        )
        self.read_client = Client(lib_location=self.lib_location)
        self.write_client = Client(lib_location=self.lib_location)
        self._set_params()
        self.SmartTags = SmartTags(self)

    def __repr__(self):
        return f"{self.name} @ {self.ip}"

    def __str__(self):
        return f"{self.name} @ {self.ip}"

    def _set_params(self):
        for param, value in self._params:
            self.read_client.set_param(param, value)
            self.write_client.set_param(param, value)

    def connect(self):
        if self.read_client.get_connected() and self.write_client.get_connected():
            return True
        try:
            if not self.read_client.get_connected():
                self.read_client.connect(self.ip, 0, 0)

            if not self.write_client.get_connected():
                self.write_client.connect(self.ip, 0, 0)
        except Snap7Exception as e:
            return False

        return self.read_client.get_connected() and self.write_client.get_connected()

    def cpu_in_run(self):
        return self.read_client.get_cpu_state() == cpu_statuses.get(8)

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
                # todo fix rekursionserror..
                return self.read(db, start, length)
            elif 'ISO : An error occurred during recv TCP : Connection timed out' in str(e):
                self.connect()
                return self.read(db, start, length)
            else:
                raise e

    def write(self, db, start, data):
        try:
            return self.read_client.write_area(Areas.DB, db, start, data)
        except  Exception as e:
            if 'CLI : Job pending' in str(e):
                # todo fix rekursionserror..
                return self.write(db, start, data)
            elif 'ISO : An error occurred during recv TCP : Connection timed out' in str(e):
                self.connect()
                return self.write(db, start, data)
            else:
                raise e


class PLCServer:
    def __init__(self, ip="0.0.0.0", port=5555):
        self.port = port
        self._plc = PLC('192.168.30.1')
        self._plc.connect()
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REP)

    def start(self):
        self._socket.bind(f"tcp://*:{self.port}")
        self.run()

    def run(self):
        while True:
            msg = None
            try:
                msg = self._socket.recv().decode('utf-8')
            except zmq.Again:
                continue

            if msg is not None:
                req = json.loads(msg)
                response = b''

                if req.get('cmd') == 'read':
                    response = self._plc.read(req.get('db'), req.get('start'), req.get('length'))

                elif req.get('cmd') == 'write':
                    self._plc.write(req.get('db'), req.get('start'), bytearray.fromhex(req.get('data')))
                    response = msg.encode('utf-8')

                elif req.get('cmd') == 'cpu_run':
                    response = str(self._plc.cpu_in_run()).encode('utf-8')

                self._socket.send(response)


class PLCClient:
    def __init__(self, ip="127.0.0.1", port=5555):
        self.ip = ip
        self.port = port
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REQ)
        self.SmartTags = SmartTags(self)

    def connect(self):
        self._socket.connect(f"tcp://{self.ip}:{self.port}")

    def transfer(self, request):
        self._socket.send(json.dumps(request).encode('utf-8'))
        return self._socket.recv()

    def cpu_in_run(self):
        req = {
            'cmd': 'cpu_run'
        }
        resonse = self.transfer(req)
        return Util.str2bool(resonse.decode('utf-8'))

    def read(self, db, start, length):
        req = {
            'cmd'   : 'read',
            'db'    : db,
            'start' : start,
            'length': length
        }
        resonse = self.transfer(req)
        return bytearray(resonse)

    def write(self, db, start, data):
        req = {
            'cmd'  : 'write',
            'db'   : db,
            'start': start,
            'data' : data.hex()
        }
        resonse = self.transfer(req)
        return resonse
