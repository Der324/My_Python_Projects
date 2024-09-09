#Looking Inside Lists.

friends = ['Dan', 'Dean', 'Drake', 'Num']
print(friends[2])

#Lists Are Mutable!

human = 'Man'
x = human.lower()
print(x)

numbers = [2, 3, 12, 25, 67]
print(numbers)
numbers[3] = 45
print(numbers)

#Using the range function.

print(range(4))
friends = ['Dan', 'Dean', 'Drake', 'Num']
print(len(friends))
print(range(len(friends)))

#A tale of two loops

friends = ['Dan', 'Dean', 'Drake', 'Num']
for friend in friends :
    print('Happy New Month:', friend)

for i in range(len(friends)) :
    friend = friends[1]
    print('Happy New Month', friend)

#Exercise

fruit = "banana"
x = fruit[1]
print(x)