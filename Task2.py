#1st part of 2nd task
number = float(input("Enter a number: "))

difference = number - 17

if number > 17:
    result = 2 * abs(difference)
else:
    result = difference

print("Result:", result)
#2nd part of 2nd task
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
   
#3rd part of 2nd task
    
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    sum = 0
else:
    sum = num1 + num2 + num3

print("Sum:", sum)

#4th part of 2nd task

month_name = input("Enter the name of the month: ")

month_name = month_name.lower() 

days = 0

if month_name == "january" or month_name == "march" or month_name == "may" or month_name == "july" or month_name == "august" or month_name == "october" or month_name == "december":
    days = 31
elif month_name == "april" or month_name == "june" or month_name == "september" or month_name == "november":
    days = 30
elif month_name == "february":
    days = 28  
    # Assuming a non-leap year

print("Number of days in", month_name.title(), "is", days)

#5th part of 2nd task

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("Triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Triangle is isosceles.")
else:
    print("Triangle is scalene.")