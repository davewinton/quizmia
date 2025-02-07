import json
import random
import tabulate

SETS = {"A+ - General 1" : "./data/a_test_1.json"}
SET_KEYS = list(SETS.keys())
SET_SIZE = [x for x in range(0, len(SET_KEYS))]
SET_DATA = list(zip(SET_SIZE, SET_KEYS))
ANS_IDX  = [0,1,2,3]
INITIAL_SET = "./data/a_test_1.json"

# Setup scoreboard
attempts = 0
correct = 0

def load_question_set(filepath: str) -> list:
    """ Loads a question set from json files in /data """
    try:
        with open(filepath, encoding="utf-8") as json_data:
            return json.load(json_data)
    except FileNotFoundError:
        print(f"Error: Question set file not found: {filepath}")
        return []

def shuffle_question_set(question_set: list) -> list:
    """ Randomises the order of questions """
    shuffled = question_set[:]
    random.shuffle(shuffled)
    return shuffled

def display_question(question_data: dict):
    """ Display the """
    question = question_data["question"]
    options = question_data["options"]
    print(f"\n{question}")

    print(tabulate.tabulate(list(zip(ANS_IDX, options)), headers=["Index", "Answer"], tablefmt="simple_grid"))

def get_user_answer(options: list) -> str:
    """ Main user interface after question has been displayed """
    # Show the other options and then prompt for user input
    print("[c]: Change question set")
    print("[p]: Pass")
    print("[q]: Quit")

    # Validate input
    while True:
        user_input = input("Answer (enter index): ").strip()
        if user_input.lower() in ("c", "p", "q"):
            return user_input.lower()
        try:
            user_answer = int(user_input)
            if 0 <= user_answer < len(options):
                return str(user_answer)
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid option.")

def display_results(correct: int, attempts: int):
    """ Displays the correct and attempted guesses and percentage """

    percent = round((correct / attempts) * 100) if attempts else 0
    print("\n=== RESULTS ===")
    print(f"[{correct}/{attempts}] Correct answers ({percent}%)")

def choose_question_set():
    # Display the question sets for user to select from
    print(tabulate.tabulate(SET_DATA, headers=["Option", "Question Set"], tablefmt="simple_grid"))
    print("[b]: Go back to questions")

    # Get the user input and validate then handle if "b", otherwise update the question set
    user_input = input("Answer (enter index): ").strip()
    if user_input.lower() == "b":
        return None
    try:
        user_input_int = int(user_input)                # Get the user choice
        selected_set_name = SET_KEYS[user_input_int]    # Gets the right set key based on index
        selected_set_path = SETS[selected_set_name]     # Set the set path from SETS[key]
        print(f"Loaded: {selected_set_name}")
        return selected_set_path                        # Return str path
    except (ValueError, IndexError):
        print("Invalid input.")
        return None                                     # Return None if invalid

def check_answer(question_data: dict, user_answer: str) -> bool:
    # TODO: FIX THIS
    options = question_data["options"]
    correct_answers = set(question_data["answer"])
    try:
        user_answer_index = int(user_answer)
        return options[user_answer_index] in correct_answers
    except (ValueError, IndexError):
        return False

def handle_quit():
    return True  # Signal to exit the quiz

def handle_change_set():
    new_set_path = choose_question_set()
    if new_set_path:
        new_question_set = load_question_set(new_set_path)
        if new_question_set:
            return shuffle_question_set(new_question_set)
        print("Failed to load new set.")
    return None  # Indicate no change

def handle_pass():
    global attempts
    attempts += 1
    print("Passing on this question.\n")
    return True  # Continue to next question

def handle_answer(question_data, user_answer):
    global attempts, correct
    attempts += 1
    if check_answer(question_data, user_answer):
        print("[+] Correct!\n")
        correct += 1
        return True  
    print("[!] Incorrect. Try again.")
    return False 

def run_quiz(initial_set_path: str):

    # Load the question set
    current_question_set = load_question_set(initial_set_path)
    if not current_question_set:
        print("[!] Error: could not load question set")
        return
    
    # Shuffle the question order
    current_question_set = shuffle_question_set(current_question_set)

    # Start the game loop with the question set
    while current_question_set:
        question_data = current_question_set.pop(0)
        display_question(question_data)

        while True:
            user_answer = get_user_answer(question_data["options"])

            if user_answer == "q":
                quit_quiz = handle_quit()
                if quit_quiz:
                    break

            elif user_answer == "c":
                new_question_set = handle_change_set()
                if new_question_set:
                    current_question_set = new_question_set
                    break  # Restart with new set
                display_question(question_data)

            elif user_answer == "p":
                if handle_pass():
                    break

            else:
                if handle_answer(question_data, user_answer):
                    break  # Move to next question

        if user_answer == "q":
            break  # Exit the quiz

    display_results(correct, attempts)

print("QuizMIA - Your terminal quizmaster")
print("Loading questions.. ")

if __name__ == "__main__":
    run_quiz(INITIAL_SET)
