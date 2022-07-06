from question_model import  Question
from data import  question_data


question_bank = []

for question in question_data:
    question_text = question['text']
    question_anwer = question['answer']
    new_question = Question(question_text,question_anwer)
    question_bank.append(new_question)


print(question_bank[0].text)

