def main(student_list):
    student_name = input("  Please input a student's name or exit: ")
    
    if student_name == "exit": return

    if student_name in student_list:
        del student_list[student_name]
        print(f"    Del {student_name} success") 
    else:
        print(f"    The name {student_name} is not found")