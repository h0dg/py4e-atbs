hours = input("Enter Hours:")
try :
    h = float(hours)
    try :
        rate = input("Enter Rate:")
        r = float(rate)
        if h > 40.0 :
            ot = h - 40.0
            pay = ot * r * 1.5 + 40.0 * r
        else :
            pay = h * r
        print (pay)
    except :
        print("Error, please enter numeric input")
except :
    print("Error, please enter numeric input")
