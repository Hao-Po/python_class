import json
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable

class AddStu:
    def __init__(self, server):
        self.message = server.message
        self.connection = server.connection

    def execute(self):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()

        student_name = self.message['parameters']['name']
        subjects = self.message['parameters']['scores']
            
        student_id = StudentInfoTable().insert_a_student(student_name)
        for subject_name, score in subjects.items():
            StudentInfoTable().insert_a_subject(student_id, subject_name, score)

        reply_msg = {
            "status" : "OK"
        }         
        
        self.connection.send(json.dumps(reply_msg).encode())
    