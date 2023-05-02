# Rewrite you pay computation to give employee 1.5 times the hourly rate for hours worked above 40 hours
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
    pay = ((hours - 40) * rate * 1.5) + 40 * rate
else:
    pay = hours * rate
print("Pay: ", round(pay, 2))