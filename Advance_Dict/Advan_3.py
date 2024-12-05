# 14.	Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.
unsorted_dict={'z':1,'a':42, 'c':9}
sorted_dict=dict(sorted(unsorted_dict.items()))
print(sorted_dict)