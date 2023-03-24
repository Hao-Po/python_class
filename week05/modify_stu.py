def main(student_list):
    while True:
        student_name = input("  Please input a student's name or exit: ")

        if student_name.lower() == "exit": return
        
        for student in student_list:
            if student_name == student['name']:
                print("  current subjects are " + " ".join([subject_name for subject_name in student['scores'].keys()]) + "\n")
                subject_name = input("  Please input a subject you want to change: ")

                if subject_name in student['scores'].keys():
                    try:
                        subject_score = float(input(f"  Please input {subject_name}'s new score of {student_name}: "))

                        if 100 >= subject_score >= 0:
                            student['scores'][subject_name] = subject_score
                            print(f"    Modify [{student_name}, {subject_name}, {subject_score}] success")
                        elif subject_score > 100:
                            print("  Score need to be 0 ~ 100")
                    except Exception as error:
                            print(f"    Wrong format with reason {error}, try again")
                else:
                    try:    
                        subject_score = float(input(f"  Add a new subject for {student_name}, please input {subject_name} score or < 0 for discarding the subject: "))

                        if 100 >= subject_score >= 0:
                            student['scores'][subject_name] = subject_score
                            print("  Add successfully")
                        elif subject_score > 100:
                            print("  Score need to be 0 ~ 100")
                    except Exception as error:
                        print(f"    Wrong format with reason {error}, try again")
                return

        print(f"    The name {student_name} is not found")