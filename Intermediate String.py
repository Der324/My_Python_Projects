#Slicing Strings
# Mountain Kilimanjaro

m = 'Mountain Kilimanjaro'
print(m[0:8])
print(m[9:40])

#exp02

m = 'Mountain Kilimanjaro'
print(m[:8])
print(m[16:])
print(m[:])

#String Concatenation
a = 'Hallo'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

# Using 'in' as a logical Operator

fruit = 'banana'

if 'a' in fruit:
    print("'a' is found in", fruit)

if 'h'not in fruit:
    print("'h' is not found in", fruit)

#string comparison
word = 'pineapple'

if word == 'pineapple':
    print('All right, pineapple. ')

if word < 'pineapple':
    print(' Your fruit,' + word + ', comes before pineapple.')
elif word > 'pineapple':
    print(' Your fruit,' + word + ', comes after pineapple.')
else:
    print('All right, pineapple.')

#String Library

greet = 'Sup Bro'
zap = greet.lower()
pop = greet.upper()
print(zap)
print(pop)
print('Nǐ hǎo ma'. lower())

#Searching a String

Shuǐguǒ = 'Xiāngjiāo'
pos = Shuǐguǒ.find('ng')
print(pos)
aa = Shuǐguǒ.find('m')
print(aa)

#making everything UPPER CASE

greet = 'Hello Don'
x = greet.upper()
print(x)
v = greet.lower()
print(v)

#Search & Replace

greet = 'Hello Don'
nstr = greet.replace('Don', 'John')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)


#Stripping Whitespace
greet ='  Hi gorge  '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

#prefixes

line = 'Please have a nice day'
line.startswith('Please')
line.startswith('p')
print()

#Parsing and Extracting
#exp: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

#exp02: Derick is using email: ntalenderick@gmail.com
data = 'Derick is using email: ntalenderick@gmail.com'
at_position = data.find('@')
print(at_position)

space_position = data.find(' ',at_position)
print(space_position)

host = data[at_position+1 : space_position]
print(host)
