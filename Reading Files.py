# The newline Character

stuff = ' Hello \n World!'
stuff
'Hello\nWorld!'
print(stuff)

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count:', count)

fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(len[:20])


