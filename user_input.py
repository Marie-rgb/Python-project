user_input = input("Enter numbers separated by spaces: ")

numbers = [float(num) for num in user_input.split()]

sum_of_numbers = sum(numbers)

print(f"The sum is: {sum_of_numbers}")
