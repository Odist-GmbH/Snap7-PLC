import PyLcSnap7



if __name__ == '__main__':
    s7 = PyLcSnap7.S7Conn()
    d = s7.readBoolArray(811,0, 3000)
    wassertemp = PyLcSnap7.Smarttags.Real(s7,811,376)

    print(1)