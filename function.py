def welcome():
    print("welcome to the program!")

welcome()    

def add_two_numbers(a,b):
    return a + b

# print(add_two_numbers(3, 5))

result = add_two_numbers(4,67)
# print(result)

def length(num):
    count = 0
    for i in num:
        count += 1
    return count    

res = length([1,2,3,])
# print(res)

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


print(calculator())