import os
import sys
import setup_variables

# Call command that updates doxygen documentation
sys.exit(os.system('doxygen ' + os.path.join(".", "DoxygenConfig")))