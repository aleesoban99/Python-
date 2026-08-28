letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","^","&"]
choice1=int(input("How many letters do you want in your password?\n"))
choice2=int(input("How many numbers do you want in your password?\n"))
choice3=int(input("How many symbols do you want in your password?\n"))
import random
password=""
for i in range(0,choice1):
    password+=random.choice(letters)
for j in range(0,choice2):
    password+=random.choice(numbers)
for j in range(0,choice3):
    password+=random.choice(symbols)
list_pass=list(password)
random.shuffle(list_pass)
final_pass="".join(list_pass)
print(final_pass)