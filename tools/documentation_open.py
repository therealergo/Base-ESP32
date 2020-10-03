import os
import sys
import platform
import setup_variables

# If there's no documentation, build it for the first time
if not os.path.isdir("./docs"):
    result = os.system("python " + os.path.join(".", "tools", "documentation_update.py"))
    if not result == 0:
        sys.exit(result)

# Select documentation main page based on what's availible (with 'annotated' page as default)
docfile = os.path.join(".", "docs", "html", "annotated.html")
if not os.path.isfile(docfile):
    docfile = os.path.join(".", "docs", "html", "index.html")
    if not os.path.isfile(docfile):
        print("Cound not find documention file to open!")
        sys.exit(-1)

# Open selected page of documentation
platformIdentifier = platform.system().lower()
if platformIdentifier.startswith('mac') or platformIdentifier.startswith('darwin'):
    sys.exit(os.system("open " + docfile))
else:
    sys.exit(os.system(docfile))
