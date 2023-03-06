import re

# read the input strings
s = input().strip()
sub = input().strip()

# define the regular expression pattern
pattern = re.compile('(?=' + sub + ')')

# find all occurrences of the substring using re.finditer()
matches = pattern.finditer(s)

# print the starting and ending indices of each match
found = False
for m in matches:
    print((m.start(), m.start() + len(sub) - 1))
    found = True

# if no match is found, print (-1, -1)
if not found:
    print((-1, -1))
