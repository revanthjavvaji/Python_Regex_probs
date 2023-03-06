regex_pattern = r'[,.]'  # matches any comma or dot character


import re
print("\n".join(re.split(regex_pattern, input())))