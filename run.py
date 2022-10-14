import os
from data import QUESTIONS, OPTIONS


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

# -------------------------
print("Do you think you are the expert in NBA?")
print("-------------------------")
print(f"The quiz has {len(QUESTIONS)} questions about NBA")
print("-------------------------")
print("If you still feel confident, please follow the steps below:")
print("-------------------------")


def check_username():
    while True:
        username = input("Type in your name and press enter: ")
        if username.isalpha():
            print("Hello " + username + ", lets see how good you are!")
            new_game()
            break
        clear()
        print(f"{username} is not valid. try again")


# -------------------------
def check_input():

    while True:
        guess = input("Enter (A, B, C, or D): ").upper()
        choices = ['A', 'B', 'C', 'D']
        if guess in choices:
            return guess
        print(f"{guess} is not valid. try again")


# This is the main function which will run the quiz
def new_game():
    clear()
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in QUESTIONS:
        print("-------------------------")
        print(key)
        for i in OPTIONS[question_num-1]:
            print(i)
        guess = check_input()
        clear()
        guesses.append(guess)
        correct_guesses += check_answer(QUESTIONS.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in QUESTIONS:
        print(f"{QUESTIONS.get(i)}", end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(f"{i}", end=" ")
    print()

    score = int((correct_guesses/len(QUESTIONS))*100)
    print(f"You scored : {correct_guesses} out of {len(QUESTIONS)}")
    print(f"Your score is: {str(score)}%")

# -------------------------


def play_again():
    while True:
        response = input("Do you want to play again? (yes or no): ").upper()
        choices = ["YES", "NO"]
        if response in choices:
            return True
        else:
            return False
# -------------------------
# These are the quiz questions and answers


check_username()

while play_again():
    new_game()

print("BYE!")

# -------------------------
