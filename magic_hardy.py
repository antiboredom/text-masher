import sys
import re

filename = sys.argv[1]
temp = ""
for line in open(filename):
    temp += line

for t in ["\n", "\r", "\t"]:
    temp = temp.replace(t, "")

pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
quotes = pat.findall(temp)

temp = ""
for line in sys.stdin:
    temp += line

text = re.split('".+?"', temp, flags=re.S)

new_text = []
for index, line in enumerate(text):
    new_text.append(line)
    if index + 1 < len(quotes):
        new_text.append(quotes[index])

print '"'.join(new_text)
