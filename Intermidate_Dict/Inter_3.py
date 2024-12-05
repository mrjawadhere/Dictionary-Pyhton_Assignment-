#  8.	Iterate through the dictionary student and print all key-value pairs in the format key: value.
Student={
    "Name":"Jawad",
    "Age":"23",
    "City":"New York",
    "Grade" : "A+"
}
for key, value in Student.items():
    print(f"Key: {key}, Value: {value}")
