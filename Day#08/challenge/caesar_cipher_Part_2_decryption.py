alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(alphabet.index("h"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text=text,shift_amount=shift):
    encrypted_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        encrypted_text +=alphabet[new_position]
    
    print(encrypted_text)

def decrypt(plain_text=text, shift_amount=shift):
    decrypted_text =''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        decrypted_text +=alphabet[new_position]
    print(f"your decrypted text is  {decrypted_text}")    



if direction == 'encode':
    encrypt(text, shift)
if direction == 'decode':
    decrypt(text,shift)
    







