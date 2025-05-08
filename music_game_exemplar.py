import os
import random


def menu():

    auth = False
    while auth == False:
        print("")
        print("Welcome to our song guessing game")
        print("")
        print("Menu")
        print("")
        print("Do you wish to;")
        print("1. Login as an existing user")
        print("2. Register a new user")
        print("3. View top scorers")
        print("4. Exit")

        print("")
        choice = int(input("Enter your choice:"))

        if choice == 2:
            registration()
        elif choice == 1:
            login()
            print("Welcome", auth_user_list[0])
            auth = True
        elif choice == 3:
            topscorers()
        elif choice == 4:
            quit()


def login():
    print("")
    print("Please enter your existing login details")
    print("")
    auth_login = False
    while auth_login == False:
        username = input("Enter your username:")
        password = input("Enter your password:")

        for line in open('players.txt', 'r').readlines():
            auth_user = line
            auth_user = auth_user.strip("\n")
            global auth_user_list
            auth_user_list = auth_user.split(", ")

            if username == auth_user_list[1]:
                if password == auth_user_list[2]:
                    auth_login = True
                    return
        os.system('clear')


def registration():
    name = input("Enter your name:")
    username = input("Enter a username:")
    password = input("Enter a password:")

    file = open("players.txt", "a")
    file.write("\n" + name + ", " + username + ", " + password)
    file.close()


def song_choice():
    file = open("questions.txt", "r")
    questions = file.readlines()
    question1 = random.choice(questions)
    question1 = question1.strip("\n")
    questionandanswer = question1.split(", ")
    file.close()
    return (questionandanswer)


def create_question(song):
    songlist = song.split(" ")
    question = ""
    for x in range(0, len(songlist)):
        word = songlist[x]
        question += word[0] + " "
    return question


def ask_question(question, songandband):
    print("Guess the title of this song")
    print(question, "by ", songandband[1])
    print("")

    answer = input("Your answer:")

    if answer.upper() == songandband[0].upper():
        return 3
    else:
        print("")
        print("Incorrect")
        print("")
        print("You have one more attempt")

        answer = input("Your answer:")

        if answer.upper() == songandband[0]:
            return 1
        else:
            return 0


def topscorers():
    file = open("scores.txt", "r")
    scores = file.read()
    scoreslist = scores.split("\n")
    top_score_list = ["", 0, "", 0, "", 0, "", 0, "", 0]
    for x in range(0, len(scoreslist)):
        tempscore = scoreslist[x]
        splitscore = tempscore.split(", ")
        if int(splitscore[1]) > int(top_score_list[1]):
            top_score_list[8] = top_score_list[6]
            top_score_list[9] = top_score_list[7]
            top_score_list[6] = top_score_list[4]
            top_score_list[7] = top_score_list[5]
            top_score_list[4] = top_score_list[2]
            top_score_list[5] = top_score_list[3]
            top_score_list[2] = top_score_list[0]
            top_score_list[3] = top_score_list[1]
            top_score_list[0] = splitscore[0]
            top_score_list[1] = splitscore[1]
        elif int(splitscore[1]) > int(top_score_list[3]):
            top_score_list[8] = top_score_list[6]
            top_score_list[9] = top_score_list[7]
            top_score_list[6] = top_score_list[4]
            top_score_list[7] = top_score_list[5]
            top_score_list[4] = top_score_list[2]
            top_score_list[5] = top_score_list[3]
            top_score_list[2] = splitscore[0]
            top_score_list[3] = splitscore[1]
        elif int(splitscore[1]) > int(top_score_list[5]):
            top_score_list[8] = top_score_list[6]
            top_score_list[9] = top_score_list[7]
            top_score_list[6] = top_score_list[4]
            top_score_list[7] = top_score_list[5]
            top_score_list[4] = splitscore[0]
            top_score_list[5] = splitscore[1]
        elif int(splitscore[1]) > int(top_score_list[7]):
            top_score_list[8] = top_score_list[6]
            top_score_list[9] = top_score_list[7]
            top_score_list[6] = splitscore[0]
            top_score_list[7] = splitscore[1]
        elif int(splitscore[1]) > int(top_score_list[9]):
            top_score_list[8] = splitscore[0]
            top_score_list[9] = splitscore[1]

    print("")
    print("TOP SCORERS")
    print("-----------")
    print("")
    print("1st - ", top_score_list[0], " - ", top_score_list[1])
    print("2nd - ", top_score_list[2], " - ", top_score_list[3])
    print("3rd - ", top_score_list[4], " - ", top_score_list[5])
    print("4th - ", top_score_list[6], " - ", top_score_list[7])
    print("5th - ", top_score_list[8], " - ", top_score_list[9])
    print("")


def add_score(name, score):
    file = open("scores.txt", "a")
    file.write("\n" + name + ", " + score)
    file.close()


def game():
    menu()

    questionscore = -1
    totalscore = 0

    while questionscore != 0:
        songandband = song_choice()
        question = create_question(songandband[0])
        questionscore = ask_question(question, songandband)
        totalscore += questionscore
        if questionscore != 0:
            print("")
            print("Well done")
            print("Your score is now:", totalscore)
            print("")

    print("")
    print("Hard luck!")
    print("You scored:", totalscore)
    add_score(auth_user_list[0], str(totalscore))
    topscorers()


game()