# creating a rolling game

import random

def roll():
    min_value = 1
    max_value = 4
    roll_value = random.randint(min_value, max_value)

    return roll_value

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")

    else:
        print("invalid input, try again. ")

max_score = 50
player_scores = [0 for _ in range(players)]

# Main game loop

game_over = False
while not game_over:
    for player_idx in range(players):
        if max(player_scores) >= max_score:
            game_over = True
            break

        print(f"\nPlayer number {player_idx + 1} turn has just started!")
        print("Your total score is: {player_scores[player_idx]} \n")
        current_score = 0

        # Player's turn to roll
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break

            else:
                current_score += value
                print(f"you rolled a {value}. Current score this turn is: {current_score}")



        player_scores[player_idx] += current_score
        print(f"your total score is now:, {player_scores[player_idx]}")


        # Check if the player has reached the max score after their turn

        if player_scores[player_idx] >= max_score:
            game_over = True
            break


winner_score = max(player_scores)
winning_idx = player_scores.index(winner_score)
print(f"\nPlayer {winning_idx + 1} is the winner with a score of: {winner_score}!")














