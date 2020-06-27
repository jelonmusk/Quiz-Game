import json
import time
from playsound import playsound
from PIL import Image
#import pillow



CATEGORY = ["Friends", "Marvel","DC", "Disney",  "Potter"]

def score_and_result(key, meta):
    actual = meta["answer"]

    if actual == meta["response"]:
        playsound('audio/Correct_Answer.mp3')
        print("--->--->question {0} is Answered Correctly \n".format(key))
        return 3
    else:
        playsound('audio/Wrong_Answer.mp3')
        print("--->-->Oops !! Wrong Answer \n")
        print("The Right Answer is {0}\n".format(actual))
        return -1


def question_pops_up(question):
    print("" + question+"\n")
    choice = int(input("Enter 1 ,2, 3,4 : \n"))
    while(True):
        if choice in range(1, 5):
            return choice
        else:
            print("Invalid choice.Enter again \n")
            choice = int(input("Enter 1 ,2, 3,4\n"))


def begin_rules(questions):
    score = 0
    playsound('audio/click1.mp3')
    print("""RULES : Rule 1 :No rules except score 3 point for each right answer and a -1 for a wrong one
          Rule 2 : Always Remember Rule 1 """)
    time.sleep(5)
    for key, meta in questions.items():
        questions[key]["response"] = question_pops_up(meta["question"])
        score += score_and_result(key, meta)

    print("\n************** FINAL SCORE ***************\n")

    playsound('audio/Claps.mp3')
    print("You score  is ", score, "out of ", (3 * len(questions)))
    try:
        img=Image.open('assets/gameover.jpg')
        img.show()
    except IOError:
        pass



def load_quiz(filename):
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)


def play_game():
    global cat
    flag = False
    try:
        print("""Enter a digit to choose from the following 5 Categories of Quizzes are:
                        1-->Friends Show
                        2-->Marvel Comic Universe
                        3-->DC Comics
                        4-->Disney World
                         5-->Harry Potter , The Boy Who Lived :\n""")
        cat = int(input())
        if cat > len(CATEGORY) or cat < 1:
            print("Invalid Response.Enter digits only from 1 to 5 to choose a category.")
            flag = True
    except ValueError as e:
        print("Invalid Response.Enter digits only from 1 to 5 to choose a category.")
        flag = True
    if not flag:
        questions = load_quiz("categories/" + CATEGORY[cat - 1] + '.json')
        begin_rules(questions)
    else:
        play_game()


def start():
    print(
        """Greetings dear Fan!! Wanna take a tour of this Ulimate Fandom quiz?? Only a die-hard fan can get a perfect score 
        Y : I'm in
        N : NAhhh , I'll pass""")

    will = input()
    if will.lower() == 'y':
        playsound('audio/click1.mp3')
        play_game()
    elif will.lower() == 'n':
        print("Cool ...wheneva you're ready buddy.")
    else:
        print("Incorrect Response. Enter y or n")
        start()


def execute():
    start()


if __name__ == '__main__':
    execute()
