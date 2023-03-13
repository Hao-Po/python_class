import add_stu, del_stu, modify_stu, print_all
import pickle

action_list = {
    "add": add_stu.main, 
    "del": del_stu.main, 
    "modify": modify_stu.main, 
    "show": print_all.main
}

def main():
    student_list = read_student_file()
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](student_list)
        except:
            pass
    
    restore_student_file(student_list)

def read_student_file():
    student_list = dict()
    try:
        with open("student_list.txt", "rb") as fp:
            student_list = pickle.load(fp)
    except:
        pass

    return student_list

def restore_student_file(student_list):
    with open("student_list.txt", "wb") as fp:
        pickle.dump(student_list, fp)

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("del: Delete a student")
    print("modify: Modify a student's score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

main()