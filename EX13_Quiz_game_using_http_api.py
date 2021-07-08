import requests
import json
import random
import pprint
import html
endGame=""
correct_score=0
incorrect_score=0
score=0
option=0

data_valid=False
url="https://opentdb.com/api.php?amount=1"
no_of_quest=0
while endGame!="quit":
    r=requests.get(url)
    if(r.status_code!=200):
        endGame=input("We have ancountered a problem. Press enter to try again")
    else:
        data=json.loads(r.text)
        question=data['results'][0]['question']
        answers=data['results'][0]['incorrect_answers']
        correct_answer=data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        i=1
        no_of_quest+=1
        print("\n"+html.unescape(question),"\n")
        for answer in answers:
            print(i,".",html.unescape(answer))
            i+=1
        
        while data_valid==False:
                try:
                    option=int(input("[*]Select the option:"))
                    if option < 0 or option > len(answers):
                        print("Invalid Option!Option can be selected between 1 and 4")
                    else:
                        data_valid=True
                            
                except:
                    print("Invalid Choice!Only numbers allowed")
        if answers[option-1]==correct_answer:
            print("Your answer is correct")
            score+=10
            correct_score+=1
        else:
            print("Invalid answer.The correct answer is",correct_answer)
            incorrect_score+=1
            print("######################################################")
            print("Your score is:"+str(round((score/no_of_quest),2)))
            print("Correct Answers:"+str(correct_score))
            print("Incorrect Answers:"+str(incorrect_score))
            print("######################################################")
        endGame=input("Do you want to continue?Press 'enter' to continue and 'quit' to close:").lower()
        data_valid=False
print("Thanks for playing !")
print("######################################################")
print("Your score is"+str(round((score/no_of_quest),2)))
print("######################################################")
