first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = last_name + " " + first_name
print("Reversed name:", full_name)

n = int(input("Enter an integer (n): "))

nn = int(f"{n}{n}")  # concatenate n twice
nnn = int(f"{n}{n}{n}")  # concatenate n thrice

result = n + nn + nnn
print("Result:", result)

strings = ["Name", "Is", "James"]
result = "**".join(strings)
print(result)

number = 3.14159
print("Formatted number: {:.2f}".format(number))

input_str = input("Enter three strings separated by a space: ")
strings = input_str.split()

if len(strings) != 3:
    print("Invalid input. Please enter exactly three strings separated by a space.")
else:
    string1 = strings[0]
    string2 = strings[1]
    string3 = strings[2]

    print("String 1:", string1)
    print("String 2:", string2)
    print("String 3:", string3)
