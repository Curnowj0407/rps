# RPS component 6 - scoring system

# Rounds won will be calculate (total  - draw - lost )
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Result for testing purpose
test_results = ["won", "won", "loss", "loss", "tie"]

# Play Game
for item in test_results:
    rounds_played += 1

    # generate computer choice

    result = item

    if result == "tie":
        result = "it's a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1

# quick calculation (stats)
rounds_won = rounds_played - rounds_lost -  rounds_drawn

# End of game statements
print()
print('***** End game summary *****')
print("won: {} \t\t lost: {} \t\t draw:{}".format(rounds_won, rounds_lost, rounds_drawn))

print()
print("thank you for playing")