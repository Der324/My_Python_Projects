#counting in a loop (using counter variable)

count = 0
print('Before', count)
for thing in [5, 76, 42, 84, 11, 2] :
    count = count + 1
    print(count, thing)
print('After', count)

#Summing in a loop

sum = 0
print('Before', sum)
for mark in [5, 76, 42, 84, 11, 2] :
    sum = sum + mark
    print(sum, mark)
print('After', sum)

#Average in loop

count = 0
sum= 0
print('Before', count, sum)
for value in [5, 76, 42, 84, 11, 2] :
    count = count + 1
    sum = sum+ value
    print(count, sum, value)
print('After', count, sum, sum / count)

#Filtering in a loop

print('Before')
for value in [5, 76, 42, 84, 11, 2] :
    if value  > 42 :
        print('Large number', value)
print('After')

#Boolean Variable (True/False)

found = False
print('Before', found)
for value in [5, 76, 2, 84, 11, 1] :
    if value == 2 :
        found = True
    print(found, value)
print('After', found)

#Finding the smallest number

smallest = None
print('Before')
for value in [5, 76, 2, 84, 11, 1] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)