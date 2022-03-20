# Create a dictionary of students
students = {
    0: "Jake",
    1: "Anna",
    2: "Pam",
    3: "Harry",
    4: "Ellie"
}

# Get the student at index 0
# This can be done in 2 different ways
print(students[0])
print(students.get(0))

# Return all keys in the dictionary
print(students.keys())

# Return all values in the dictionary
print(students.values())

# Add another item to the dictionary
students[5] = "Fiona"

# Get all key:value pairs
print(students.items())

# Check if a key exists
if 5 in students:
    print("Yes")
else:
    print("No")

# Update dictionary by changing an item
# Updates the dictionary with items from a given argument
# If the item does not exist, the item will be added
students.update({3: "Olivia"})

# Remove an item
students.pop(5)
del students[4]

# Print all values in the dictionary
for student in students:
    print(students[student])

# Loop through both keys and values
for index, name in students.items():
    print(index, name)

# Copy a dictionary
students_copy = students.copy()
