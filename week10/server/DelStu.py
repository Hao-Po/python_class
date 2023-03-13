import json
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable

class DelStu:
    def __init__(self, server):
        self.message = server.message
        self.connection = server.connection

    def execute(self):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()        
     
        student_name = self.message['parameters']['name']
        
        student_id = StudentInfoTable().select_a_student(student_name)
        StudentInfoTable().delete_a_student(student_id[0])
        StudentInfoTable().delete_subjects(student_id[0])

        reply_msg = {
            "status" : "OK"
        }

        print(f"    Del {student_name} success")
        self.connection.send(json.dumps(reply_msg).encode())
