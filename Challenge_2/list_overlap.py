# PART 3: LIST OVERLAP

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

common_items = set(list_a) & set(list_b)
print("Common items:", common_items)

#OVERLAPPING PRINTING JOB
non_overlapping_items = set(list_a) ^ set(list_b)
print("Non-overlapping items:", non_overlapping_items)