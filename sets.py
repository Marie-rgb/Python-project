user_input = input("Enter your first set")
set1 = set(map(int, user_input.split()))

user_input1 = input("Enter your second set")
set2 = set(map(int, user_input1.split()))

set_sum = set1.intersection(set2)

print("\nset1:", set1)
print("set2:", set2)
print("Common Elements Set:", set_sum)

