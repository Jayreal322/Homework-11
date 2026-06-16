import random

def roll_die():
    sides = ["L", "C", "R", ".", ".", "."]
    return random.choice(sides)

def players_with_chips(chips):
    count = 0
    for chip in chips:
        if chip > 0:
            count = count + 1
    return count

def main():
    num_players = int(input("Enter number of players, 3 or more: "))

    chips = [3] * num_players
    center = 0
    player = 0
    round_num = 1

    while players_with_chips(chips) > 1:
        print()
        print("Round", round_num)
        print("Player", player + 1, "turn")

        dice_to_roll = chips[player]

        if dice_to_roll > 3:
            dice_to_roll = 3

        if dice_to_roll == 0:
            print("Player has no chips and skips.")
        else:
            for i in range(dice_to_roll):
                roll = roll_die()
                print("Rolled:", roll)

                if roll == "L":
                    chips[player] = chips[player] - 1
                    left = (player - 1) % num_players
                    chips[left] = chips[left] + 1
                elif roll == "R":
                    chips[player] = chips[player] - 1
                    right = (player + 1) % num_players
                    chips[right] = chips[right] + 1
                elif roll == "C":
                    chips[player] = chips[player] - 1
                    center = center + 1

        print("Chips:", chips)
        print("Center pot:", center)

        player = (player + 1) % num_players

        if player == 0:
            round_num = round_num + 1

    for i in range(num_players):
        if chips[i] > 0:
            print()
            print("Player", i + 1, "wins!")
            print("Center pot prize:", center)

main()
