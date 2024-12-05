# 21.	Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".
def get_value(dictionary, key):
    return dictionary.get(key, "Key not found")

print(get_value({'a': 1, 'b': 2}, 'b'))  

print(get_value({'a': 1, 'b': 2}, 'c'))