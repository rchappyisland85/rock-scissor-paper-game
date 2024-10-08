import time
import random

def rock():
     return """
    _________ 
---|    |____|
     |__|____|
     (_______|
---|_(_______|

"""


def scissor():
	return """
    ___________    
---|    |______|   
     |__|_________ 
     (_____|______|
---|_(_____|     
"""


def paper():
	return """
    ______        
___|  ____|__     
        _____|__   
       _________|  
      ________|   
---|________|     
"""

choice = {
	"rock": rock(),
	"scissor": scissor(),
	"paper": paper()
}

game_choice = ["rock", "scissor", "paper"]

print("Game Rule: First to win 2 games of 3. If there's a tie, the game continues.")

player_win = 0
computer_win = 0

while player_win < 2 and computer_win < 2:
	  player_choice = random.choice(game_choice)
	  print(f"Player's choice:\n{choice[player_choice]}")
	  computer_choice = random.choice(game_choice)
	  print(f"Computer's choic:\n{choice[computer_choice]}")
	
	
	  if((player_choice == "rock" and computer_choice == "scissor") or 
	    (player_choice == "scissor" and computer_choice == "paper") or
	    (player_choice == "paper" and computer_choice == "rock")):
	    print(f"Player win this round, and total rounds win: {player_win + 1}")
	    player_win += 1
	  elif((computer_choice == "rock" and player_choice == "scissor") or 
		  (computer_choice == "scissor" and player_choice == "paper") or
		  (computer_choice == "paper" and player_choice == "rock")):
		  print(f"Computer win this round, and total rounds win: {computer_win + 1}")
		  computer_win += 1
	  else:
		  print(f"Tied Game!")
		  continue

	  time.sleep(1)
		
if player_win == 2:
	print("Player won this game!")
else:
	print("Computer won this game!")
