#  Pre-defined list of students
students = [
    {
        "name": "Alice",
        "grades": {
            "Math": 90,
            "Science": 85,
            "English": 78
        }
    },
    {
        "name": "Bob",
        "grades": {
            "Math": 88,
            "Science": 92,
            "English": 79
        }
    }
]

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    num_subjects = int(input("How many subjects? "))

    grades = {}  # Create an empty dictionary for grades

    # Collect subject names and grades
    for _ in range(num_subjects):  # (_) - it means i am not using any variable 
        subject = input("Enter subject name: ")
        grade = int(input(f"Enter grade for {subject}: "))
        grades[subject] = grade  # Add to the grades dictionary

    # Create new student record and add to the list
    student = {
        "name": name,
        "grades": grades
    }
    students.append(student)
    print("Student added successfully!\n")

# Step 3: Function to display all students
def display_students():
    print("----- Student Records -----")
    for i in students:
        print(f"Name: {i['name']}")
        for subject, grade in i["grades"].items():
            print(f"  {subject}: {grade}")
        print()  # Blank line between students

# Step 4: Main program flow
add_student()        # Call function to add a new student
display_students()   # Call function to print all students