import tornado.web
import json
from DBController.StudentInfoTable import StudentInfoTable
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer


class DeleteStudentHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()        
     
        student_name = self.get_argument('name')
        
        student_id = StudentInfoTable().select_a_student(student_name)
        StudentInfoTable().delete_a_student(student_id[0])
        StudentInfoTable().delete_subjects(student_id[0])

        reply_msg = {
            "status" : "OK"
        }

        print(f"    Del {student_name} success")
        self.write(json.dumps(reply_msg).encode())
