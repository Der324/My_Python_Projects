#Multi-way

x = 4
if x < 2 :
    print("small")
elif x < 10 :
    print("Medium")
else :
    print("Large")
print("All done!")

#Multi-way Puzzles

x = 6
if x < 2 :
    print("Below 2")
elif x >= 2 :
    print("Two or more")
else:
    print("Something else")


if x < 2 :
    print("below 2")
elif x < 20 :
    print("below 20")
elif x < 10 :
    print("below 10")
else:
    print("something else")


astr = "Hello bob"
try:
    istr = int(astr)
except:
    istr = -1
print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = "hello bob"

print("second", istr)

rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print("Nice work")
else:
    print("Not a number")