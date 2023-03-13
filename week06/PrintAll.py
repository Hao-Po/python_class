class PrintAll:
    def __init__(self, student_list):
        self.student_list = student_list
        
    def execute(self):
        print ("\n==== student list ====\n")

        for student_name, subject in self.student_list.items():
            print(f"Name: {student_name}")
            for subject_name, subject_score in subject.items():
                print(f"  subject: {subject_name}, score: {subject_score}")
            print()
        
        print ("======================")

        return self.student_list