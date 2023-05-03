import random
from game_data import data
from art import logo, vs
from os import system as sys

# globar variables used to work with dictionaries data
NAME = "name"
DESC = "description"
F_CNT = "follower_count"
CNTRY = "country"

def compare_profiles(prof1: dict, prof2: dict):
    """Function compares profiles followers count and returns 1 if frist profiles has more followers, or it returns 2 if second profile has more followers."""

    if prof1[F_CNT] > prof2[F_CNT]:
        return 1
    
    else:
        return 2

def display(prof1: dict, prof2: dict):
    """Function displays informations about compared profiles."""
    print(f"Compare A: {prof1[NAME]}, a {prof1[DESC]}, from {prof1[CNTRY]}.")
    print(vs)
    print(f"Compare B: {prof2[NAME]}, a {prof2[DESC]}, from {prof2[CNTRY]}.")


def higher_lower_game(help: bool = False):
    """Function allows user to play higher lower game. The game is about guessing which one of two Instagam profiles has more followers. If player guess right they continue and increase
    their good answers score, but if they guess wrong they lose."""

    # creating list with not already compared - numbers of list cells that stores dictionaries with profile informations
    not_picked = []
    for count, _ in enumerate(data):
        not_picked.append(count)

    # picking two first profiles
    choice_1 = random.choice(not_picked)
    c_prof_1 = data[choice_1]   # current profile 1
    not_picked.remove(choice_1)

    choice_2 = random.choice(not_picked)
    c_prof_2 = data[choice_2]
    not_picked.remove(choice_2)

    # variables used in loop condition
    wrong_answer = False
    good_answer_counter = 0

    sys("cls")
    # main loop
    while wrong_answer is False and good_answer_counter < len(data) - 1:

        # printing logo
        print(logo)

        # communication with player
        if good_answer_counter > 0:
            print("You are right!")
            
        print(f"Your current score is: {good_answer_counter}.\n")

        # infromation display
        display(c_prof_1, c_prof_2)

        # checking which profile has more followers
        more_followers = compare_profiles(c_prof_1, c_prof_2)

        # communication with player if condition is met
        if help is True:
            print(f"More followers has: {more_followers}!")

        # taking decision from player
        decision = input("\nWho has more followers? Type \"A\" or \"B\": ")

        # based on decision correctness player gets +1 good answer score and moves on to next choice or loses game
        if decision == "A" and more_followers == 1:
            good_answer_counter += 1
        
        elif decision == "A" and more_followers == 2:
            wrong_answer = True

        elif decision == "B" and more_followers == 2:
            good_answer_counter += 1
        
        elif decision == "B" and more_followers == 1:
            wrong_answer = True

        # if player asnwer was correct profile 2 becomes profile 1, and another profile from not already compared profiles is selected to become profile 2
        if wrong_answer is False:
            c_prof_1 = c_prof_2
            
            choice_2 = random.choice(not_picked)
            c_prof_2 = data[choice_2]
            not_picked.remove(choice_2)
        
        sys("cls")
    
    # communication with player
    print("Game is over!")

    if wrong_answer is True:
        print(f"You lose. Your good answer score is: {good_answer_counter}.")
    
    else:
        print("You WIN!")
    
    # oportunity to start another game
    next_game = input("Do You want to play another game? Type \"yes\" or \"no\": ")
    if next_game == "yes":
        higher_lower_game()
    
if __name__ == "__main__":
    higher_lower_game()