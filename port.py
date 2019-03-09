import serial
a=0b10
print(int(a))
print(bin(1))

py = serial.Serial()
py.baundrate =19200
py.port = "COM3"
py.open()
print(py.is_open)
py.close()