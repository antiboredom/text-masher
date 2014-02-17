import sys
import re

filename = sys.argv[1]
temp = ""
for line in open(filename):
    temp += line
temp = temp.replace("\n", "")
temp = temp.replace("\r", "")
temp = temp.replace("\t", "")

quotes = [l.strip() for l in temp.split(". ")]
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
quotes = pat.findall(temp)

temp = ""
for line in sys.stdin:
    temp += line

text = re.split('".+?"', temp)
#text = temp.split('"')
j = 0
for index, line in enumerate(text):
    if index % 2 == 1 and j + 1 < len(quotes):
        #text[index] = '"' + coming_insurrection[j] + '."' 
        text[index] =  quotes[j]
        j = j + 1

print '"'.join(text)

#import re
#pattern = r'".+?"'
#regex = re.compile(pattern)
#for match in regex.finditer(temp):
    #print "%s: %s" % (match.start(), match.group(0))

#print '"'.join(text)

#print "".join(text)
#j = 0
#for l in text:
    #if i % 2 == 0:
        #print l
    #else:
        #print '"' + coming_insurrection[j] + '."'
        #j = j + 1
    #i = i + 1

#print text

#print coming_insurrection
