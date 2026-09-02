import random
difficulty=input("Choose you difficulty easy or hard?").lower()
if difficulty == "easy":
    lives=10
else:
    lives= 5

print ("Computer is guessing a number between 0 to 100..")
random_number= random.randint(0,100) 

for i in range(lives):
    
    chosen_word= int(input("Guess the number: \n"))
    if chosen_word > random_number:
        print("Wrong Guess !!Too Higher!!")
        print(f"{lives-i-1} lives left!")
    elif chosen_word < random_number:
        print("Wrong Guess!! Lower!!")
        print(f"{lives-i-1} lives left!")
    elif chosen_word == random_number:
        print("Wow yo got the number!")
        break
else:
    print(f"you lost the number was {random_number}")