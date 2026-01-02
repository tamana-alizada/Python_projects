# This project is taken from BroCode Python Tutorial!

# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
import random 

dice_art = {
  1: ("┌─────────┐", 
      "│         │", 
      "│    ●    │", 
      "│         │", 
      "└─────────┘"),
  2: ("┌─────────┐", 
      "│  ●      │", 
      "│         │", 
      "│      ●  │", 
      "└─────────┘"),
  3: ("┌─────────┐", 
      "│  ●      │", 
      "│    ●    │", 
      "│      ●  │", 
      "└─────────┘"),
  4: ("┌─────────┐", 
      "│  ●   ●  │", 
      "│         │", 
      "│  ●   ●  │", 
      "└─────────┘"),
  5: ("┌─────────┐", 
      "│  ●   ●  │", 
      "│    ●    │", 
      "│  ●   ●  │", 
      "└─────────┘"),
  6: ("┌─────────┐", 
      "│  ●   ●  │", 
      "│  ●   ●  │", 
      "│  ●   ●  │", 
      "└─────────┘")
}

num_of_dice = int(input("How many dice?:  "))
dice = []
total = 0
for die in range(num_of_dice):
  dice.append(random.randint(1, 6))

# for num in range(num_of_dice):
#     for die in dice_art.get(dice[num]):
#        print(die)

for line in range(5):
  for die in dice:
      print(dice_art.get(die)[line], end="")
  print()

for die in dice:
   total += die
print(f"Total: {total}")