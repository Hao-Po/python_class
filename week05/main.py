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
            if select_result != "exit":
                print("  No such choice!")
    
    restore_student_file(student_list)

def read_student_file():
    student_list = list()
    try:
        with open("student_list.db", "rb") as fp:
            student_list = pickle.load(fp)
    except:
        pass

    return student_list

def restore_student_file(student_list):
    with open("student_list.db", "wb") as fp:
        pickle.dump(student_list, fp)

def print_menu():
    print()
    print("add: add a student's name and score")
    print("del: delete a student")
    print("modify: modify a student's score")
    print("show: print all")
    print("exit: exit")
    selection = input("Please select: ")

    return selection

main()