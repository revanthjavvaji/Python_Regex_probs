# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

vowels = "AEIOUaeiou"
consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"

# define the regular expression pattern
pattern = r"(?<=[" + consonants + "])([" + vowels + "]{2,})(?=[" + consonants + "])"

# read the input string
s = input()

# find all matching substrings
matches = re.findall(pattern, s)

# print the matches or -1 if no match is found
if matches:
    for match in matches:
        print(match)
else:
    print(-1)
