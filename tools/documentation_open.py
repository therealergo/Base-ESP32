import os
import sys
import platform
import setup_variables

# If there's no documentation, build it for the first time
if not os.path.isdir("./docs"):
    result = os.system("python " + os.path.join(".", "tools", "documentation_update.py"))
    if not result is 0:
        sys.exit(result)

# Select documentation main page to open based on what's availible
docfile = os.path.join(".", "docs", "html", "annotated.html")
if not os.path.isfile(docfile):
    docfile = os.path.join(".", "docs", "html", "index.html")
    if not os.path.isfile(docfile):
        print("Cound not find documention file to open!")
        sys.exit(-1)

# Open 'annotated' page as main page of documentation
platformIdentifier = platform.system().lower()
if platformIdentifier.startswith('mac') or platformIdentifier.startswith('darwin'):
    sys.exit(os.system("open " + docfile))
else:
    sys.exit(os.system(docfile))