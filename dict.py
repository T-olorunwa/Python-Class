# Create a dictionary named student
student = {
    "name": "Alice",
    "age": 21,
    "major": "Data Science"
}
# Access and print out the value associated with the key name
print(student["name"])
print(student["age"])
print(student["major"])

# Print all the keys in the dictionary
print(student.keys())

# Print all the values in the dictionary
print(student.values())

# Update the age t0 22
student["age"] = 22

# Add a new key-value pair: graduation_year: 2025
student["graduation_year"] = 2025

print(student)