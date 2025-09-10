# function doesn't work if defined after called
def computepay(hours, rate) :
    if hours > 40.0 :
        pay = (hours - 40.0) * (1.5 * rate) + (40.0 * rate)
    else :
        pay = hours * rate
    return print('Pay', pay)

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
try :
    h = float(hours)
    r = float(rate)
except :
    print("Please enter a numeric value")
    quit()
computepay(h, r)