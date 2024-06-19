from os import name
from sys import _enablelegacywindowsfsencoding
import time
import webbrowser

# Open the file in read mode
with open('test.txt', 'r') as file:
    # Read the entire content of the file
    file_content = file.read()

# Now file_content contains the content of the file as a string
print(file_content)