import random
word_list = ["apple","mouse","perfume","lamp"]
chosen_word = random.choice(word_list)
print(chosen_word)

place_holder = ""
word_len=len(chosen_word)
for position in range(word_len):
    place_holder += "_"
print (place_holder)
game_over=False

corrected_letters=[]
lives=6
while not game_over:

    guess = input("Guess a letter: ").lower()
    print (guess)
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display+= letter
            corrected_letters.append(guess)
        elif letter in corrected_letters:
            display+= letter
        else:
            display+= "_"
    print (display)

    if guess not in chosen_word:
        lives-=1
        print (f"{lives} lives left!!!")

    if lives == 0:
        game_over= True
        print ("Game over!!")

    if "_" not in display:
        game_over=True
        print ("You Won")
        
