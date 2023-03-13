from AddStu import AddStu
from PrintAll import PrintAll
from SocketServer import SocketServer
from StudentInfoProcessor import StudentInfoProcessor

action_list = {
    "add": AddStu, 
    "show": PrintAll
}

def main():
    server = SocketServer(host = "127.0.0.1", port = 20001)
    server.setDaemon(True)
    server.serve()

    student_list = list()
    student_list = StudentInfoProcessor().read_student_file()  

    while True:
        try:
            student_list = action_list[server.message['command']](server.message,
                                                                  server.connection,
                                                                  student_list).execute()
            server.message = dict()
            StudentInfoProcessor().restore_student_file(student_list)
        except KeyboardInterrupt:
            pass
        except:
            pass

main()