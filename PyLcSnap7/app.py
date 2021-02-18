from PyLcSnap7.DataTypes import *
from snap7.util import DB
from snap7.util import *
from snap7.snap7types import S7AreaDB
from PyLcSnap7.PLC import S7
import math

x = S7("127.0.0.1")
x.connect()

c = x.SmartTags.BoolArray(1, 1046, 100)
ae = x.SmartTags.StringArray(1, 1990, 100)



print("STOP")
