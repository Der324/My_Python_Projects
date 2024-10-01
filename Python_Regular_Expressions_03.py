# Regular Expressions: Practical Application


#Reminding
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ",atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

#Reminding
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
words = line.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])

# The Regex Version

import re
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("@([^ ]*)",line)
print(y)


#Spam Confidence

import re
hand = open("mbox-short.txt")
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1 :
        continue
    num = float(stuff[0])
    numlist.append(num)

if numlist:
    print("Maximum:", max(numlist))
else:
    print("No matching lines found.")


# Escape Character

import re
x = "We just received $10.00 for cookies"
y = re.findall(r'\$[0-9.]+', x)
print(y)