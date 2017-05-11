import re
string = "0.142857142857142857142857142857"

regex = re.compile(r'(.+.+)(\1)+')
match = regex.search(string)

print(match.groups())