sum_num = 0
count = 0

num = int(input("text a number: "))

while num <= 100:
    print(f"you still needs {100-num} to complete")
    sum_num = int(input("text another number: "))
    num += sum_num
    count += 1

print("you've completed, congrats!!!")
print (f"you've texted {count} numbers")