print("welcome to rock paper sciccors game!")
rps=["R","P","S"]
import random
user_choice=input("chose rock paper and sciccors (R,P,S)\n").upper()
computer_choice=random.choice(rps)
print(f"You choosed {user_choice}")
print(f"computer chooses {computer_choice}")
if user_choice== "R" and computer_choice=="R":
    print("Its a Draw!")
elif user_choice== "P" and computer_choice=="P":
    print("Its a Draw!!")
elif user_choice== "S" and computer_choice=="S":
    print("Its a Draw!!!")
elif user_choice=="R" and computer_choice=="P":
    print("Computer Wins")
elif user_choice=="R" and computer_choice=="S":
    print("You win!!")
elif user_choice=="P" and computer_choice=="S":
    print("Computer wins!!")
elif user_choice=="S" and computer_choice=="R":
    print("Computer wins!!")
elif user_choice=="S" and computer_choice=="P":
    print("You wins!!")
elif user_choice=="P" and computer_choice=="R":
    print("You win!!")
else:
  print("Invalid input please choose between R-P-S")