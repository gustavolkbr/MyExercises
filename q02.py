grade1 = float(input("enter your grade for 1st exam: "))
grade2 = float(input("enter your grade for 2st exam: "))
grade3 = float(input("enter your grade for 3st exam: "))

total = ((grade1*2)+(grade2*3)+(grade3*5))/10

print(f"your final grade is: {total:.2f}")