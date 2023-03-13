from AddStu import AddStu
from PrintAll import PrintAll
from DelStu import DelStu
from ModifyStu import ModifyStu
from Query import Query
from SocketServer import SocketServer

action_list = {
    "add": AddStu, 
    "modify" : ModifyStu,
    "delete" : DelStu,
    "show": PrintAll,
    "query" : Query
}

def main():
    server = SocketServer(host = "127.0.0.1", port = 20001)
    server.setDaemon(True)
    server.serve()

    while True:
        try:
            action_list[server.message['command']](server).execute()
            server.message = dict()
        except KeyboardInterrupt:
            pass
        except:
            pass

main()