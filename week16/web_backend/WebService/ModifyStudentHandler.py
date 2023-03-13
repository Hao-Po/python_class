import tornado.web
import json
from DBController.StudentInfoTable import StudentInfoTable
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer


class ModifyStudentHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()
        
        student_name = self.get_argument('name')
        subjects_from_client = json.loads(self.get_arguments('scores_dict')[0])

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
        self.write(json.dumps(reply_msg).encode())
