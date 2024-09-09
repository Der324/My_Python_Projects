 #Write a program to read through a file the contents of the file(line by line) all in upper case.

fh = open('Exercise04.txt')
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())