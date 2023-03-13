class AddStu:
    def __init__(self, student_list):
        self.student_list = student_list

    def execute(self):
        while True:
            student_name = input("  Please input a student's name or exit: ")

            if student_name == "exit": return self.student_list

            if student_name not in self.student_list:
                self.student_list.update({student_name : dict()})

                while True:
                    subject_name = input("  Please input a subject name or exit for ending: ")
                    if subject_name not in self.student_list[student_name]:
                        if subject_name == "exit":
                            if self.student_list[student_name]:
                                print(f"    Add {student_name}'s score successfully")
                            return self.student_list
                    else:
                        print(f"    {subject_name} already exists")
                        continue

                    flag = True
                    while flag == True:
                        try:
                            subject_score = float(input(f"  Please input {student_name}'s {subject_name} score < 0 for discarding the subject: "))
                            if 0 <= subject_score <= 100:
                                self.student_list[student_name].update({subject_name : subject_score})
                                flag = False
                            elif subject_score > 100:
                                print("    Score only can input 0 ~ 100")
                                break
                            else:
                                break
                        except Exception as error:
                            print(f"    Wrong format with reason {error}, try again")
                            flag = True
            else:
                print(f"    {student_name} already exists")