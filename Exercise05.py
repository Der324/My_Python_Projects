han = open('mbox-short-exercise05.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
# guardian a bit stronger
    if len(wds) < 3 :
        continue
    if wds[0] != 'From' :
        continue
    print(wds[2])


# another method!

han = open('mbox-short-exercise05.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
#guardian in a compound statement.
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])