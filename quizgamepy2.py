import json
import time
from playsound import playsound
from PIL import Image
# noinspection PyUnresolvedReferences
import tkinter
import random
import sys
import os

#sys.setrecursionlimit(10000)


CATEGORY = ["Friends", "Marvel", "DC", "Disney", "Potter"]
score = 0



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


def score_and_result(key, meta):
    actual = meta["answer"]

    if actual == meta["response"]:
        playsound('audio/Correct_Answer.mp3')
        head.config(font=("Helvetica", 14), fg="#CD5C5C",
                    pady=10, bd=15, bg="#F7FB6D", anchor=tkinter.CENTER, justify=tkinter.CENTER, relief=tkinter.RAISED,
                    text="--->--->question {0} is Answered Correctly \n".format(key))

        return 3
    else:
        playsound('audio/Wrong_Answer.mp3')
        head.config(font=("Helvetica", 14), fg="#CD5C5C",
                    pady=10, bd=15, bg="#F7FB6D", anchor=tkinter.CENTER, justify=tkinter.CENTER, relief=tkinter.RAISED,
                    text="--->-->Oops !! Wrong Answer \n The Right Answer is {0}\n".format(actual))
        return -1


def question_pops_up(question):
    head.config(font=("Helvetica", 14), fg="#CD5C5C",
                pady=10, bd=15, bg="#F7FB6D", anchor=tkinter.CENTER, justify=tkinter.CENTER, relief=tkinter.RAISED,
                text="Enter 1 ,2, 3,4 : \n")
    label.config(bg="#A3E4D7", font=('Helvetica', 14), text="" + question + "\n")
    a.focus_set()
    while (True):
        if a in range(1, 5):
            return a
        else:
            head.config(font=("Helvetica", 14), fg="#CD5C5C",
                        pady=10, bd=15, bg="#F7FB6D", anchor=tkinter.CENTER, justify=tkinter.CENTER,
                        relief=tkinter.RAISED,
                        text="Invalid choice.Enter again \n Enter 1 ,2, 3,4\n")
            a.focus_set()


def begin_rules(questions):
    score = 0
    playsound('audio/click1.mp3')
    head.config(bg="#A3E4D7", font=('Helvetica', 14), text="""RULES : Rule 1 :No rules except score 3 point for each right answer and a -1 for a wrong one
          Rule 2 : Always Remember Rule 1 """)
    time.sleep(5)
    for key, meta in questions.items():
        questions[key]["response"] = question_pops_up(meta["question"])
        score += score_and_result(key, meta)
        scorelbl.config(text=str(score))
        a.delete(0, tkinter.END)

    head.config(bg="#A3E4D7", font=('Helvetica', 14), text="\n************** FINAL SCORE ***************\n")

    playsound('audio/Claps.mp3')
    head.config(bg="#A3E4D7", font=('Helvetica', 14),
                text="You score  is " + str(score) + "out of " + str((3 * len(questions))))

    gameOverlbl = tkinter.Label(window, text="GAME OVER. PRESS RESTART TO TRY AGAIN",
                                font=("Helvetica", 14),
                                fg="#CD5C5C", bg="#A3E4D7").pack()
    # restart button
    tkinter.Button(window, text="Restart", command=restart_program).pack()
    try:
        img = Image.open('assets/gameover.jpg')
        img.show()
    except IOError:
        pass


def load_quiz(filename):
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)


def play_game():

    flag = False
    try:
        a.focus_set()

        head.config(text="""Enter a digit to choose from the following 5 Categories of Quizzes are:
                        1-->Friends Show
                        2-->Marvel Comic Universe
                        3-->DC Comics
                        4-->Disney World
                         5-->Harry Potter , The Boy Who Lived :\n""")


        if a.get() > 'len(CATEGORY)' or a.get() < '1':
            label.config(text="yo!")
            head.config(bg="#A3E4D7", font=('Helvetica', 14),
                        text="Invalid Response.Enter digits only from 1 to 5 to choose a category.")
            flag = True
    except ValueError as e:

        head.config(bg="#A3E4D7", font=('Helvetica', 14),
                    text="Invalid Response.Enter digits only from 1 to 5 to choose a category.")
        flag = True
    if not flag:
        a.delete(0, tkinter.END)
        questions = load_quiz("categories/" + CATEGORY[a - 1] + '.json')
        begin_rules(questions)
    else:
        a.delete(0, tkinter.END)
        #play_game()
        label.config(text="bye")


def start(event):
    # print("""Greetings dear Fan!! Wanna take a tour of this Ulimate Fandom quiz?? Only a die-hard fan can get a perfect score  Y : I'm in N : NAhhh , I'll pass""")

    a.focus_set()
    if a.get() == 'y':
        a.delete(0, tkinter.END)
        playsound('audio/click1.mp3')

        play_game()
    elif a.get() == 'n':
        a.delete(0, tkinter.END)
        head.config(bg="#A3E4D7", font=('Helvetica', 14), text="Cool ...wheneva you're ready buddy.")
    else:
        a.delete(0, tkinter.END)
        head.config(bg="#A3E4D7", font=('Helvetica', 14), text="Incorrect Response. Enter y or n")
        #a.delete(0, tkinter.END)
        start(event)


# Window layout specifications
window = tkinter.Tk()
window.title("Quiz Game")
window.configure(bg="#F7FB6D")
window.geometry("640x480")

# title
head = tkinter.Label(window,
                    text="""Greetings Dear Fan!!\n Wanna take a tour of this Ulimate Fandom quiz?? \n Only a die-hard fan can get a perfect score.\nY : I'm in \nN : Nahhh , I'll pass""",
                    font=("Helvetica", 14), fg="#CD5C5C",
                    pady=10, bd=15, bg="#F7FB6D", anchor=tkinter.CENTER, justify=tkinter.CENTER,
                    relief=tkinter.RAISED)
head.pack()
# score heads
scorelbl = tkinter.Label(window, text="0",
                        font=("Helvetica", 14), bg="#A3E4D7", fg="#F39C12",
                        height=3, padx=4)
scorelbl.pack()


# label to display text
label = tkinter.Label(window, bg="#A3E4D7", font=('Helvetica', 50))
label.pack()

# text entry input box for answers
var = tkinter.StringVar()
a = tkinter.Entry(textvariable=var)
a.place(width=40, height=400)
window.bind('<Return>',start)
a.pack()
a.focus_set()


window.mainloop()
