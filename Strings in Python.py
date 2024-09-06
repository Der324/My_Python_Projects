#Reading & Converting
name = input("Enter: ")
print(name)
apple = input("Enter: ")
x = int(apple) - 10
print(x)

# Looking inside Strings
#Banana

fruit = 'Banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)

#Len Function

fruit = 'banana'
x = len(fruit)
print(x)

#Looping Through Strings

fruit = 'Banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#exp02
fruit = 'banana'
for letter in fruit:
    print(letter)

#Looping & Counting

word = 'Photosynthesis'
count = 0
for letter in word :
    if letter == 't' :
        count = count + 1
print(count)

#looking deeper into 'in'

for n in 'Banana' :
    print(n)
