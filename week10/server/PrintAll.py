import json
from StudentInfoProcessor import StudentInfoProcessor

class PrintAll:
    def __init__(self, server):
        self.connection = server.connection

    def execute(self):
        student_list = StudentInfoProcessor().read_student_info()

        reply_msg = {
            "status" : "OK",
            "parameters" : student_list
        }

        self.connection.send(json.dumps(reply_msg).encode())