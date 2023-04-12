import requests
def get_questions():
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    question_data = []


    questions = requests.get("https://opentdb.com/api.php", params=parameters)
    questions = questions.json()

    for question in questions["results"]:
        question_data.append(question)


    return question_data

