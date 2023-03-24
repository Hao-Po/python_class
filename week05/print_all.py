def main(student_list):
    print ("\n==== student list ====\n")

    for student in student_list:
        print(f"Name :{student['name']}")
        for subject_name, subject_score in student["scores"].items():
            print(f"  subject:{subject_name}, score:{subject_score}")
        print()
  
    print ("======================")
