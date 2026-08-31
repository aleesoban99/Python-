alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
direction= input("Type encode to encrypt and decode to decrypt: \n").lower()
text=input("Type your message: ").lower()
shift=int(input("Tell how many shifts: "))

# def encrypt(original_text,shift_amount):
#     cypher_text=""

#     for letter in original_text:
#         shifted_position=alphabets.index(letter)+shift_amount

#         shifted_position=shifted_position % len(alphabets)
#         cypher_text+=alphabets[shifted_position]
#     print(f"Here is the encoded result: {cypher_text}")


# def decrypt(original_text,shift_amount):
#     output_text=""
    
#     for letter in original_text:
#         shifted_position=alphabets.index(letter)-shift_amount
    
#         shifted_position=shifted_position % len(alphabets)
#         output_text+=alphabets[shifted_position]
#         print(f"Here is the decoded result: {output_text}")

def ceaser(original_text,shift_amount,encode_or_decode): 
    output_text="" 

    if encode_or_decode == "decode": 
        shift_amount *= -1
             
    for letter in original_text: 
        shifted_position=alphabets.index(letter)+ shift_amount
        shifted_position %=len(alphabets) 
        output_text+=alphabets[shifted_position]
        
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# encrypt(original_text=text,shift_amount=shift)
# decrypt(original_text=text,shift_amount=shift)
ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)

          