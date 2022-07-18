from PyLcSnap7.PLC import PLCClient


def main():
    c = PLCClient()
    c.connect()
    while True:
        val = c.cpu_in_run()
        print(val)


    test_bool = c.SmartTags.Bool(107,0,0)
    test_bool.write(True)

    print(1)
    while True:
        x = c.read_bool(107, 0, 0)
        print(x)
        print(c.write_bool(107, 0, 0, not x))
        x = c.read_byte(107, 1)
        print(x)
        print(c.write_byte(107, 1, 1))
    pass


if __name__ == '__main__':
    main()
