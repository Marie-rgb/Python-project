person_info = {}

person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

print("\nYour information: ")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")