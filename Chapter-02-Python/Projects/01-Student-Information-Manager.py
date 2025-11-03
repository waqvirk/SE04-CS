# Menu System
print("\nWelcome to Student Information Manager\n")
print("1. Add Student")
print("2. View All Students")
print("3. Search Student")
print("4. Show Statistics")
print("5. Exit\n")

menu_selection = input("Enter the number 1-5: ")
if menu_selection != range[1:5]:
    ValueError("not right number")


# Step 1: Add Student
student1 = {"name" : "John Doe",
      "age" : 25,
      "courses" : ("math", "science")}
student2 = {"name" : "Christopher Andrew",
      "age" : 27,
      "courses" : ("french", "science")}
student3 = {"name" : "Harvey Dent",
      "age" : 23,
      "courses" : ("science", "history")}

# Step 2: View All Students
# students_list = [student1["name"], student2["name"], student3["name"]]
# print(students_list)
# courses_set = {student1["courses"],student2["courses"], student3["courses"]}
# print(courses_set)
# Step 3: Search Students
# Step 4: Show Statistics
# Step 5: Exit
