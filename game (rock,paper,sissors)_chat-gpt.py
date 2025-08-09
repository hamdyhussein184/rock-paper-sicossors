#!/usr/bin/env python3
import random

wins = losses = draws = 0
moves = {"r": "Rock", "p": "Paper", "s": "Scissors"}
beats = {("r", "s"), ("p", "r"), ("s", "p")}

print("Rock‑Paper‑Scissors — press q to quit")
while True:
    player = input("Choose [r]ock, [p]aper, [s]cissors: ").lower()
    if player.startswith("q"):
        break
    if player not in moves:
        print("Invalid choice, try again.\n")
        continue

    computer = random.choice(list(moves))
    print(f"You: {moves[player]} | Computer: {moves[computer]}")

    if player == computer:
        result = "Draw!"
        draws += 1
    elif (player, computer) in beats:
        result = "You win! 🎉"
        wins += 1
    else:
        result = "Computer wins! 😅"
        losses += 1

    print(result)
    print(f"Score → You {wins} | Computer {losses} | Draws {draws}\n")

print("Thanks for playing — goodbye!")
