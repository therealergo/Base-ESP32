import os
import sys
import setup_variables

# Call flash script
result = os.system('python ./tools/build_target.py flash')
if result is 0:

    # Then call monitor script if flash succeeded
    sys.exit(os.system('python ./tools/monitor.py'))
else:
    sys.exit(result)