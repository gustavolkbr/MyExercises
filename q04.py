salary = float(input("what's your monthly salary?: "))
overtime_hour = float(input("how much overtime did you do this month?: "))

hour_wage = salary/160
overtime_wage = (hour_wage * 1.5)*overtime_hour

total_wage = salary + overtime_wage

print(f"your total wage this month is: {total_wage:.2f}")