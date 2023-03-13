import json

class AddStu:
    def __init__(self, message, connection, student_list):
        self.message = message
        self.connection = connection
        self.student_list = student_list

    def execute(self):
        is_exist = False
        student_name = self.message['parameters']['name']
        
        if len(self.student_list):
            for data in self.student_list:
                if data['name'] == student_name:
                    is_exist = True
        
        reply_msg = dict()
        if is_exist:
            reply_msg['status'] ='Fail'
            reply_msg['reason'] = 'The name already exists.'
        else:
            reply_msg['status'] = 'OK'            
            self.student_list.append(self.message['parameters'])
             
        self.connection.send(json.dumps(reply_msg).encode())
        return self.student_list
