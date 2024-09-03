#A simple Definite Loop

for i in [5, 4, 3, 2, 1, 0] :
    print(i)
print('Blastoff!')

# Definite Loop with Strings

friends = ['bone', 'don', 'son']
for friend in friends :
    print(' Happy new month:', friend)
print('done!')

#Exercise
for i in [2, 1, 5]:
    print(i)



#Loop idioms

print('Before')
for number in [0, 9, 7, 3, 1] :
    print(number)
print('After')

#finding the largest value

largest_so_far = 1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
     largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

#Exercise: which line may cause problems to the code (ANS:break, Line 44)
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)


