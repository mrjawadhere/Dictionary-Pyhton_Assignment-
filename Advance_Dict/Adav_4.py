# 15.	Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys
original_dict={'a':1,'b':2,'c':3}
revrse_dict={v: k for k, v in original_dict.items()}
print(revrse_dict)