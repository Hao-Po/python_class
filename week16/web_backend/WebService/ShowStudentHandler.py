import tornado.web
import json
from DBController.StudentInfoProcessor import StudentInfoProcessor


class ShowStudentHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        student_list = StudentInfoProcessor().read_student_info()

        reply_msg = {
            "status" : "OK",
            "parameters" : student_list
        }

        self.write(json.dumps(reply_msg).encode())