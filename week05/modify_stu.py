def main(student_list):
    student_name = input("  Please input a student's name or exit: ")
    if student_name == "exit": return

    if student_name in student_list:
        print("  current subjects are " + " ".join([subject_name for subject_name in student_list[student_name]]) + "\n")
        subject_name = input("  Please input a subject you want to change: ")

        if subject_name in student_list[student_name]:
            try:
                subject_score = float(input(f"  Please input {subject_name}'s new score of {student_name}: "))

                if subject_score >= 0 :
                    student_list[student_name].update({subject_name : subject_score})
                    print(f"    Modify [{student_name}, {subject_name}, {subject_score}] success")
            except Exception as error:
                    print(f"    Wrong format with reason {error}, try again")
        else:
            subject_score = float(input(f"  Add a new subject for {student_name}, please input {subject_name} score or < 0 for discarding the subject: "))

            if subject_score >= 0 :
                student_list[student_name].update({subject_name : subject_score})
                print("  Add successfully")
    else:
        print(f"    The name {student_name} is not found")

        
            




































