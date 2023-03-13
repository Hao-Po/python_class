import json

class PrintAll:
    def __init__(self, message, connection, student_list):
        self.message = message
        self.connection = connection
        self.student_list = student_list
        
    def execute(self):
        reply_msg = dict()
        reply_msg['status'] ='OK'
        reply_msg['parameters'] = self.student_list
        self.connection.send(json.dumps(reply_msg).encode())

        return self.student_list