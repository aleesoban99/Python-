print("Welcome to treasure island game!!")
direction=input("Where do you want to go (L for left R for right?)\n")
if direction=="R":
    print("WRONG MOVE--GAME OVER!!!!")
elif direction=="L":
    choice1=input("Ok Now you want to Swim or Wait for someone(S for Swim W for wait)\n")
    if choice1=="S":
        print("WRONG MOVE--GAME OVER!!!!")
    elif choice1=="W":
     choice2=input("Now one last move to win the Game which door you want to go? RED BLUE OR YELLOW?")
if choice2=="R":
    print("SO close BETTER LUCK NEXT TIME!!")
elif choice2=="B":
    print("SO close BETTER LUCK NEXT TIME!!")
elif choice2=="Y":
    print("CONGRATIONS YOU UNLOCKED THE TREASURE!!!!")





