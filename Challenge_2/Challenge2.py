# 1. List values
# Using this list:
#
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# You need to do two separate things here and report both in your Python file.
# You should have two solutions in this file, one for item 1 and one for item 2.
# Item 2 is tricky so if you get stuck try your best (no penalty), for a hint check
# out the solution by desiato here.
#
# Make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python (you do not need to append to a list just print the output).

# PART 1: LIST VALUES

original_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
new_list = [num for num in original_list if num < 5]
print(new_list)

# PART 2: PRINTING RESULTS
print([num for num in original_list if num < 5])

# printing job yields = [1, 2, 3]