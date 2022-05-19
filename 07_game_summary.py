game_summary = []
rounds_lost = 0
rounds_drawn = 0
rounds_played = 0

for item in range (0, 5):
    result = input ("choose result: ")
    rounds_played += 1

    if result == "lost":
        rounds_lost += 1
        feedback = "Sorry - you lost"
    elif result == "tie":
        rounds_drawn += 1
        feedback = "It's a tie"
    else:
        feedback = "You won"

    print(feedback)

    outcome = "Round {}: {}".format(rounds_played, feedback)

    game_summary.append(outcome)


rounds_won = rounds_played - rounds_lost - rounds_drawn

# ***** calculate game stats *****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

print()

# display game stats with % value to the nearest whole numvber
print("******* Game Statistic *******")
print("win:{}, ({:.0f}%)\nLoss:{},({:.0f}%)\ntie:{}, "
      "({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn,percent_tie ))
