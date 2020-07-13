import os
import sys
import shutil
import setup_variables

# Make we've been given a CMake build target
if len(sys.argv) == 2:

    # Remove the build directory, should it exist
    if os.path.isdir('build'):
        shutil.rmtree('build')

    # Re-generate cmake build files
    # If this succeeds it will return 0
    result = os.system('cmake -S. -Bbuild -GNinja')

    # Perform a normal build if build files were successfully generated
    if result is 0:
        sys.exit(os.system('cmake --build build --target ' + sys.argv[1]))

    # Pass the exit code back to the system if it was a failure
    else:
        sys.exit(result)

else:
    raise ValueError('Invalid clean_and_build_target.py call! Must have 1 argument, clean_and_build_target.py <target>.')