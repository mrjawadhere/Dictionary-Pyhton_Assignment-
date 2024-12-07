# 26.	Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, write a Python program to add the values of matching keys and print the result.

dict1 = {'a': 5, 'b': 10}
dict2 = {'a': 3, 'b': 7}

result = {key: dict1[key] + dict2[key] for key in dict1}
print(result)