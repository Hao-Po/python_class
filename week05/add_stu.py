def main(student_list):
    while True:
        student_name = input("  Please input a student's name or exit: ")

        if student_name.lower() == "exit": return
        
        exist = False
        for student in student_list:
            if student_name == student['name']:
                exist = True

        if not exist:
            student = dict()
            student['name'] = student_name
            student['scores'] = dict()

            while True:
                subject_name = input("  Please input a subject name or exit for ending: ")
                if subject_name not in student['scores'].keys():
                    if subject_name == "exit":
                        student_list.append(student)
                        return
                else:
                    print(f"    {subject_name} already exists")
                    continue

                flag = True
                while flag == True:
                    try:
                        subject_score = float(input(f"  Please input {student_name}'s {subject_name} score < 0 for discarding the subject: "))
                        if 100 >= subject_score >= 0:
                            student["scores"].update({subject_name : subject_score})
                            flag = False
                        elif subject_score > 100:
                            print("  Score need to be 0 ~ 100")
                        else:
                            break
                    except Exception as error:
                        print(f"    Wrong format with reason {error}, try again")
                        flag = True
        else:
            print(f"    {student_name} already exists")