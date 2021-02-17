from PyLcSnap7.PLC import S7
x = S7("127.0.0.1")
x.connect()

plc_info = x.client.get_cpu_state()
print(plc_info)


# print(x.readString(1,0,255))
# print(x.readBool(1,256,0))
# print(x.readBool(1,256,1))
# print(x.readString(1,258,254))

#st = x.SmartTags.Bool(1,0,0)

#print(x.readBool(1,0,1))
# print(x.readString(1,2,255))
# print(x.readString(1,258,254))
#e
# if x.readBool(1,0,0):
#     x.writeString(1,2,"FUCK_YEAH", 255)
#
#     print(x.readString(1, 2, 255))
#

print("1")


