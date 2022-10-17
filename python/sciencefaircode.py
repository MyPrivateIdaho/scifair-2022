import serial, time

ser = serial.Serial('/dev/ttyUSB0')
python_file = open("data.py", "w")

while True:
    data = []
    for index in range(0,10):
        datum = ser.read()
        data.append(datum)

    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    print(pmtwofive, pmten)
    python_file.write(str(pmtwofive) + "," + str(pmten) + "," + str(time.time()) + "\n")
    time.sleep(1)

    

python_file.close()


    
