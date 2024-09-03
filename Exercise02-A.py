#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#sh -> string hour, sr -> string rate

sh = input(" Enter Hours: ")
sr = input(" Enter Rate: ")
fh = float(sh)
fr = float(sr)
#print(fh, fr)
if fh > 40 :
    #print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    #print(reg,otp)
    xp = reg + otp
else:
    #print("Regular")
    xp = fh * fr
print("Pay:", xp)