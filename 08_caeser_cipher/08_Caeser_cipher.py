from random import randint
from art_caeser import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_to_cypher = alphabet * 2

print(logo)

def ceaser(direction, text, shift):
    if direction != 'decode' and direction != 'encode':
        return print('Message is not set to decode or encode.')
    for letter in text:
        try:
            ind = alphabet.index(letter)
            if direction == 'decode':
                ind += 26
                letter = alphabet_to_cypher[ind - shift]
            elif direction == 'encode':
                letter = alphabet_to_cypher[ind + shift]
        except:
            letter = letter
        word_to_return.append(letter)
    print(f"The {direction}d text is {''.join(word_to_return)}")

while True:
    direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message:\n").lower()
    try:
        shift_input = int(input("Type the shift number:\n"))
    except:
        shift_input = randint (1, 26)
        print(f"Shift was set to {shift_input}")

    if shift_input > 26:
        shift_input = shift_input % 26

    word_to_return = []
    text = list(text_input)

    ceaser(direction_input, text_input, shift_input)
    exit = input("Type 'yes' if you want to restart the program, type 'no' if you want to exit.\n")

    if exit != 'yes':
        break