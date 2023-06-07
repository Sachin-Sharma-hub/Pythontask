
#1st part of 4th task

def calculate_gcd(num1, num2):
while num2 != 0:
num1, num2 = num2, num1 % num2
return num1
# Test the function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd = calculate_gcd(num1, num2)
print("GCD:", gcd)

#2nd part of 4th task

def is_armstrong_number(number):
# Convert the number to a string to access its digits
num_str = str(number)

# Calculate the sum of the cubes of the digits
sum_of_cubes = sum(int(digit)**3 for digit in num_str)

# Check if the sum is equal to the number
return sum_of_cubes == number


# Test the function
num = int(input("Enter a three-digit number: "))

if is_armstrong_number(num):
print(f"{num} is an Armstrong number")
else:
print(f"{num} is not an Armstrong number")
def is_armstrong_number(number):
num_str = str(number)
sum_of_cubes = sum(int(digit)**3 for digit in num_str)
return sum_of_cubes == number
# Find Armstrong numbers between 100 and 500
armstrong_numbers = []
for num in range(100, 501):
if is_armstrong_number(num):
armstrong_numbers.append(num)
# Print the Armstrong numbers
print("Armstrong numbers between 100 and 500:")
for armstrong_num in armstrong_numbers:
print(armstrong_num)


#3rd part of 4th task

for num in range(1, 51):
if num % 3 == 0 and num % 5 == 0:
print("FizzBuzz")
elif num % 3 == 0:
print("Fizz")
elif num % 5 == 0:
print("Buzz")
else:
print(num)

#4th part of 4th task

number = int(input("Enter a number: "))
count = 0
while number != 0:
number //= 10 # Remove the last digit
count += 1
print("Total number of digits:", count)

#5th part of 4th task

for num in range(50, 0, -1):
print(num)

#6th part of 4th task

import random
# Generate a random number between 1 and 9
target_number = random.randint(1, 9)
# Initialize the flag for guessing
guessed = False
# Prompt the user for guesses
while not guessed:
guess = int(input("Guess a number between 1 and 9: "))
if guess == target_number:
print("Congratulations! You guessed the correct number.")
guessed = True
elif guess < target_number:
print("Too low. Try again.")
else:
print("Too high. Try again.")