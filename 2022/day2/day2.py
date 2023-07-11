with open('day2.in') as file:
    data = [i for i in file.read().strip().split('\n')]


# 0 if lost, 3 if draw, 6 if win
# 1 for rock, 2 for paper, 3 for scissors

# A: rock, B: paper, C: scissors
# X: rock, Y: paper, Z: scissors

# WIN, LOSE, DRAW

# PART 1
# guide = [['A Y', 'B Z', 'C X'], ['A Z', 'B X', 'C Y'], ['A X', 'B Y', 'C Z']]
# point_scheme = {'X': 1, 'Y': 2, 'Z': 3}
# total_points = 0


# for match in data:
#     total_points += point_scheme[match[2]]

#     if match in guide[0]:
#         total_points += 6
#     elif match in guide[1]:
#         total_points += 0
#     else:
#         total_points += 3

# print(total_points)

# PART 2
# X: lose, Y: draw, Z: win

total_points = 0

requirement = {'X': 0, 'Y': 1, 'Z': 2}
point_scheme = {'X': 1, 'Y': 2, 'Z': 3}

# LOSE, DRAW, WIN
guide = [['A Z', 'B X', 'C Y'], ['A X', 'B Y', 'C Z'], ['A Y', 'B Z', 'C X']]

for match in data:
    # opponent_move = opponent_move, game_state = what we want to do
    opponent_move = match[0]
    game_state = match[2]

    # basically we find the game state we want and copy the move correlated with that state
    for state in guide[requirement[game_state]]:
        if state[0] == opponent_move:
            my_move = state[2]

    total_points += point_scheme[my_move]
    # this ending line is funny cause if lose = 0 points = 0*3, draw = 3 points = 1*3, win = 6 points = 2*3
    total_points += requirement[game_state] * 3

print(total_points)
