import add_stu, del_stu, modify_stu, print_all
import re

class EXIT:
    def main(self):
        return

def main():
    ## NOTE: NO if else elif judgements are allowed in the main function !!!!
    student_list = read_student_file()
    select_result = 0

    while select_result != 4:
        # call main functions in add_stu, del_stu, modify_stu, print_all here
        try:
            select_result = print_menu()
            select_regex = re.match('[0-4]', str(select_result))
            switch = [add_stu, del_stu, modify_stu, print_all, EXIT]
            switch[int(select_regex.group())].main(student_list)
        except KeyboardInterrupt:
            print()
            print("ctrl + c, KeyboardInterrupt")
            return
        except:
            print("You need to input number 0 ~ 4")
    
    restore_student_file(student_list)

def read_student_file():
    student_list = list()
    try:
        with open("student_list.txt", "r") as fp:
            for line in fp:
                if len(line) > 0:
                    line = line.rstrip("\n").split(":")
                    student_list.append([line[0], float(line[1])])
    except:
        pass

    return student_list

def restore_student_file(student_list):
    # restore student list to file here
    try:
        with open("student_list.txt", "w") as fp:
            for student in student_list:
                fp.write(f"{student[0]}:{student[1]}\n")
    except:
        pass

def print_menu():
    print()
    print("0. Add a student's name and score")
    print("1. Delete a student")
    print("2. Modify a student's score")
    print("3. Print all")
    print("4. Exit")
    selection = int(input("Please select: "))

    return selection

main()