from newgame import newgame
from character import *

class main:

	def __init__(self,newchar):
		self.newchar = newchar
		self.newstats = newchar.stats()

	def start(self):

		out = f'''===================================
Welcome, new Hero. To the Game of Choices. Please select a choice below.
[ New Game ]
[ Help ]
[ Quit ]
==================================='''
		helptext = f'''===================================
The Game of Choices is a simple RPG meant to help with teaching players how to make the best choice to progress. They will be tasked with defeating the Demon King, and it will be hard, but as they learn what does what, they will definitely be able to complete the game.
==================================='''

		while True:
			print(out)
			x = input("Your Choice: ")
			if x.lower()=="quit":
				input("Game is now ending. Press ENTER to continue.")
				exit()
			if x.lower()=="help":
				print(helptext)
				input("Press ENTER to continue.")
				continue		
			elif x.lower() == "new game":
				input("Game is now starting. Press ENTER to continue.")
				newgame().start_instance(self.newchar,self.newstats)
				break
			else:
				print("You have entered an invalid response. Please try again.")

main(hero()).start()