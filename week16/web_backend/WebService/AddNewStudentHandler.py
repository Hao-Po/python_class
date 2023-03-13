import tornado.web
import json
from DBController.StudentInfoTable import StudentInfoTable
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer

class AddNewStudentHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()

        student_name = self.get_argument('name')
        subjects = json.loads(self.get_arguments('scores')[0])

        student_id = StudentInfoTable().insert_a_student(student_name)
        for subject_name, score in subjects.items():
            StudentInfoTable().insert_a_subject(student_id, subject_name, score)

        reply_msg = {
            "status" : "OK"
        }         
        
        self.write(json.dumps(reply_msg).encode())