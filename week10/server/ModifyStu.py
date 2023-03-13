import json
from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable

class ModifyStu:
    def __init__(self, server):
        self.message = server.message
        self.connection = server.connection

    def execute(self):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()
        
        student_name = self.message['parameters']['name']
        subjects_from_client = self.message['parameters']['scores_dict']

        student_id = StudentInfoTable().select_a_student(student_name)
        subjects_from_db = StudentInfoTable().select_someone_subjects(student_id[0]).keys()

        for subject_name, score in subjects_from_client.items():
            if subject_name in subjects_from_db:
                StudentInfoTable().update_a_subject(student_id[0], subject_name, score)
            else:
                StudentInfoTable().insert_a_subject(student_id[0], subject_name, score)

        reply_msg = {
            "status" : "OK"
        }
        
        print(f"    Modify {student_name} success")
        self.connection.send(json.dumps(reply_msg).encode())
