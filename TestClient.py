from PyLcSnap7.PLC import PLCClient


def main():
    c = PLCClient()
    c.connect()



    test_bool = c.SmartTags.Bool(107,0,0)
    test_bool.write(True)

    test_string = c.SmartTags.String(107,90,)
    test_string.write('asda')
    print(test_string.read())



if __name__ == '__main__':
    main()
