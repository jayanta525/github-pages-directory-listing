"""import os.path"""
import os

for dirname, dirnames, filenames in os.walk('.'):

    if 'index.html' in filenames:
        print("removing leftover index.html")
        os.remove(os.path.join(dirname, 'index.html'))
