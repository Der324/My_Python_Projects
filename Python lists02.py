# Concatenating lists using +
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [3, 4, 5, 6, 7, 8, 9, 10]
d = [4, 5, 6, 7, 8, 9, 10]
e = [5, 6, 7, 8, 9, 10]
f = a + b + c + d +e
print(f)
#Slicing Lists
t = [a, b, c, d, e]
t[2:4]

#Building a list from Scratch

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
stuff.append('Dan')
print(stuff)

#Built-in Function and Lists

nums =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))