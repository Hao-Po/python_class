from matplotlib.font_manager import json_dump
import requests
import json

def post_service():
    response = requests.post(
        url="http://127.0.0.1:9000/add_student",
        data={
            "name": 'apple',
            "scores": json.dumps({"py" : 70, "fv" : 80})
        },
        verify=False
    )

    if (response.status_code == requests.codes.ok):
        response_json = json.loads(response.text)
        print (response_json["status"])
    else:
        print("Fail")

post_service()