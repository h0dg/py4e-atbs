hours = input("Enter Hours:")
rate = input("Enter Rate:")
try :
    h = float(hours)
    r = float(rate)
except :
    print("Error, please enter numeric input")
    quit() # learned quit() command.
if h > 40.0 :
    ot = h - 40.0
    pay = ot * r * 1.5 + 40.0 * r
else :
    pay = h * r
print (pay)