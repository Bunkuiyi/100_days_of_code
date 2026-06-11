alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     encoded_letters = ""
#     for letter in original_text :
#         position = alphabet.index(letter)
#         position += shift_amount
#         position %= len(alphabet) # 0-25
#         encoded_letters += alphabet[position]
#     print(f"Here is the encoded result: {encoded_letters}")
#
# encrypt(original_text=text, shift_amount=shift)

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# def decrypt (original_text, shift_amount) :

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

# def decrypt (original_text, shift_amount) :
#     decoded_letter = ""
#     for letter in original_text:
#         decoded_letter = ""
#         position = alphabet.index(letter)
#         position -= shift_amount
#         decoded_letter += alphabet[position]
#     print(f"Here is the decoded result: {decoded_letter}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount):
    if direction == "encode":
        encoded_letters = ""
        for letter in original_text:
            position = alphabet.index(letter)
            position += shift_amount
            position %= len(alphabet)  # 0-25
            encoded_letters += alphabet[position]
        print(f"Here is the encoded result: {encoded_letters}")

    elif direction == "decode":
        decoded_letters = ""
        for letter in original_text:
            position = alphabet.index(letter)
            position -=  shift_amount
            position %= len(alphabet)
            decoded_letters += alphabet[position]
        print(f"Here is the decoded result: {decoded_letters}")

    else:
        print("That was the wrong input. Try again. ")


caesar(text, shift)




