# Regular Expressions: Matching & Extracting Data.

import re
x = "My 4 fAvOrite nUmbers are 11, 22, 27 and 47"
y = re.findall("[0-9]+", x)
print(y)

y = re.findall("[AEIOU]+", x)
print(y)

# Greedy Matching

import re
x = 'From: Using the: character'
y = re.findall('^F.+:', x)
print(y)

# Non-Greedy

import re
x = 'From: Using the: character'
y = re.findall('^F.+?:', x)
print(y)

#Fine_Tunning String Extraction

import re
x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+',x)
print(y)

# Exercise

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)