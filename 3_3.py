score = input("Enter Score: ")
try :
    s = float(score)
except :
    print("Please enter a value between 0.0 and 1.0")
    quit()
if s > 1.0 :
    print("Please enter a value between 0.0 and 1.0")
    quit()
elif s < 0.0 :
    print("Please enter a number between 0.0 and 1.0")
    quit()
elif s >= 0.9 :
    grade = 'A'
elif s >= 0.8 :
    grade = 'B'
elif s >= 0.7 :
    grade = 'C'
elif s >= 0.6 :
    grade = 'D'
else :
    grade = 'F'
print(grade)