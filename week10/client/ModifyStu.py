class ModifyStu:
    def __init__(self, client):
        self.client = client

    def execute(self):
        student_name = input("  Please input a student's name or exit: ")

        if student_name == "exit": return 

        self.client.send_command("query", {'name' : student_name})
        response = self.client.wait_response()

        if response['status'] == 'OK':
            print("  current subjects are " + " ".join(response['scores'].keys()) + "\n")
            try:
                subject_name = input("  Please input a subject you want to change: ")
                
                if subject_name in response['scores'].keys():
                    subject_score = float(input(f"  Please input {subject_name}'s new score of {student_name}, < 0 for canceling: "))
                    
                    if 0 <= subject_score <= 100:
                        response['scores'][subject_name] = subject_score

                        self.client.send_command("modify", {'name' : student_name, 'scores_dict' : response['scores']})
                        response = self.client.wait_response()

                        if response['status'] == 'OK':
                            print(f"    Modify [{student_name}, {subject_name}, {subject_score}] success")

                    elif subject_score > 100:
                        print("    Score only can input 0 ~ 100")                  
                else:
                    subject_score = float(input(f"  Add a new subject for {student_name}, please input {subject_name} score or < 0 for discarding the subject: "))
                    
                    if 0 <= subject_score <= 100:
                        response['scores'][subject_name] = subject_score

                        self.client.send_command("modify", {'name' : student_name, 'scores_dict' : response['scores']})
                        response = self.client.wait_response()

                        if response['status'] == 'OK':
                            print(f"    Add [{student_name}, {subject_name}, {subject_score}] success")
                    
                    elif subject_score > 100:
                            print("    Score only can input 0 ~ 100")
            except Exception as error:
                print(f"    Wrong format with reason {error}, try again")
        else:
            print(f"    The name {student_name} is not found.")