# Create a simple calculator application that can perform basic arithmetic operations

def calculator():
    num1 = int(input("enter first value: "))
    num2 = int(input("enter second value: "))
    operand = input("enter operator value: ")

    if operand == "+":
       return num1 + num2
    elif operand == "-":
       return num1 - num2
    elif operand == "/":
       return num1 / num2
    elif operand == "*":
        return num1 * num2
    else:
        num1 % num2         

# print(calculator())


# Write a function to find the largest of three numbers
def find_largest(a,b,c):
    return max(a,b,c)

# print(find_largest(45,6,7))


# Write a function that reverse the words of a string
def reverse_string(word):

    # for i in range(len(word)-1, -1, -1):
    #     print(word[i])
    return word[::-1]

# print(reverse_string("words"))        


# Write a function to count the numver of vowels in a string
def count_vowels(word):
    count = 0
    vowels= "aeiou"
    for i in word:
        if i.lower() in vowels:
            count += 1 
    return count

# print(count_vowels("HEllO dear"))


# Write a function to find the average of given numbers
def calculate_average (*num): 
    if (len == 0):
        return 0
    return sum(num) / len(num)

# print(calculate_average(3, 5, 10))

        #Alternatively
def calculate_average (num):
    return sum(num)/ len(num)

# print(calculate_average([3, 5, 10]))

# Write a function that accepts a word and check if it reads the same forward and backword
def is_Palindromes (word):
    if word.lower() == word[::-1].lower():
        print(f"{word} is a palindrome")
    else: 
        print(f"{word} is not a palindrome")

# More simplified and considering spaces
def is_Palindrome(word):
    trimmed_word = word.replace(" ","").lower()
    return trimmed_word == trimmed_word[::-1]

# print(is_Palindrome("lawal Lawala"))

# Write a function that accepts a list and returns a new list without duplicate values
def remove_duplicates(s):
    new_list= []

    for i in s:
        if i not in new_list:
            new_list.append(i)
    new_list.sort()
    return new_list

# print(remove_duplicates([1,2,6,4,2,6,]))

        # Alternatively
def remove_duplicates(s):
    return list(set(s))

# print(remove_duplicates([9, 9, 3,2, 2,1,1,1]))

# Write a function that accepts a list and returns a new list without duplicate values

def calculate_grade(grade):
    if grade >= 70:
        return "A"
    elif grade >= 60:
        return "B"
    elif grade >= 50:
        return "C"
    elif grade >= 45:
        return "D"
    elif grade >= 40:
        return "E"
    else:
        return "F"

# print(calculate_grade(89))


# Write a function that accepts a list of numbers and returns the sum of all element
def sum_list(num):
    sum = 0
    for i in num:
        sum += i
    return sum

# print(sum_list([10,5,7,7,6]))

# Write a function that accepts a list and returns the largest and smallest numbers
def find_min_max(number):
    max_number = max(number)
    min_number = min(number)
    return (f"maximum number is: {max_number}",
            f"minimum number is: {min_number}")

# print(find_min_max([20, 25, 10, 57, 200]))

# Write a function that accepts a list and separates even numbers from odd numbers
def seperate_number(number):
    odd_list = []
    even_list = []

    for i in number:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)    
    return odd_list, even_list
    # print(odd_list, even_list)

seperated_list = seperate_number([11,2,33,42,434,343,23,5,66])

my_dictionary = {
    "even": seperated_list[1],
    "odd": seperated_list[0]
}

# print(my_dictionary)


# Write a function that accepts two lists and combines them into one single list without duplicate

def merge_lists(num1, num2):
    set_value = set(num1).union(set(num2))
    return list(set_value)

# print(merge_lists([1,2,8,4,5], [1,2,3,4,5,]))

# Write a function that returns the total price of all products in a dictionary

my_dict = {
    "Laptop": 250000,
    "Mouse": 15000,
    "Keyboard": 29000
}

def calculate_total (my_dict):
    add = 0
    for value in my_dict.values():
        add += value
    return add

print(calculate_total(my_dict))