#Dictionaries: Common Application.
#Exp01

ccc = dict()
ccc ['csev'] = 1
ccc ['cwen'] = 1
print(ccc)
ccc ['cwen'] = ccc['cwen'] + 1
print(ccc)

#Exp02: encountering a new name.

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#the get method for dictionaries

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

#Exercise
#What will the following code print?

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))



