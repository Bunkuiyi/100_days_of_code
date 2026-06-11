# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1
#
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")

# if letter not in alphabet:
#     enoded_letters += letter

# TODO-3: Can you figure out a way to restart the cipher program?


def caesar(original_text, shift_amount):
    if direction == "encode":
        encoded_letters = ""
        for letter in original_text:
            if letter not in alphabet:
                    encoded_letters += letter
            else:
                    position = alphabet.index(letter)
                    position += shift_amount
                    position %= len(alphabet)  # 0-25
                    encoded_letters += alphabet[position]
        print(f"Here is the encoded result: {encoded_letters}")

    elif direction == "decode":
        decoded_letters = ""
        for letter in original_text:
            if letter not in alphabet:
                decoded_letters += letter
            else:
                position = alphabet.index(letter)
                position -= shift_amount
                position %= len(alphabet)
                decoded_letters += alphabet[position]
        print(f"Here is the decoded result: {decoded_letters}")

    else:
        print("One of your inputs was wrong. Try again. ")

encryption_over = False

while not encryption_over:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift)

    continuation = input("Type yes if you want to go again. Otherwise type no\n ").lower()

    if continuation == "no":
        encryption_over = True
        print("Goodbye")




