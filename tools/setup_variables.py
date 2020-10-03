import os
import sys
import zipfile
import platform

# Tell ESP-IDF that we're targetting esp32
os.environ['IDF_TARGET'] = 'esp32'

# Initialize all git submodules on first startup
if not os.path.isfile('.submodconfig'):
    print('Performing first-time git submodule initialization...')
    result = os.system('git submodule update --init --recursive')
    if result == 0:
        f = open('.submodconfig', 'w')
        f.write('submodule update completion marker')
        f.close()
    else:
        sys.exit(result)

# Initialize all over-size zipped files on first startup
if not os.path.isfile('.zipconfig'):
    print('Performing first-time large file unzipping...')
    with zipfile.ZipFile("tools/linux64/doxygen/doxygen.zip","r") as zip_ref:
        zip_ref.extractall("tools/linux64/doxygen")
    with zipfile.ZipFile("tools/macos/doxygen/Frameworks/libclang.dylib.zip","r") as zip_ref:
        zip_ref.extractall("tools/macos/doxygen/Frameworks")
    with zipfile.ZipFile("tools/macos/doxygen/Resources/doxygen.zip","r") as zip_ref:
        zip_ref.extractall("tools/macos/doxygen/Resources")
    f = open('.zipconfig', 'w')
    f.write('large file unzip completion marker')
    f.close()

# Read the device's serial port and baud rate from the config file
CONFIG_FILE = '.deviceconfig'
try:
    config_lines = open(CONFIG_FILE, 'r').readlines()
    line_port = config_lines[0].strip()
    line_baud = config_lines[1].strip()
    os.environ['ESPPORT'] = '' if line_port=='auto' else line_port
    os.environ['ESPBAUD'] = line_baud
except (IOError, IndexError):
    os.environ['ESPPORT'] = ''
    os.environ['ESPBAUD'] = '115200'

# Setup IDF_PATH variable for building
os.environ['IDF_PATH'] = os.path.abspath('./tools/esp-idf')

# Get a string that identifies the current OS
platformIdentifier = platform.system().lower()

# Add python dependencies to current process's path, PATH, and PYTHONPATH
pythonToolsDir = os.path.abspath('./tools/python')
sys.path.insert(0, pythonToolsDir)
os.environ['PATH'] = pythonToolsDir + os.pathsep + os.environ['PATH']
if "PYTHONPATH" in os.environ:
    os.environ['PYTHONPATH'] = pythonToolsDir + os.pathsep + os.environ['PYTHONPATH']
else:
    os.environ['PYTHONPATH'] = pythonToolsDir

# Setup os-specific PATH variable for building
if platformIdentifier.startswith('win'):
    os.environ['PATH'] = os.path.abspath('./tools/win64/cmake/3.13.4/bin')                      + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/win64/ninja/1.9.0')                           + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/win64/mconf/v4.6.0.0-idf-20190628')           + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/win64/xtensa-esp32-elf/esp-2019r2-8.2.0/bin') + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/win64/doxygen')                               + os.pathsep + os.environ['PATH']
elif platformIdentifier.startswith('mac') or platformIdentifier.startswith('darwin'):
    os.environ['PATH'] = os.path.abspath('./tools/macos/cmake/3.13.4/bin')                      + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/macos/ninja/1.9.0')                           + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/macos/xtensa-esp32-elf/esp-2019r2-8.2.0/bin') + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/macos/doxygen/Resources')                     + os.pathsep + os.environ['PATH']
elif platformIdentifier.startswith('linux'):
    os.environ['PATH'] = os.path.abspath('./tools/linux64/cmake/3.13.4/bin')                      + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/linux64/ninja/1.9.0')                           + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/linux64/xtensa-esp32-elf/esp-2019r2-8.2.0/bin') + os.pathsep + os.environ['PATH']
    os.environ['PATH'] = os.path.abspath('./tools/linux64/doxygen')                               + os.pathsep + os.environ['PATH']
else:
    raise ValueError('Unable to determine host OS!')
