def main(student_list):
    name = input("  Please input a student's name: ")

    exist = False
    for student in student_list:
        if student[0] == name:
            exist = True
            break

    if exist:
        try:
            new_score = float(input(f"  Please input {name}'s new score: "))
            if 0 <= new_score <= 100:
                student[1] = new_score
                print(f"    Modify [{name}, {new_score} success]")
            else:
                print("  Score need to be 0 ~ 100")
        except:
            print("  You need to input number")
    else:
        print(f"    The name {name} is not found")

    return student_list
