# 16.	Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).
def dicts_identical(dict1, dict2):
    return dict1 == dict2

print(dicts_identical({'a': 1, 'b': 2}, {'b': 2, 'a': 1}))  # Output: True
print(dicts_identical({'a': 1}, {'a': 2}))  # Output: False