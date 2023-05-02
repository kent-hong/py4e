# Prompt user for hours & rate per hour to compute gross pay
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:", round(pay, 2))