from character import *
from random import *
from questions import *

class menus:

	def __init__(self,newstats):
		self.newstats = newstats

	def newline(self, text):
		print(f'''===================================
{text}
===================================''')
		return input("Press ENTER to Continue.")

	def status(self):
		self.newline(f'''Your current statistics.
HP: {self.newstats["hp"]}/{self.newstats["maxhp"]}
Days of Exploration: {self.newstats["days"]}''')


	def forage(self):
		items = {
			"Chocolate":{"count":randint(2,5),"eline":"regained 2 HP!","effect":2},
			"Yogurt":{"count":1,"eline":"regained 3 HP!","effect":3},
			"Nuts":{"count":randint(10,20),"eline":"regained 3 HP!","effect":3} 
		}
		choose = choice(list(items.keys()))
		out = f'''===================================
You searched your kitchen and found some delicious snacks to treat yourself after a long day of work.
You binged on {items[choose]["count"]}x {choose} and {items[choose]["eline"]}
==================================='''
		self.newstats['hp'] += items[choose]["effect"]
		print(out)
		input("Press ENTER to view your status.")
		self.status()


	def downtime(self):

		out = f'''===================================
Select an activity you wish to do.
[ Meditate ]  [ Forage ]
[ Exercise ]  [ Status ]
[ Back to Game  (back) ]
==================================='''

		while True:
			self.newstats["days"] += 1
			print(out)
			dt = input("What do you do? ")
			if dt.lower() == "meditate":
				self.newstats["hp"] = self.newstats["maxhp"]
				self.newline("You took a well-deserved break to recover your mind and body. Your health is now fully restored!")
				break
			elif dt.lower() == "forage":
				self.forage()
				break
			elif dt.lower() == "exercise":
				if self.newstats["hp"] < self.newstats['maxhp']-4:
					self.newstats["hp"] += 4
					print("""===================================
You sweated out your stresses and regained 6 HP!""")
				else:
					self.newstats["hp"] = self.newstats['maxhp']
					print("""===================================
You sweated out your stresses and restored your health!""")
				
				input("Press ENTER to view your status.")
				self.status()
				break
			elif dt.lower() == "status":
				self.status()
			elif dt.lower() == "back":
				break
			else:
				print("You have entered an invalid response. Please try again.")
		
		q = questions()
		q.popup_question2()

	def choices(self):

		out = f'''===================================
The next step of your Exploration awaits you.
Make your choice. (Type the word in the brackets like these.)
[ Continue your Exploration (Continue) ]
[ Take a break, spend some Downtime (Downtime) ]
[ Quit the Game (Quit) ]
==================================='''
		while True:
			print(out)
			dt = input("What do you do? ")
			if dt.lower() == "continue":
				break
			elif dt.lower() == "downtime":
				self.newline("You have decided to take a break to do other things.")
				self.downtime()
			elif  dt.lower() == "quit":
				self.newline("You have quit the game. Thanks for Playing!")
				exit()
			else:
				print("You have entered an invalid response. Please try again.")