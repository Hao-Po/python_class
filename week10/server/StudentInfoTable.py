from DBConnection import DBConnection

class StudentInfoTable:
    def insert_a_student(self, name):
        command = "INSERT INTO student_info (name) VALUES  ('{}');".format(name)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()
            return cursor.lastrowid

    def select_a_student(self, name):
        command = "SELECT * FROM student_info WHERE name='{}';".format(name)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return [row['stu_id'] for row in record_from_db]

    def delete_a_student(self, stu_id):
        command = "DELETE FROM student_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def update_a_subject(self, stu_id, subject_name, score):
        command = "UPDATE subject_info SET score='{}' WHERE stu_id='{}' and subject='{}';".format(score, stu_id, subject_name)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def get_all_students(self):
        get_all_studentInfo = "SELECT * FROM student_info"
        get_all_subjectInfo = "SELECT * FROM subject_info"

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(get_all_studentInfo)
            record_from_db_students = cursor.fetchall()
            cursor.execute(get_all_subjectInfo)
            record_from_db_subjects = cursor.fetchall()

        return record_from_db_students, record_from_db_subjects

    def insert_a_subject(self, stu_id, subject, score):
        command = "INSERT INTO subject_info (stu_id, subject, score) VALUES ('{}','{}','{}');".format(stu_id, subject, score)
            
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def delete_subjects(self, stu_id):
        command = "DELETE FROM subject_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()

    def select_someone_subjects(self, stu_id):
        command = "SELECT * FROM subject_info WHERE stu_id='{}';".format(stu_id)

        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            record_from_db = cursor.fetchall()

        return {row['subject']:row['score'] for row in record_from_db}