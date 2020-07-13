import os
import sys
import setup_variables

# Ensure we have a built elf file for the ESP-IDF monitor to use
result = os.system('python ./tools/build_target.py all')

# Call the command to open the ESP-IDF monitor for the board
if result is 0:
    sys.exit(os.system('python ' + os.environ["IDF_PATH"] + '/tools/idf.py monitor'))

# Pass the build exit code back to the system if it was a failure
else:
    sys.exit(result)