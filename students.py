from student_details_structure import Student

student_list = [
    Student("Ömer", "Taşcı", 1, "Turkish", "10-01-2024", ["Computer Engineering"]),
    Student("Lord", "Voldemort", 2, "British", "15-02-1992", ["Dark arts"]),
    Student("John", "Doe", 3, "American", "20-03-2024", ["Management"])
]

def add_student(first_name, last_name, index_number, nationality, starting_date, courses):
    new_student = Student(first_name, last_name, index_number, nationality, starting_date, courses)
    student_list.append(new_student)

def display_student_info():
    for student in student_list:
        print(f"Name: {student.first_name} Index Number: {student.index_number}")

add_student("stu","dent",4,"Ugandan","01-01-1860","Managment")

display_student_info()