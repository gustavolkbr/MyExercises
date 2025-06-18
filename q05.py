name = str(input("what's your name?: "))
product = str(input("what do you want to buy?: "))
product_price = float(input (f"what the price of {product}"))
quantity = float(input (f"how many {product} will you take today?"))

total_purchases = product_price*quantity

if quantity > 10:
    total_purchases = total_purchases*0.9

print(f"the total of your purchase is {total_purchases:.2f}")