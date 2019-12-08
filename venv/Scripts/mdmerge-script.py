#!C:\Users\lola3\PycharmProjects\reviewTrackers\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'MarkdownTools==1.0.1','console_scripts','mdmerge'
__requires__ = 'MarkdownTools==1.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('MarkdownTools==1.0.1', 'console_scripts', 'mdmerge')()
    )
