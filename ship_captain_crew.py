import random

def roll_dice(num):
    dice = []

    for i in range(num):
        dice.append(random.randint(1, 6))

    return dice

def take_turn(player):
    print()
    print("Player", player, "turn")

    has_ship = False
    has_captain = False
    has_crew = False
    cargo_score = 0
    dice_left = 5

    for roll_num in range(1, 4):
        dice = roll_dice(dice_left)
        print("Roll", roll_num, ":", dice)

        if has_ship == False and 6 in dice:
            has_ship = True
            dice.remove(6)
            dice_left = dice_left - 1
            print("Ship found!")

        if has_ship == True and has_captain == False and 5 in dice:
            has_captain = True
            dice.remove(5)
            dice_left = dice_left - 1
            print("Captain found!")

        if has_ship == True and has_captain == True and has_crew == False and 4 in dice:
            has_crew = True
            dice.remove(4)
            dice_left = dice_left - 1
            print("Crew found!")

        if has_ship and has_captain and has_crew:
            cargo_score = sum(dice)
            dice_left = 2
            print("Cargo score:", cargo_score)

    if has_ship and has_captain and has_crew:
        return cargo_score
    else:
        return 0

def main():
    num_players = int(input("Enter number of players: "))

    scores = []

    for player in range(1, num_players + 1):
        score = take_turn(player)
        scores.append(score)
        print("Player", player, "score:", score)

    high_score = max(scores)

    if scores.count(high_score) > 1:
        print()
        print("There is a tie. Tied players should play again.")
    else:
        winner = scores.index(high_score) + 1
        print()
        print("Player", winner, "wins with", high_score, "points!")

main()
