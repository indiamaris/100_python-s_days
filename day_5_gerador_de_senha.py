
import random
senha = []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input ("How many letters would you like in your password?\n"))
nr_symbols = int(input (f"How many symbols would you like?\n"))
nr_numbers = int(input (f"How many numbers would you like?\n"))

senha += random.choices(letters, k=nr_letters)
senha += random.choices(numbers, k=nr_numbers)
senha += random.choices(symbols, k=nr_symbols)
random.shuffle(senha)
senha ="".join(senha)

print(f'Sua senha será: {senha}')


