alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def tela():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    received_text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encriptator(received_text, shift, direction)

def encriptator(received_text, shift, direction):
    text_shifted = []
    if direction == 'decode':
        shift *= -1
    for letter in received_text:
        position = alphabet.index(letter)
        new_position = position + shift
        text_shifted.append(alphabet[new_position])
    text_shifted = "".join(text_shifted)
    print(text_shifted)

tela()
