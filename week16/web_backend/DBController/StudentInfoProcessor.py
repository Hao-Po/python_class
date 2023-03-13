from DBController.StudentInfoTable import StudentInfoTable
from DBController.DBConnection import DBConnection
from DBController.DBInitializer import DBInitializer

class StudentInfoProcessor:
    def __init__(self):
        pass
    
    def read_student_info(self):
        DBConnection.db_file_path = "example.db"
        DBInitializer().execute()

        students_info, subjects_info = StudentInfoTable().get_all_students()
        student_list = list()
        for student_info in students_info:
            student_dict = dict()
            student_dict['name'] = student_info['name']
            
            subject_dict = dict()
            for subject_info in subjects_info:
                if subject_info['stu_id'] == student_info['stu_id']:
                    subject_dict[subject_info['subject']] = subject_info['score']

            student_dict['scores'] = subject_dict
            student_list.append(student_dict)   
    
        return student_list