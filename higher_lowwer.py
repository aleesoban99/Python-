import random

print("---Welcome to higher lower game".title())
cricketers = {
    "Virat Kohli": 275,
    "MS Dhoni": 51,
    "Sachin Tendulkar": 50,
    "Rohit Sharma": 44,
    "Hardik Pandya": 40,
    "Suryakumar Yadav": 25,
    "Shubman Gill": 17,
    "KL Rahul": 21,
    "Rishabh Pant": 12,
    "Yuzvendra Chahal": 10,
    "Jasprit Bumrah": 18,
    "Shikhar Dhawan": 18,
    "Ravindra Jadeja": 15,
    "Mohammed Shami": 17,
    "Dinesh Karthik": 4,
    "Irfan Pathan": 7,
    "Yuvraj Singh": 18,
    "Harbhajan Singh": 10,
    "Suresh Raina": 26,
    "Sanju Samson": 9,
    "David Warner": 11,
    "Pat Cummins": 3,
    "Steve Smith": 4,
    "Glenn Maxwell": 4,
    "Mitchell Starc": 2,
    "Travis Head": 3,
    "Jos Buttler": 3,
    "Ben Stokes": 3,
    "Joe Root": 2,
    "Jofra Archer": 2,
    "Babar Azam": 6,
    "Shaheen Afridi": 4,
    "Mohammad Rizwan": 4,
    "Shadab Khan": 4,
    "Naseem Shah": 3,
    "Fakhar Zaman": 2,
    "Rashid Khan": 11,
    "Mohammad Nabi": 2,
    "Kane Williamson": 2,
    "Trent Boult": 1,
    "AB de Villiers": 27,
    "Faf du Plessis": 5,
    "Chris Gayle": 18,
    "Andre Russell": 5,
    "Dwayne Bravo": 4,
    "Kieron Pollard": 2,
    "Quinton de Kock": 1,
    "Marnus Labuschagne": 1,
    "Lasith Malinga": 3,
    "Shoaib Akhtar": 4
}

score=0
loop=True
while loop is not False:
    random_selcted1= random.choice(list(cricketers.keys()))
    random_selcted2= random.choice(list(cricketers.keys()))
    while random_selcted1 == random_selcted2:
        random_selcted2 = random.choice(list(cricketers.keys()))


    print(f"choose between {random_selcted1} and {random_selcted2}".title())
    choice_user=int(input("enter 1 or 2: ".title()))
    if choice_user ==1:
        if cricketers[random_selcted1] > cricketers[random_selcted2]:
            print("you won this round!".title())
            score+=1
            print(f"your current score is {score}".title())

        else:
            print("You lost")
            print(f"your Final score is {score}".title())
            break

    elif choice_user==2:
        if cricketers[ random_selcted2] >cricketers [random_selcted1]:
            print("you won this round".title())
            score+=1
            print(f"Current score is {score}".title())

        else:
            print("You lost")
            print(f"your final score is {score}".title())
            break