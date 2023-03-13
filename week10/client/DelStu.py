class DelStu:
    def __init__(self, client):
        self.client = client

    def execute(self):
        student_name = input("  Please input a student's name or exit: ")
    
        if student_name == "exit": return

        self.client.send_command("query", {'name' : student_name})
        response = self.client.wait_response()

        if response['status'] == 'OK':
            comfirm = input("  Confirm to delete (y/n): ")

            if comfirm == "y":
                self.client.send_command("delete", {"name" : student_name})
                response = self.client.wait_response()
                
                if response['status'] == 'OK':
                    print("    Delete success.")