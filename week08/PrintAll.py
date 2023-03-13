class PrintAll:
    def __init__(self, client):
        self.client = client
        
    def execute(self):
        self.client.send_command("show", dict())
        all_data = self.client.wait_response()

        print ("\n==== student list ====\n")

        for data in all_data['parameters']:
            print(f"Name: {data['name']}")
            for subject_name, subject_score in data['scores'].items():
                print(f"  subject: {subject_name}, score: {subject_score}")
            print()
        
        print ("======================")