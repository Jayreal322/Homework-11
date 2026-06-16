import random

def roll_dice():
    return [
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6)
    ]

def score_roll(dice, round_num):
    if dice[0] == round_num and dice[1] == round_num and dice[2] == round_num:
        return 21
    elif dice[0] == dice[1] and dice[1] == dice[2]:
        return 5
    else:
        points = 0

        for die in dice:
            if die == round_num:
                points = points + 1

        return points

def player_turn(player, round_num):
    print()
    print("Player", player, "Round", round_num)

    total = 0
    points = 1

    while points > 0:
        dice = roll_dice()
        points = score_roll(dice, round_num)

        print("Rolled:", dice, "Points:", points)

        total = total + points

    print("Player", player, "round total:", total)
    return total

def main():
    num_sets = int(input("Enter number of sets, 2 to 4: "))

    scores = [0, 0, 0, 0]

    for set_num in range(1, num_sets + 1):
        print()
        print("Set", set_num)

        for round_num in range(1, 7):
            print()
            print("Round", round_num)

            for player in range(1, 5):
                points = player_turn(player, round_num)
                scores[player - 1] = scores[player - 1] + points

            print("Scores:", scores)

    high_score = max(scores)
    winner = scores.index(high_score) + 1

    print()
    print("Final Scores:", scores)
    print("Player", winner, "wins!")

main()
