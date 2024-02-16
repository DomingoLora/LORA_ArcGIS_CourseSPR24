# PART 1: LIST VALUES

original_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
new_list = [num for num in original_list if num < 5]
print(new_list)

# PART 2: PRINTING RESULTS
print([num for num in original_list if num < 5])

# printing job yields = [1, 2, 3]