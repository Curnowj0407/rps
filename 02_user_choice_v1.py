# Function go here
def choice_checker(question):

    error = "please choose from rock / paper / scissors (or xxx to quit)"

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        if response == "r" or response == "rock":
            return response
        elif response == "p" or response == "rock":
            return response
        elif response == "s" or response == "scissors":
            return response

        # check for exit code...
        elif response == "xxx":
            return response
        else:
            print(error)

# Main routine goes here


# loop for testing purpose
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and checker it's valid
    user_choice = choice_checker("choose rock / paper / paper (r/p/s):")


    # print out choice for comparison purpose
    print("you chose {}".format(user_choice))
