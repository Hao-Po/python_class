def main(student_list):
    name = input("  Please input a student's name: ")

    exist = False
    for student in student_list:
        if student[0] == name:
            exist = True
            break

    if exist:
        print("  The student already exists")
    else:
        try:
            score = float(input(f"  Please input {name}'s score: "))
            if 0 <= score <= 100:
                name_score = [name, score]
                student_list.append(name_score)
                print(f"    Add [{name}, {score}] success")
            else:
                print("  Score need to be 0 ~ 100")
        except:
            print("  You need to input number")

    return student_list
