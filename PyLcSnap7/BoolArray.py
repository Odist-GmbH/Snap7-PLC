from PyLcSnap7.DataTypes import *
from snap7.util import DB
from snap7.util import *
from snap7.snap7types import S7AreaDB
from PyLcSnap7.PLC import S7


x = S7("127.0.0.1")
x.connect()

plc_info = x.client.get_cpu_state()
print(plc_info)


# print(x.readBool(1, 770, 0))
b = x.SmartTags.Bool(1,1031,1)
d = x.SmartTags.BoolArray(1, 1030, 0, 100)


DB_layout = {
#   0: [db,  start,     offset,     size,
    1: [1,      1030,    0,          10]
}

def get_bool_array(DB_layout):

    data_array = x.client.read_area(snap7.snap7types.S7AreaDB, 1, 0, 1032)

    plc_data = []

    for item in DB_layout:
        offset_count = DB_layout[item][2]
        byte_index = DB_layout[item][1]
        for size in range(DB_layout[item][3]):
            tbool = snap7.util.get_bool(data_array, byte_index, offset_count)
            plc_data.append(tbool)
            # plc_data.append([f"ID: {item}, "
            #                  f"Type:   BOOL, "
            #                  f"VALUE: {tbool}"])
            if offset_count < 7:
                offset_count += 1
            else:
                offset_count = 0
                byte_index += 1

    return plc_data


data = get_bool_array(DB_layout)
print(data)
for item in data:
    print(item)
print("Done")


