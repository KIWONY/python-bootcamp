# def function_name(parameter):
#     print(f"hi{parameter}")
# function_name(argument)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    sum = ""
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position + shift_amount
        a = alphabet[new_position]
        sum += a
    print(f"The encoded text is{sum}")

def decrypt(changed_text,shift_amount):
    sum =""
    for i in changed_text:
        changed_position = alphabet.index(i)
        original_position = changed_position - shift_amount
        a = alphabet[original_position]
        sum += a
    print(f"The decoded text is {sum}")


if direction == "encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)

