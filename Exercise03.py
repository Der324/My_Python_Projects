# Write a program which repeatedly reads numbers until the user enters "done".
# once"done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than number, detect their mistake
# using try and except and print an error message and skip to the next number.

num = 0
tot = 0.0
while True :
    string_value = input('Enter a number: ')
    if string_value == 'done' :
        break
    try:
        float_value = float(string_value)
    except:
        print('Invalid input')
        continue
    #print(float_value)
    num = num + 1
    tot = tot + float_value

#print('ALL DONE')
print(tot,num,tot/num)

