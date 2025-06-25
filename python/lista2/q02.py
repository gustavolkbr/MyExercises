total = 0
i = 0

while True:
    num = float(input("type a number: "))
    if num < 0:
        break

    total += num
    i += 1
    
if i > 0:
    average = total / i
    print(average)