import random


# Functions go here
def check_rounds():
    while True:
        response = input("how many rounds do you want to play ? ")

        round_error = "please type either <enter> or an integer that is more 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

                # output error if item nt in list

        print(error)
        print()


def show_help():
    print("""

How to Play...

Choose rock / paper or scissors etc

    """)

# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes","no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

game_summary = []

# Ask user if they have played before.
show_instructions = choice_checker("Do you want to see the instructions?",
                                   yes_no_list,
                                   "Please answer yes or no")
if show_instructions == "yes":
    show_help()


# ask user for # of rounds then loop...
rounds_played = 0
rounds_won = 0
rounds_drawn = 0

mode = "regular"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5

end_game = "no" 
while end_game == "no":

    # Rounds Heading
    print()
    if mode == "infinite":

        rounds += 1

        headings = "continue mode: round {}".format(rounds_played + 1)
    else:
        headings = "round {} of {}".format(rounds_played + 1, rounds)

    print(headings)
    choose_instruction = "Choose Rock / Paper / Scissors"
    choose = choice_checker(choose_instruction, rps_list, "Please enter r / p / s")

    if rounds_played == rounds - 1:
        end_game = "yes"

    if choose == "xxx":
        break

    comp_choice = random.choice(rps_list[:-1])

    # rest of loop / game
    if choose == comp_choice:
        result = "tie"
        rounds_drawn += 1
    elif choose == "rock" and comp_choice == "paper":
        result = "loss"
    elif choose == "paper" and comp_choice == "scissors":
        result = "loss"
    elif choose == "scissors" and comp_choice == "rock":
        result = "loss"
    else:
        result = "win"
        rounds_won += 1

    rounds_played += 1

    feedback = "{} vs {}: {}".format(choose, comp_choice, result)
    print(feedback)

    outcome = "Round {}: {}".format(rounds_played, feedback)

    game_summary.append(outcome)

        # Ask user if they want to see their game history.
    

# quick calculation (stats)
rounds_lost = rounds_played - rounds_won -  rounds_drawn

# End of game statements
print()
print('***** End game summary *****')
print("won: {} \t\t lost: {} \t\t draw:{}".format(rounds_won, rounds_lost, rounds_drawn))

print()
print("thank you for playing")