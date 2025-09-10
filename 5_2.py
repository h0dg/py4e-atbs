largest = None
smallest = None

while True :
    nin = input("Enter Number: ")
    if nin == 'done' :
        break
    else :
        try :
            num = int(nin)
        except :
            print("Invalid input")
            continue
        if largest is None :
            largest = num
            smallest = num
        elif num < smallest :
            smallest = num
        elif num > largest :
            largest = num

print("Maximum is", largest)
print('Minimum is', smallest)