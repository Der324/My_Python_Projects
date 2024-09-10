# Relationship between Strings & Lists

abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[2])

#loop!
abc = 'with three words'
stuff = abc.split()
print(stuff)
for w in stuff:
    print(w)

#space

line = 'A lot     of spaces'
etc = line.split()
print(etc)
 #exp02

line = 'nice;living;with;human'
thing = line.split()
print(thing)

thing = line.split(';')
print(thing)
print(len(thing))

#using email

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('from ') :
        continue
    words = line.split()
    print(words[2])

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)
#the Double Split Pattern.
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#Exercise.
#What does n equal in this code?

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]
print(n)