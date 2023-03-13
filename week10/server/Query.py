import json
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable

class Query:
    def __init__(self, server):
        self.message = server.message
        self.connection = server.connection

    def execute(self):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()

        student_name = self.message['parameters']['name']
        if StudentInfoTable().select_a_student(student_name):
            student_id = StudentInfoTable().select_a_student(student_name)
            reply_msg = {
                "status" : "OK",
                "scores" : StudentInfoTable().select_someone_subjects(student_id[0])
            }
            print(f"    Query {student_name} seccess")
        else:
            reply_msg = {
                "status" : "Fail",
                "reason" : "The name is not found."
            }
        
        self.connection.send(json.dumps(reply_msg).encode())
