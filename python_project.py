# Write a python program that multiplies all the items in a list

list_Multiplication = [2, 3, 5]
result = 1 

for i in list_Multiplication:
    result = result * i
    # print(result)

# Write a python program to get a list, sorted in increasing order by the last element in each tuple, from a given list of non-empty tuples

sample_list = [(2,5), (1,2), (4,4), (2,3), (2,1)]
# new_list =[]
# for i in sample_list:
#     convert = list(i)
#     new_list.append(convert)

# print(new_list.sort())
sample_list.sort(key=lambda x:x[1])

# print(sample_list)

# Write a Python program that combines two dictionaries by adding values for common keys

d1= {
    "a": 100,
    "b": 200,
    "c": 400
}

d2= {
    "a": 300,
    "b": 200,
    "d": 400
}

expected_result = {}

for key,value in d1.items():
    expected_result[key] =value

for key in d2:
    print("hello")

print(expected_result)