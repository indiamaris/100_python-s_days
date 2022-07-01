print ("Welcome to the PyPassword Generator!")

nr_letters = int (input ("How many letters would you like in your password?\n"))
nr_symbols = int (input (f"How many symbols would you like?\n"))
nr_numbers = int (input (f"How many numbers would you like?\n"))
letra_secreta = random.choices(letters, k=nr_letters)
numero_secreto = random.choices(numbers, k=nr_numbers)
simbolo_secreto = random.choices(symbols, k=nr_symbols)
senha = letra_secreta + numero_secreto + simbolo_secreto
random.shuffle(senha)
senha ="".join(senha)
print(f'A sua senha: {senha}')
