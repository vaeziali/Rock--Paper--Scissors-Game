
# Rock, Paper, Scissors Game 

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Start the Game
game_image = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))
if player >= 3 or player < 0:
  print ("You typed a wrong number!")
else:
  print(game_image[player])
  # Random by Computer
  computer = random.randint(0,2)
  print ("computer chose:")
  print (game_image[computer])
  
  # Check and result
   
  if player == 0 and computer == 2:
    print ("You win!")
  elif computer == 0 and player == 2:
    print("You lose")
  elif computer > player:
    print ("You lose")
  elif computer < player:
    print ("You Win")
  elif computer == player:
    print("It's a draw")
  
  



