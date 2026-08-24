print("Welcome to python pizza delivery! ")
bill=0
size=str(input("What size do you want S,M or L ?\n"))
peproni=str(input("Do you want pepproni on your pizza? Y for yes N for no\n"))
cheese=str(input("Do you want extra cheese? Y for Yes N for No\n"))
if size == "S":
    bill=15
    print("Small pizza is for 15$")
elif size == "M":
    bill=20
    print("Medium pizza is for 20 $")
elif size =="L":
    bill=25
    print("Large pizza is for 25 $")
if peproni== "Y":
    bill+=2
if cheese== "Y":
    bill +=1

    print(f"Your total bill is  {bill} $")