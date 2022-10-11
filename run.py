# import gspread
# from google.oauth2.service_account import Credentials


# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]


# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('quiz_game')

# -------------------------
print("Do you think you are the expert in NBA?")
print("-------------------------")
print("The quiz has _ questions about NBA")
print("-------------------------")
print("If you still feel confident, please follow the steps below:")
print("-------------------------")

username = input("Type in your name and press return: ")

age = int(input("Please enter your age: "))

days = 365 * age

print("Hello " + username + ", you've been alive for:" + str(days) + " days")
# -------------------------
# This is the main function which will run the quiz


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
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
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*10)
    print("Your score is: "+str(score))

# -------------------------


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------
# These are the quiz questions and answers


questions = {
    "Who has the most assists in a single NBA game?: ": "D",
    "Who has Fastest foul out in nba history?: ": "A",
    "Who has the most Blocks in NBA history?: ": "C",
    "Who has the most games in NBA history?: ": "B"
}
# These are the quiz options
options = [
    ["A. J.Stockton", "B. M.Johnson", "C. L.Wilkens", "D. S.Skiles"],
    ["A. B.Wells", "B. R.Wallace", "C. D.Rodman", "D. A.Gilmore"],
    ["A. D.Mutombo", "B. Kareem", "C. H.Olajuwon", "D. T.Duncan"],
    ["A. D.Nowitzki", "B. R.Parish", "C. V.Carter", "D. Kareem"]]


new_game()

while play_again():
    new_game()

print("BYE!")

# -------------------------
