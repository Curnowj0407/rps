 # version 3 - checker that response is in a given list

# Function go here
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

# Main routine goes here



# lists for checking responses
rsp_list= ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("choose rock / paper"
                                 " / scissors (r/p/s):", rsp_list,
                                 "please choose from rock /"
                                "paper / scissors"
                                 "(or xxx to quit)")


    # print out choice for comparison purposes
    print ("you chose {}".format(user_choice))