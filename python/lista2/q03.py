price = float(input("how much is it?: "))
cash = 0.00

while cash < price:
    print(f"insufficient money, you still need ${price-cash:.2f}: ")
    inserted = float(input("how much do you want to insert now?: "))
    cash += inserted

print("you have reached the necessary cash, congrats!")