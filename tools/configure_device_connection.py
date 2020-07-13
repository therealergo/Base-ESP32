import sys

# Write our two arguments to the config file
CONFIG_FILE = ".deviceconfig"
if len(sys.argv) == 3:
    f = open(CONFIG_FILE, 'w')
    f.writelines(sys.argv[1] + "\n" + sys.argv[2])
    f.close()
else:
    raise ValueError('Invalid configure_device_connection.py call! Must have 2 arguments, configure_device_connection.py <serial port> <upload baud>.')