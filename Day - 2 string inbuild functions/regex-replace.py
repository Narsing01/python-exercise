#The re.sub() function in Python is used to replace all occurrences of a pattern in a string with a new substring.
import re

string = "A shell script is a text file that contains a sequence of commands for a UNIX-based operating system"
pattern = r"shell"

replacement = "bash"
new_text = re.sub(pattern, replacement, string)

print("modified text:", new_text)

