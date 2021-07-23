import requests
import json

class QuestionBank:
    def __init__(self) -> None:
        self.url = "https://opentdb.com/api.php?amount=5&difficulty=easy&type=multiple"
    
    def get_questions(self):

        resp = requests.get(self.url)
        data_dict = json.loads(resp.text)
        return data_dict['results']
