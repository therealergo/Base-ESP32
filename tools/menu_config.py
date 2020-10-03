import os
import sys
import shutil
import setup_variables

# Hack to clear terminal
# Prevents menuconfig window being cut off by VS Code
print('\n' * 100)

# Call the cmake command to start menuconfig for the board
result = os.system('python ./tools/build_target.py menuconfig')

# Copy generated 'sdkconfig' file into '.vscode' directory
# This lets VS Code load in the sdkconfig defines properly
# Note that any run to MenuConfig will regenerate this file
if result == 0:
    shutil.copy('./build/config/sdkconfig.h', './.vscode')
else:
    sys.exit(result)
