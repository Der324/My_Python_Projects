fname = input("Enter File: ")
if len(fname) < 1 : fname = "crown_02.txt"
hand = open(fname)

di = dict()
for lin in hand:
    lin= lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

#print(di)

#x = sorted(di.items())
#print(x[:5])
tmp = list()
for j,k in di.items():
   # print(j,k)
    newtup = (k,j)
    tmp.append(newtup)

#print("Flipped", tmp)
tmp = sorted(tmp, reverse=True)
#print("sorted", tmp[:5])
for k,j in tmp[:5]:
    print(j,k)