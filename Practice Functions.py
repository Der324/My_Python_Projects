#Stored (and reused) Steps

def thing() :
    print("Hello")
    print("FUN")

thing()
print("Zap")
thing()


big = max("Hello you")
print(big)

tiny = min("Hello world")
print(tiny)

#types Conversions

print (float(99) / 100)

i = 42
type(i)
f = float(i)
print(f)

type(f)
print(1 + 2 * float(3) / 4 - 5)

#Building our own Functions

x = 5
print('Hello')

def print_lyrics(): #it's not calling instead it is remembering/storing
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
x = x + 2
print(x)

#call/invoking def


x = 5
print('Hello')

def print_lyrics(): #it's not calling instead it is remembering/storing
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)


#Parameters

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

#Return Value

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'), 'Glenn')
print(greet('se'), 'Sally')
print(greet('fr'), 'Micheal')


#Multiple Parameters / Arguments

def addtwo(a, b):
    added = a + b
    return added
x = addtwo(5, 5)
print(x)

#Exercise

def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()