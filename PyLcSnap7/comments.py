

plc_info = x.client.get_cpu_state()
print(plc_info)
# string1 = snap7.util.get_string(data_array, DB_layout[1][2], DB_layout[1][3])

# data_array = x.client.read_area(snap7.snap7types.S7AreaDB, 1, 0, 500)
# string1 = snap7.util.get_string(data_array, 0, 255)
#
# bool2 = snap7.util.get_bool(data_array, 256, 1)
# bool3 = snap7.util.get_bool(data_array, 256, 2)
# string2 = snap7.util.get_string(data_array, 257, 255)


# print(data_array)
# print(string1)
# print(bool1)
# print(bool2)
# print(bool3)
# print(string2)

# DB_layout = {
#     1: (1, 1, 255),
# #    2: (1, 256, 512),
# #    3: (1, 256, 1),
# #    4: (1, 258, 255)
# }
#
# for count in range(1, len(DB_layout)+1):
#
#     data = x.client.db_read(DB_layout[count][0], DB_layout[count][1], DB_layout[count][2])
#     fstring = data[DB_layout[count][1]:(DB_layout[count][2])].decode('UTF-8').strip('\x00')
#     print(fstring)
#
# #for count in range(len(DB_layout)):
# #    data = x.client.db_read(DB_layout[count][0],DB_layout[count][1],DB_layout[count][2])
# #    fstring = data[DB_layout[count][1]:DB_layout[count][2]].decode('UTF-8').strip('\x00')



#b = x.SmartTags.Bool(1,1031,1)
# c = x.SmartTags.BoolArray(1, 1046, 100)
#d = x.SmartTags.Byte(1, 777)
#e = x.SmartTags.Word(1, 777)
#f = x.SmartTags.DWord(1, 774)
#g = x.SmartTags.LWord(1, 774)
#h = x.SmartTags.SInt(1, 773) #liest 772 aus cpu aus (weil 0) -> +1 in DataTypes?
#i = x.SmartTags.Int(1, 772)
#j = x.SmartTags.DInt(1, 774)
#k = x.SmartTags.USInt(1, 773) #liest 772 aus cpu aus (weil 0) -> +1 in DataTypes?
#l = x.SmartTags.UInt(1, 772)
#m = x.SmartTags.UDInt(1, 773)
#n = x.SmartTags.LInt(1, 772)
#o = x.SmartTags.ULInt(1, 1672)
#p = x.SmartTags.Real(1, 1682)
#q = x.SmartTags.LReal(1, 1682)
#r = x.SmartTags.Time(1, 1684)
#s = x.SmartTags.Char(1, 1688)
# t = x.SmartTags.WChar(1, 1690)
#u = x.SmartTags.String(1,1692)
#v = x.SmartTags.String(1,1692)
#w = x.SmartTags.Date(1, 1948)
#a = x.SmartTags.TOD(1, 1950)
#aa = x.SmartTags.LTOD(1, 1954)
#ab = x.SmartTags.DT(1, 1962)
# ac = x.SmartTags.LDT(1, 1970)
# ad = x.SmartTags.DTL(1, 1978)
# ae = x.SmartTags.StringArray(1, 1990, 10)
#
# #print(int(-2).to_bytes(8, byteorder="big", signed=True))
#
#
# # "e = x.SmartTags.Word(1, 777)\n"
# # "returns 2 bytes -> e.g. K R -> in hex -> 4b 52 -> binary -> K(0100 1011) R(0101 0010) -> int -> 19282\n"
# #print(int(-33205429).to_bytes(4, byteorder="big", signed=True))
#
# print("STOP")
#
#
# DB_layout = {
# #   0: [db,  start,     offset,     size,
#     1: [1,      1030,    0,          10]
# }
#
# def get_bool_array(DB_layout):
#
#     data_array = x.client.read_area(snap7.snap7types.S7AreaDB, 1, 0, 1032)
#
#     plc_data = []
#
#     for item in DB_layout:
#         offset_count = DB_layout[item][2]
#         byte_index = DB_layout[item][1]
#         for size in range(DB_layout[item][3]):
#             tbool = snap7.util.get_bool(data_array, byte_index, offset_count)
#             plc_data.append(tbool)
#             # plc_data.append([f"ID: {item}, "
#             #                  f"Type:   BOOL, "
#             #                  f"VALUE: {tbool}"])
#             if offset_count < 7:
#                 offset_count += 1
#             else:
#                 offset_count = 0
#                 byte_index += 1
#
#     return plc_data
#
#
# data = get_bool_array(DB_layout)
# print(data)
# for item in data:
#     print(item)
# print("Done")