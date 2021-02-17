from PyLcSnap7.DataTypes import *
from snap7.util import DB
from snap7.util import *
from snap7.snap7types import S7AreaDB
from PyLcSnap7.PLC import S7



x = S7("127.0.0.1")
x.connect()

plc_info = x.client.get_cpu_state()
print(plc_info)


print(x.readBool(1, 770, 0))

DB_layout = {
#   0: [db,  start,     offset,     size,   type (1: string, 2: bool, 3: int]
    1: [1,      0,      0,          255,    1],
    2: [1,      256,    0,          0,      2],
    3: [1,      256,    1,          0,      2],
    4: [1,      256,    2,          0,      2],
    5: [1,      258,    0,          255,    1],
    6: [1,      514,    0,          255,    1],
    7: [1,      770,    0,          0,      2],
    8: [1,      772,    0,          0,      3],
    9: [1,      774,    0,          255,    1]
}

def check_plc_data(DB_layout):

    data_array = x.client.read_area(snap7.snap7types.S7AreaDB, 1, 0, 1000)

    plc_data = []

    for item in DB_layout:
        if DB_layout[item][4] == 1:
            tstring = snap7.util.get_string(data_array, DB_layout[item][1], DB_layout[item][3])
            plc_data.append([f"ID: {item}, "
                             f"Type: STRING, "
                             f"VALUE: {tstring}"])

        elif DB_layout[item][4] == 2:
            tbool = snap7.util.get_bool(data_array, DB_layout[item][1], DB_layout[item][2])
            plc_data.append([f"ID: {item}, "
                             f"Type:   BOOL, "
                             f"VALUE: {tbool}"])

        elif DB_layout[item][4] == 3:
            tint = snap7.util.get_int(data_array, DB_layout[item][1])
            plc_data.append([f"ID: {item}, "
                             f"Type:    INT, "
                             f"VALUE: {tint}"])

    return plc_data


data = check_plc_data(DB_layout)
for item in data:
    print(item)


print("Done")


