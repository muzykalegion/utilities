from glob import glob
import re
import os
# TO INSTALL: python -m pip install --upgrade pywin32
import win32com.client as win32
from win32com.client import constants

# PATH_TO_DOCS = 'C:\\path\\to\\doc\\files\\**\\*.doc'
PATH_TO_DOCS = 'D:\\Work\\Projects\\utilities\\*.doc'


def save_as_docx(path):
    # Opening MS Word
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(path)
    doc.Activate()

    # Rename path with .docx
    new_file_abs = os.path.abspath(path)
    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

    # Save and Close
    word.ActiveDocument.SaveAs(new_file_abs, FileFormat=constants.wdFormatXMLDocument)
    doc.Close(False)


# Create list of paths to .doc files
paths = glob(PATH_TO_DOCS, recursive=True)
for doc_path in paths:
    save_as_docx(doc_path)
