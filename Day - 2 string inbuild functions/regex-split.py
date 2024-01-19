#
import re

string = "hardwork,persistent,perseverence,confidence"
pattern = r","

split_result = re.split(pattern, string)
print("this is split result:", split_result)

