#Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# use 'find' and string slicing to extract thr portion of the string
# after the colon character and then use the 'float' function
#to convert the extracted into a floating point umber.

str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
 # print(ipos)
piece = str[ipos+2:]
 # print(piece)
 # print(piece+45.0) # will fail
value = float(piece)
print(value)
 # print(value+42.0)

word = "bananana"
i = word.find("na")
print(i)