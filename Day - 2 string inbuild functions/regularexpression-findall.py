
#The re.search() function in Python is used for searching a string for the presence of a pattern.

import re

string = "consistency is the key to success"
pattern = r"key"

search = re.search(pattern, string)

if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")