heterogeneous_list = [1, 'cat', 98.99, 2, 4]

integer_list = [num for num in heterogeneous_list if isinstance(num, int)]
print(integer_list)