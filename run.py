import os
import time
import pyfiglet
import colorama
from colorama import Fore
from data import QUESTIONS, OPTIONS
colorama.init(autoreset=True)


def clear():
    """
    This function clears the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


clear()

# welcome menu
banner = pyfiglet.figlet_format("NBA QUIZ GAME!!")
print(banner)
print("Do you think you are the expert in NBA?")
print("-------------------------")
print(f"The quiz has {len(QUESTIONS)} questions about NBA")
print("-------------------------")
print("If you still feel confident, please follow the steps below:")
print("-------------------------")


def check_username():
    """
    This function checks the user enters a valid alpha username
    """
    while True:
        username = input("Type in your name and press enter: ")
        if username.isalpha():
            print("Hello " + username + ", lets see how good you are!")
            new_game()
            break
        clear()
        print(f"{Fore.RED}{username} is not valid. try again")


def check_input():
    """
    This function checks the user enters a valid choice
    """
    while True:
        guess = input(
            f"Enter ({Fore.CYAN}A{Fore.WHITE}, "
            f"{Fore.CYAN}B{Fore.WHITE}, {Fore.CYAN}C{Fore.WHITE}, or "
            f"{Fore.CYAN}D{Fore.WHITE}): ").upper()
        choices = ['A', 'B', 'C', 'D']
        if guess in choices:
            return guess
        print(f"{Fore.RED}{guess} is not valid. try again")


def new_game():
    """
    This is the main function which will run the quiz
    """
    clear()
    guesses = []
    correct_guesses = 0
    question_num = 1

    for index, key in enumerate(QUESTIONS):
        print("-------------------------")
        print(f" {Fore.YELLOW}QUESTION # {index + 1} of {len(QUESTIONS)}")
        print("-------------------------")

        print(key)
        for i in OPTIONS[question_num-1]:
            print(f"{Fore.CYAN}{i}")
        guess = check_input()
        clear()
        guesses.append(guess)
        correct_guesses += check_answer(QUESTIONS.get(key), guess)
        question_num += 1
        time.sleep(0.5)

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    """
    This function will check if the answer is correct or not
    """
    if answer == guess:
        print(f"{Fore.GREEN}CORRECT!")
        return 1
    else:
        print(f"{Fore.RED}WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    """
    This function will compile all the awswers and give a final result
    """
    time.sleep(1)
    clear()
    print("calculating results...")
    time.sleep(1)
    clear()
    print("-------------------------")
    print(f"{Fore.YELLOW}RESULTS")
    print("-------------------------")

    # grab the question's values
    ANSWERS = [*QUESTIONS.values()]
    # zip the results of correct answers with user's guesses
    results = zip(ANSWERS, guesses)
    # print all correct answers
    print("Answers: ", end="")
    for a in ANSWERS:
        print(f"{Fore.CYAN}{a}", end=" ")
    print()
    # print the user's guesses
    print("Guesses: ", end="")
    for q, g in results:
        if (g == q):
            # user guessed correctly
            print(f"{Fore.GREEN}{g}", end=" ")
        else:
            # user guessed wrong
            print(f"{Fore.RED}{g}", end=" ")
    print("\n")


# total questions guessed correct


score = int((correct_guesses/len(QUESTIONS))*100)
print(f"You scored : {Fore.CYAN}{correct_guesses} out of {len(QUESTIONS)}")
# percentage of correctly guessed answers
print(f"Your score is: {Fore.CYAN}{str(score)}%\n")


def play_again():
    """
    This funcion will ask the player if they want to play again
    """
    while True:
        response = input(
            f"Do you want to play again? "
            f"({Fore.GREEN}yes{Fore.WHITE} or "
            f"{Fore.RED}no{Fore.WHITE}): ").upper()
        choices = ["YES", "NO"]
        if response in choices:
            if response == "YES":
                return True
            else:
                return False
        else:
            clear()
            print(
                f"{Fore.RED}{response} "
                "Is not a valid option, please try again")


check_username()

while play_again():
    new_game()

print("BYE!")
