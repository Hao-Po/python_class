class DelStu:
    def __init__(self, student_list):
        self.student_list = student_list

    def execute(self):
        student_name = input("  Please input a student's name or exit: ")
    
        if student_name == "exit": return self.student_list

        if student_name in self.student_list:
            del self.student_list[student_name]
            print(f"    Del {student_name} success") 
        else:
            print(f"    The name {student_name} is not found")
        
        return self.student_list