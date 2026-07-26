students = []

while True:
    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("Students:", students)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
        
print("Git is awesome!")