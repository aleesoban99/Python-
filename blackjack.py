import random

card = [11,2,3,4,5,6,7,8,9,10,10,10,10]

print("---Welcome to Blackjack Game---".title())

user_cards = [random.choice(card), random.choice(card)]
computer_cards = [random.choice(card), random.choice(card)]

print(f"Your cards are {user_cards}".title())
print(f"Your total sum is {sum(user_cards)}")
print(f"Computer cards are {computer_cards[0]} and ?".title())

choice = input("Do you want another card? 'y' for yes 'n' for no: ".title()).lower()

while choice == "y":

    user_cards.append(random.choice(card))
    computer_cards.append(random.choice(card))

    print(f"Your cards are {user_cards}".title())
    print(f"Your total sum is {sum(user_cards)}")
    print(f"computer total sum is {sum(computer_cards)}")

    if sum(user_cards) > 21:
        break

    if sum(computer_cards)>21:
        break
    
    choice = input("Do you want another card? 'y' for yes 'n' for no: ".title()).lower()

print("----------------------------------------------")

print(f"Your final cards are {user_cards}".title())
print(f"Your final score is {sum(user_cards)}")

print(f"Computer cards are {computer_cards}".title())
print(f"Computer score is {sum(computer_cards)}")

if sum(user_cards) > 21:
    print("Computer wins because your total exceeds 21".title())

elif sum(computer_cards) > 21:
    print("You won because computer score exceeds 21".title())

elif sum(user_cards) > sum(computer_cards):
    print("You won!".title())

elif sum(computer_cards) > sum(user_cards):
    print("Computer won!".title())

elif sum(user_cards) == sum(computer_cards) and sum (user_cards) >21 and sum(user_cards) >21:
    print("You both lose the game because your total is same but it exceeds 21".title())

else:
    print("It's a draw".title())