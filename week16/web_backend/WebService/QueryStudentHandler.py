import tornado.web
import json
from DBController.StudentInfoTable import StudentInfoTable
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer


class QueryStudentHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()

        student_name = self.get_argument("name")

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
        
        self.write(json.dumps(reply_msg).encode())
        
