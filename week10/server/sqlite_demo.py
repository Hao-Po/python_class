from DBConnection import DBConnection
from DBInitializer import DBInitializer
from StudentInfoTable import StudentInfoTable


DBConnection.db_file_path = "example.db"
DBInitializer().execute()

# StudentInfoTable().insert_a_student("apple")
# StudentInfoTable().insert_a_student("Ryan")
# StudentInfoTable().insert_a_student("Ben")
# StudentInfoTable().insert_a_student("Test")

# student_id = StudentInfoTable().select_a_student("Ryan")
# print("student_id: {}".format(student_id))

# StudentInfoTable().delete_a_student(student_id)
# StudentInfoTable().update_a_subject("1", "Python", 50)

# student_id = StudentInfoTable().select_a_student('Ruby')
# print(student_id[0]['stu_id'])
# StudentInfoTable().delete_a_student(student_id[0])
# StudentInfoTable().delete_subjects(student_id[0])

# data = StudentInfoTable().select_someone_subjects(1)
# print(data)

# data = StudentInfoTable().select_a_student("Ruby")
# print(data)

# print(StudentInfoTable().select_someone_subjects(1))