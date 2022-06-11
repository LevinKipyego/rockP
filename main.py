import random
from enum import Enum
class Action(Enum):
  Rock="R"
  Paper="P"
  Scissors ="S"
   
   
#user input
def get_user_input():
  user=input('choose R for Rock P for Paper and S for Scissors:')
  selection=user.upper()
  actionU=Action(selection)
  print(f'User({actionU.name})')
  return actionU


#cpu select
def get_cpu_input():
  cpu=random.choice(["R","P","S"])
  action=Action(cpu)
  print (f'Cpu ({action.name})')
  return action


#determin_winner
def get_winner(user_action,cpu_action):
  
  if user_action == cpu_action:
    print(f"Both players selected {cpu_action.name} It's a tie!")
  elif user_action== Action.Rock:
    if cpu_action == Action.Scissors:
      print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
  elif user_action == Action.Paper:
    if cpu_action == Action.Rock:
      print("Paper beats rock! You win!")
    else:
       print("Scissors beats paper! You lose.")
  elif user_action == Action.Scissors:
    if cpu_action == Action.Paper:
      print("Scissors beats paper! You win!")
    else:
      print("Rock beats scissors! You lose.")
   
#get_winner(get_user_input(),get_cpu_input())

while True:
    try:
        user_action = get_user_input()
    except ValueError as e:
       
        print("😱😱you entered an Invalid selection please try again***\n")
        continue

    cpu_action = get_cpu_input()
    get_winner(user_action, cpu_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
      break

