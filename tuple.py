# Create a python tuple
my_tuple = (1, 2, 3)

# add 4 to the end of the tuple
# my_tuple = my_tuple + (4,)

print(my_tuple)

# Similarly, i can convert it to a list then update the list before converting back to tuple
# convert to a list 
my_tuple = list(my_tuple)

# Update the list
my_tuple.append(4)

# convert back to tuple
my_tuple = tuple(my_tuple)
print(my_tuple[2])
