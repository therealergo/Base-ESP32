import os
import sys
import setup_variables

# Make we've been given a CMake build target
if len(sys.argv) == 2:

    # If build files have previously been generated, build normally
    if os.path.isdir('build'):
        sys.exit(os.system('cmake --build build --target ' + sys.argv[1]))

    # If no build files have previously been generated, do a full rebuild
    else:
        sys.exit(os.system('python ./tools/clean_and_build_target.py ' + sys.argv[1]))

else:
    raise ValueError('Invalid build_target.py call! Must have 1 argument, build_target.py <target>.')