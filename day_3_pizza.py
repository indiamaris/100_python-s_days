
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
preco = 0
if size == 'S':
    preco = 15
    if add_pepperoni == 'Y':
        preco = preco + 2
if size == 'M':
    preco = 20
    if add_pepperoni == 'Y':
        preco = preco + 3
if size == 'L':
    preco = 25
    if add_pepperoni == 'Y':
        preco = preco + 3
if extra_cheese == 'Y':
    preco = preco+1
print(f'Your final bill is: ${preco}.')
