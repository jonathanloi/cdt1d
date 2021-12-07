from newgame import newgame
from character import *
from questions import *

class main:

	def __init__(self,newchar):
		self.newchar = newchar
		self.newstats = newchar.stats()

	def start(self,char_name):
		out = '''===================================
Welcome to the Game of Life Choices, {}! Please select a choice below.
[ New Game ]
[ Help ]
[ Quit ]
==================================='''.format(char_name)
		helptext = f'''===================================
The Game of Life Choices is a simple RPG meant to educate players on the importance of loving oneself. Players will be tasked to make some life choices during the game. At the end of the game, players will gain insight on how much they love themselves.
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

char_name = input("Please enter your name: ")
main(hero(char_name)).start(char_name)