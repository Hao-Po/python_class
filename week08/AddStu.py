class AddStu:
    def __init__(self, client):
        self.client = client
        self.student_list = dict()

    def execute(self):
        try:
            student_name = input("  Please input a student's name or exit: ")

            if student_name == "exit": return

            self.student_list['name'] = student_name
            self.student_list['scores'] = dict()

            while True:
                subject_name = input("  Please input a subject name or exit for ending: ")
                if subject_name not in self.student_list['scores'].keys():
                    if subject_name == "exit":
                        self.client.send_command("add", self.student_list)
                        all_data = self.client.wait_response()
                        
                        if all_data['status'] == 'OK':
                            print(f"    Add{self.student_list} success")
                        else:
                            print(f"    Add{self.student_list} fail")
                        return self.student_list

                    flag = True
                    while flag == True:
                        try:
                            subject_score = float(input(f"  Please input {student_name}'s {subject_name} score < 0 for discarding the subject: "))
                            if 0 <= subject_score <= 100:
                                self.student_list['scores'].update({subject_name : subject_score})
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
                    print(f"    Subject {subject_name} already exists.")
        except Exception as error:
            print(f"    {error}")