#The re.match() function in this code attempts to match the pattern "key" at the beginning of the string,

import re

string = "consistency is the key to success"
pattern = r"consistency"

match = re.match(pattern, string)
if match:
    print("match found:", match.group())
else:
    print("no match")
