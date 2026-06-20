positive=0
negetive=0
zero=0
for i in range(10):
    num=int(input("Enter a number: "))
    if num>0:
        positive+=1
    elif num<0:
        negetive+=1
    else:
        zero+=1

print("Positive numbers:", positive)
print("Negative numbers:", negetive)
print("Zeros:", zero)

#task 2
for j in range(1, 50):
    if j%3==0:
     continue
    print(j)
# task 3
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("First prime number:", num)
            break
else:
    print("No prime number found in the given range.")
# task 4
marks = []

for i in range(5):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("\nHighest Mark:", highest)
print("Lowest Mark:", lowest)
print("Average Mark:", average)

print("Students scoring above average:")
for mark in marks:
    if mark > average:
        print(mark)
#task 5
student = {
    "Student Name": "Rahul",
    "Roll Number": 101,
    "Marks": 85
}

# Add Grade
student["Grade"] = "A"

# Update Marks
student["Marks"] = 90

# Display all keys and values
print("Student Record:")
for key, value in student.items():
    print(f"{key}: {value}")

#task 6
numbers = []

while True:
    print("\nMenu")
    print("1. Add a number")
    print("2. Display the list")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("Enter a number: "))
        numbers.append(num)
        print("Number added successfully!")

    elif choice == "2":
        print("List:", numbers)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
# task 7
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()  
#task 8
   for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# task 9
# Increasing Pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Reverse Pattern
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()