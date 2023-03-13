from AddStu import AddStu
from PrintAll import PrintAll
from SocketClient import SocketClient

action_list = {
    "add": AddStu, 
    "show": PrintAll
}

def main():
    select_result = "initial"

    client = SocketClient(host = "127.0.0.1", port = 20001)
    
    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client).execute()
        except:
            pass
    
    client.client_socket.close()

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection

main()