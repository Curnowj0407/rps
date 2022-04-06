# Fuction used to check input is vaild


def check_rounds():

    while True:
        response = input ("how many rounds: ")

        round_error = "please type either <enter> or an integerthat is more 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print (round_error)
                    continue

            except ValueError:
                print(round_error)
                continue


        return response

# Main routine goes here

rounds_played = 0
choose_instruction = "please choose rock (r), paper (p), or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds =="":
        
        headings = "continue mode: round {}".format(rounds_played)
        print(headings)
        choose = input("{} or 'xxx' to end:".format(choose_instruction))
        if choose == "xxxc":
            break
    else:
        headings = "round {} of {}".format(rounds_played + 1, rounds)
        print(headings)
        choose = input(choose_instruction)
        if rounds_played == rounds -1:
            end_game = "yes"

    # rest of loop / ga,e
    print("you choose {}".format(choose))

    rounds_played += 1

print("thank you for playing")



