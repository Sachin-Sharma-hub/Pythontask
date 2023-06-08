#1st part of 4th task

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = gcd(num1, num2)
    
    print("The GCD of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()


#2nd part of 4th task

def is_armstrong_number(number):
    # Convert the number to a string to access individual digits
    number_str = str(number)
    
    # Extract individual digits and calculate the sum of their cubes
    sum_of_cubes = 0
    for digit in number_str:
        sum_of_cubes += int(digit) ** 3
    
    # Check if the sum of cubes is equal to the number
    if sum_of_cubes == number:
        return True
    else:
        return False

def print_armstrong_numbers():
    for number in range(100, 501):
        if is_armstrong_number(number):
            print(number)

if __name__ == "__main__":
    print("Armstrong numbers between 100 and 500:")
    print_armstrong_numbers()
    

#3rd part of 4th task

def fizz_buzz():
    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

if __name__ == "__main__":
    fizz_buzz()

#4th part of 4th task

def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count

def main():
    number = int(input("Enter a number: "))
    
    digit_count = count_digits(number)
    
    print("The total number of digits in the number is:", digit_count)

if __name__ == "__main__":
    main()
    
#5th part of 4th task

def print_numbers():
    num = 50
    while num >= 1:
        print(num)
        num -= 1

if __name__ == "__main__":
    print_numbers()

#6th part of 4th task

import random

def guess_number():
    target_number = random.randint(1, 9)
    attempts = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
        attempts += 1
        
        if guess == target_number:
            print("Congratulations! You guessed the correct number in", attempts, "attempts.")
            break
        elif guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_number()
    
