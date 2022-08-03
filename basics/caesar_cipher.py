# def function_name(parameter):
#     print(f"hi{parameter}")
# function_name(argument)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text,shift_amount,direction):
    sum =""
    if direction == "decode":
        shift_amount = shift_amount * -1

    for i in start_text:
        if start_text in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            sum += alphabet[new_position]
        else:
            sum+= i
    print(f"The {direction}d text is{sum}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # 나머지 연산으로 alphabet 리스트에 있는 글자 수 보다 큰 개수의 단어(shift number)를 입력했을 때
    # 리스트 개수만큼 나누어서
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, direction=direction)

