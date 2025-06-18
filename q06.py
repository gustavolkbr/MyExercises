vehicle_price = float(input("what's the vehicle price?: ")) 
numof_installment = int(input("what the number of installments?: "))
percent = float(input("what's the interest rate %?:" ))
interest_rate = percent/100

installment = (vehicle_price/numof_installment)*(1+interest_rate)
total_price = installment*numof_installment

print(f"your car will cost R${total_price:.2f}")