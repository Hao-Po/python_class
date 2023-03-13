class ModifyStu:
    def __init__(self, student_list):
        self.student_list = student_list

    def execute(self):
        student_name = input("  Please input a student's name or exit: ")
        if student_name == "exit": return self.student_list

        if student_name in self.student_list:
            print("  current subjects are " + " ".join([subject_name for subject_name in self.student_list[student_name]]) + "\n")
            subject_name = input("  Please input a subject you want to change: ")

            if subject_name in self.student_list[student_name]:
                try:
                    subject_score = float(input(f"  Please input {subject_name}'s new score of {student_name}, < 0 for canceling: "))

                    if 0 <= subject_score <= 100:
                        self.student_list[student_name].update({subject_name : subject_score})
                        print(f"    Modify [{student_name}, {subject_name}, {subject_score}] success")
                    elif subject_score > 100:
                        print("    Score only can input 0 ~ 100")
                    else:
                        print
                except Exception as error:
                        print(f"    Wrong format with reason {error}, try again")
            else:
                try:
                    subject_score = float(input(f"  Add a new subject for {student_name}, please input {subject_name} score or < 0 for discarding the subject: "))
                    
                    if 0 <= subject_score <= 100:
                        self.student_list[student_name].update({subject_name : subject_score})
                        print("  Add successfully")
                    elif subject_score > 100:
                            print("    Score only can input 0 ~ 100")
                    else:
                        print
                except Exception as error:
                        print(f"    Wrong format with reason {error}, try again")
        else:
            print(f"    The name {student_name} is not found")

        return self.student_list