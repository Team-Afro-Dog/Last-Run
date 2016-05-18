'''
In charge starting the game and handling in which state
When the user runs the game, they run this script first
'''

import game

def runWelcomeScreen():
   '''For now we are returning fixed data'''
   print("Staring game...")
   return {"name" : "Bob", "level" : 1} 

def endGame():
   '''Currently nothing but later do something interesting'''
   print("Closing game...")

def main():
   
   '''Probably for selecting level, getting user's name...etc
   someParameter should be a dictionary
   '''
   stats = runWelcomeScreen() 

   '''Run the actual game after welcome screen done'''
   game.game(stats)

   endGame() 

main()


 
