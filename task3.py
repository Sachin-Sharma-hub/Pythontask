#1st part of 3rd task

def find_smallest_number(numbers):
    if not numbers:  # Check if the list is empty
        return None
    
    smallest = numbers[0]  # Assume the first number is the smallest
    
    for num in numbers:
        if num < smallest:
            smallest = num
    
    return smallest

# Example usage
numbers_list = [5, 2, 8, 1, 9, 3]
smallest_number = find_smallest_number(numbers_list)
print("The smallest number is:", smallest_number)

#2nd part of 3rd task

def is_list_empty(lst):
    if not lst:
        return True
    else:
        return False

# Example usage
empty_list = []
non_empty_list = [1, 2, 3]

if is_list_empty(empty_list):
    print("The list is empty")
else:
    print("The list is not empty")

if is_list_empty(non_empty_list):
    print("The list is empty")
else:
    print("The list is not empty")

#3rd part of 3rd task

def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
list3 = [8, 9, 10]

if has_common_member(list1, list2):
    print("List1 and List2 have at least one common member.")
else:
    print("List1 and List2 do not have any common members.")

if has_common_member(list1, list3):
    print("List1 and List3 have at least one common member.")
else:
    print("List1 and List3 do not have any common members.")

#4th part of 3rd task

def append_list(list1, list2):
    list2.extend(list1)

# Example usage
list1 = [1, 2, 3]
list2 = [4, 5, 6]

append_list(list1, list2)
print("List2 after appending List1:", list2)

#5th part of 3rd task

def remove_elements(lst):
    indices_to_remove = [0, 4, 5]
    result = [elem for i, elem in enumerate(lst) if i not in indices_to_remove]
    return result

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

modified_list = remove_elements(my_list)
print("Modified list:", modified_list)

#6th part of 3rd task

# Take 10 integer inputs from the user
user_inputs = []
for _ in range(10):
    num = int(input("Enter an integer: "))
    user_inputs.append(num)

# Create a new list with elements in reverse order
reversed_list = user_inputs[::-1]

# Print the original and reversed lists
print("Original list:", user_inputs)
print("Reversed list:", reversed_list)