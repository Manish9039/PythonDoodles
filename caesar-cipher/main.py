from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

print(logo)

# def encrypt(plain_text, shift_amount):
#     new_text = []
#     for letter in plain_text:
#         current_index = alphabet.index(letter)
#         shift_index = current_index + shift_amount
#         if shift_index <= 25:
#             new_text += alphabet[shift_index]
#         else:
#             shift_index -= 26
#             new_text += alphabet[shift_index]
#     encrypted_txt = ''.join(new_text)
#     print(f"The encoded text is {encrypted_txt}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = []
#     for letter in cipher_text:
#         current_index = alphabet.index(letter)
#         shift_index = current_index - shift_amount
#         plain_text += alphabet[shift_index]
#     decrypted_txt = ''.join(plain_text)
#     print(f"The decoded text is {decrypted_txt}")

def ceaser(operation, input_txt, shift_amount):
    new_text = ""
    for char in input_txt:
        if char in alphabet:
            current_index = alphabet.index(char)
            if operation == "encode":
                shift_index = current_index + shift_amount
                if shift_index <= 25:
                    new_text += alphabet[shift_index]
                else:
                    shift_index -= 26
                    new_text += alphabet[shift_index]
            elif operation == "decode":
                shift_index = current_index - shift_amount
                new_text += alphabet[shift_index]
        else:
            new_text += char
    print(f"The {operation}d text is {new_text}")


keep_operating = True
while keep_operating:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(operation=direction, input_txt=text, shift_amount=shift)
    user_input = input("Type 'yes' to continue operation and 'no' to quit.\n").lower()
    if user_input == "no":
        keep_operating = False
        print("GoodBye!")