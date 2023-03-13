def main(student_list):
    print ("\n==== student list ====\n")

    for student_name, subject in student_list.items():
        print(f"Name: {student_name}")
        for subject_name, subject_score in subject.items():
            print(f"  subject: {subject_name}, score: {subject_score}")
        print()
    
    print ("======================")
