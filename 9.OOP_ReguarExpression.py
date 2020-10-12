import re

string = "Search inside the string please. the word"
result = re.search('The', string)
result.group()


string = "Search inside the string please. the word please"
pattern = re.compile('the')
a = pattern.search(string)
a
b = pattern.findall(string)
b

pattern2 = re.compile('Search inside the string please. the word')
c = pattern2.fullmatch(string)
c.group()

pattern3 = re.compile('Search inside the string please. the word')
d = pattern3.match(string)
d.group()


# password checker
# at least 8 characters
# contain any letters, numbers, and $%#@!
# has to end with a number

import re

regex = r"[a-zA-Z0-9$%@#!]{8,}\d"

test_str = "ding8fein5"



matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


regex = r"[a-zA-Z0-9$%@#!]{8,}\d"
pattern = re.compile(regex)
test_str = "ding8fein5"
check = pattern.fullmatch(test_str)
check

