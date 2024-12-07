# cube 

n = int(input("Enter a number: "))
cubes = {x: x**3 for x in range(1, n + 1)}
print(cubes)