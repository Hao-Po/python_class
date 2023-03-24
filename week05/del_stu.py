def main(student_list):
    student_name = input("  Please input a student's name or exit: ")
    
    if student_name == "exit": return

    for student in student_list:
        if student_name == student["name"]:
            student_list.remove(student)
            print(f"    Del {student_name} success") 
            return
    
    print(f"    The name {student_name} is not found")








