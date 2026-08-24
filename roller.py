print("welcome to roller coaster ride!")
bill=0
height=int(input("what is your height?\n"))
if height >=120:
    print("you are allowed to ride")
    age=int(input("what is your age??"))
    if age<=12: 
        bill=7  
        print("please pay 7$")
    elif age<=18:
        bill=10
        print("pay 10 $")
    else:
        bill=12
        print("please pay 12$")
    wants_photo=str(input("do you want photo? y for yes n for no "))
    if wants_photo=="y":
        bill+=3
        print(f"now your total bill is {bill}")
    else:
        print(f"your total bill is {bill}")
else:
    print("you are not allowed to enter")