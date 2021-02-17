

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
# #    print(fstring)
