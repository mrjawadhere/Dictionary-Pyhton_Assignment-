# 24.	Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}.
data = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
unique_dict = {}
for key, value in data.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print(unique_dict)