hrs = input("Enter Hours:")
h = float(hrs)
r = input("Enter pay rate:")
rate = float(r)
if h > 40.0 :
    ot = h - 40.0
    pay = ot * rate * 1.5 + 40.0 * rate
else :
    pay = h * rate
print (pay)