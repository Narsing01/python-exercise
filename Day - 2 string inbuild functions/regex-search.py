#The re.search() function in Python is used to search for a pattern in a string

import re

string = "old keys will not open new doors"
pattern = r"old keys"

search = re.search(pattern, string)

if search:
    print("search found:", search.group())
else:
    print("search not found")

