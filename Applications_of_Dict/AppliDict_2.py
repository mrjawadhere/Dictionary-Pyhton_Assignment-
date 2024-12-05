# 22.	Write a Python program to find the key with the maximum value in the dictionary {'a': 10, 'b': 15, 'c': 7}.
data={'a': 10, 'b': 15, 'c': 7}
max_key=max(data, key=data.get)
print(max_key)

#That below code is to take info from user and give him the maximum keys value.

user_dict = {}
n = int(input("How many items do you want to add to your dictionary? "))

for i in range(n):
    key = input(f"Enter key {i + 1}: ")
    value = int(input(f"Enter value for key '{key}': "))
    user_dict[key] = value

# Finding the key with the maximum value in the user dictionary
if user_dict:  # Check if the dictionary is not empty
    max_key_user = max(user_dict, key=user_dict.get)
    print(f"\nThe key with the maximum value in your dictionary is '{max_key_user}' with a value of {user_dict[max_key_user]}.")
else:
    print("\nThe dictionary is empty.")