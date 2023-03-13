def main(student_list):
    name = input("  Please input a student's name: ")

    exist = False
    for student in student_list:
        if student[0] == name:
            exist = True
            break
        else:
            exist = False

    if exist:
        student_list.remove(student)
        print(f"  Del {name} success")
    else:
        print(f"    The name {name} is not found")
    return student_list