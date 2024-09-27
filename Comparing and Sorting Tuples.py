# sorting Lists of Tuples

d = {"a" : 20, "b" : 6, "c" :28}
d.items()
print(d)
sorted(d.items())
print(sorted(d.items()))

# sorting without case sensitivity
#sorted_case_insensitive = sorted(d.items(),
 #                                key = lambda x: x[0].lower())
#print(sorted_case_insensitive)

#Using sorted
b = {"a" : 20, "b" : 6, "c" :28}
t = sorted(b.items())
print(t)
for k, v in sorted(b.items()):
    print(k, v)



# sort by values instead of key

z = {"a" : 20, "b" : 6, "c" :28}
tmp = list()
for k, v in z.items():
    tmp.append( (v, k) )
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)



# the top most common words.
# long method of doing it

fhand = open("romeo.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
    print(key, val)

# short method of doing it

z = {"a" : 20, "b" : 6, "c" :28}
print(sorted( [ (v, k) for k,v in z.items() ] ) )