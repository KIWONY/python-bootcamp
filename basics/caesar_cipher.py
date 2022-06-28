# def function_name(parameter):
#     print(f"hi{parameter}")
# function_name(argument)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(start_text,shift_amount,direction):
    sum =""
    for i in start_text:
        position = alphabet.index(i)
        if direction == "decode":
            shift_amount = shift_amount * -1

        new_position = position + shift_amount
        sum += alphabet[new_position]
    print(f"The {direction}d text is{sum}")


caesar(start_text=text,shift_amount=shift,direction=direction)

