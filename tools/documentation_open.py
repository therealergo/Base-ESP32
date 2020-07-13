import os
import sys
import platform
import setup_variables

# If there's no documentation, build it for the first time
if not os.path.isdir("./docs"):
    result = os.system("python " + os.path.join(".", "tools", "documentation_update.py"))
    if not result is 0:
        sys.exit(result)

# Open 'annotated' page as main page of documentation
platformIdentifier = platform.system().lower()
if platformIdentifier.startswith('mac') or platformIdentifier.startswith('darwin'):
    sys.exit(os.system("open " + os.path.join(".", "docs", "html", "annotated.html")))
else:
    sys.exit(os.system(os.path.join(".", "docs", "html", "annotated.html")))