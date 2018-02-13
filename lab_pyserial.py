import serial
# Omega Water Trap
# PORT = '/dev/cu.usbserial-FTYZM33G' 
# Omega Sample Trap
PORT = '/dev/cu.usbserial-FT91NTBS'
BAUDRATE = 9600
BYTESIZE = serial.SEVENBITS
PARITY = serial.PARITY_ODD
STOPBITS = serial.STOPBITS_ONE
TIMEOUT = 5.0  # Must by type float
XONXOFF = True
RTSCTS = True
DSRDTR = True

try:
    ser = serial.Serial(
        port=PORT, baudrate=BAUDRATE, bytesize=BYTESIZE,
        parity=PARITY, stopbits=STOPBITS, timeout=TIMEOUT,
        xonxoff=XONXOFF, rtscts=RTSCTS, dsrdtr=DSRDTR,
    )
except serial.serialutil.SerialException:
    print('The specified port could not be found\n')
else:
    print("PORT is open? {}".format(ser.is_open))
    for key, value in ser.get_settings().items():
        print("{}: {}".format(key, value))
    ser.read()
