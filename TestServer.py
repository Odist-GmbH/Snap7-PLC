from PyLcSnap7.PLC import PLCServer

def main():
    s = PLCServer()
    s.start()
    print(s)

if __name__ == '__main__':
    main()