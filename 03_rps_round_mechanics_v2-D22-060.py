def check_rounds():
    while True:
        response = input("how many rounds:")

        round_error = "please type either <enter> or an integer that is more than 0"

        if response != "":
            try: