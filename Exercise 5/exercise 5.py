Months= {1: 31,2: 28,3: 31,4: 30,5: 31, 6: 30,7: 31,8: 31,9: 30, 10: 31,11: 30,12: 31}
month_number = int(input("Enter the month number (1-12): "))
if 1 <= month_number <= 12:
        print(f"The month  has {month_number} {Months[month_number]} days.")
else:
        print("Invalid month number. Please enter a number between 1 and 12.")
