class Real:
    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start

    def read(self):
        return self.client.readReal(self.db, self.start)

    def write(self, value):
        self.client.writeReal(self.db, self.start, value)

    def __repr__(self):
        return f"{self.read()}"

    def __str__(self):
        return f"{self.read()}"

class RealArray:
    def __init__(self, client, db, start, length):
        self.client = client
        self.db = db
        self.start = start
        self.length = length

    def read(self):
        return self.client.readRealArray(self.db, self.start, self.length)

    def write(self, values):
        self.client.writeRealArray(self.db, self.start, values)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start} Length: {self.length}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start} Length: {self.length}"


class Bool:
    def __init__(self, client, db, start, offset):
        self.client = client
        self.db = db
        self.start = start
        self.offset = offset

    def read(self):
        return self.client.readBool(self.db, self.start, self.offset)

    def write(self, value):
        self.client.writeBool(self.db, self.start, self.offset, value)

class BoolArray:
    def __init__(self, client, db, start, length):
        self.client = client
        self.db = db
        self.start = start
        self.length = length

    def read(self):
        return self.client.readBoolArray(self.db, self.start, self.length)

    def write(self, values):
        self.client.writeBoolArray(self.db, self.start, values)

    def __repr__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start} Length: {self.length}"

    def __str__(self):
        return f"PLC: {self.client} DB: {self.db} Start: {self.start} Length: {self.length}"


class Int:
    def __init__(self, client, db, start):
        self.client = client
        self.db = db
        self.start = start

    def read(self):
        return self.client.readInt(self.db, self.start)

    def write(self, value):
        self.client.writeInt(self.db, self.start, value)

class String:
    def __init__(self, client, db, start, length=255):
        self.client = client
        self.db = db
        self.start = start
        self.length = length

    def read(self):
        return self.client.readString(self.db, self.start, self.length)

    def write(self, value):
        self.client.writeString(self.db, self.start, self.length, value)

