# Q1: Create a tuple and sort it
tuple_data = (34, 12, 5, 89, 1)
sorted_tuple = tuple(sorted(tuple_data))
print("Sorted tuple:", sorted_tuple)

# Q2: Create a tuple of numbers and print sum of all the elements
num_tuple = (10, 20, 30, 40, 50)
print("Sum of elements in the tuple:", sum(num_tuple))

# Q3: Find maximum and minimum of a tuple
print("Maximum value:", max(num_tuple))
print("Minimum value:", min(num_tuple))

# Q4: Count the occurrence of an element in a tuple in a specific range
tuple_count = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
start_index, end_index = 2, 8 
print("Count of 3 in specified range:", tuple_count[start_index:end_index].count(3))

# Q5: Reverse a tuple
reversed_tuple = tuple_count[::-1]
print("Reversed tuple:", reversed_tuple)
