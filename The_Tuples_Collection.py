# Tuples work/are like lists
# The difference is that u cannot alter its content
#U cannot use (sort(),  append(), and Reverse()) in a tuple
#exp01

x = ('Dean', 'Glenn', 'Ntare', 'Ivan')
print(x[0])
y = (1, 9, 0, 2)
print(y)
print(max(y))

for iter in y:
    print(iter)

# Tuples & Assignment
# NB: Put tuples on the left-hand side of an assignment
(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

#Tuple & Dictionaries

d = dict()
d['csev'] = 2
d['swen'] =6
for (k,v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

#comparison in tuples
#NB: if the first item is equal, python goes on to the,
#the next element, and so oon, until it finds element that differ.

d = (0, 1, 3)
x = (0, 8, 9)
if d > x:
    print(True)
else:
    print(False)


# Exercise
# what will the following code print?

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)