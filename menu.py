from character import *
from random import *

class menus:

	def __init__(self,newstats):
		self.newstats = newstats

	def newline(self, text):
		print(f'''===================================
{text}
===================================''')
		return input("Press ENTER to Continue.")

	def status(self):
		inv = ' / '.join([f'''{k}: {v["count"]}''' for k,v in self.newstats["inventory"].items()])
		self.newline(f'''Your current statistics.
HP: {self.newstats["hp"]}/{self.newstats["maxhp"]}
Attack: {self.newstats["minatk"]}-{self.newstats["maxatk"]}
Inventory: {inv}
Days of Travel: {self.newstats["days"]}''')

	def forage(self):
		items = {
			"Berry":{"count":randint(1,3),"eline":"You regain 5 HP!","effect":"self.pstats['hp'] += 5"},
			"Potion":{"count":1,"eline":"You restore your health fully!","effect":"self.pstats['hp'] = self.pstats['maxhp']"}
		}
		choose = choice(list(items.keys()))
		out = f'''===================================
You forage in the surrounding lands.

You find {items[choose]["count"]}x {choose}! Upon using this item, the following effect applies:

[ {items[choose]["eline"]} ]
==================================='''
		if choose in self.newstats["inventory"]:
			self.newstats["inventory"][choose]["count"] += items[choose]["count"]
		else:
			self.newstats["inventory"][choose] = items[choose]
		print(out)
		input("Press ENTER to view your inventory.")
		self.status()

	def shop(self):
		self.newline("A friendly merchant shows you their wares.")

	def downtime(self):

		out = f'''===================================
The rest of the day is free.
[ Rest ]  [ Forage ]
[ Status ]
==================================='''

		while True:
			self.newstats["days"] += 1
			print(out)
			dt = input("What do you do? ")
			if dt.lower() == "rest":
				self.newstats["hp"] = self.newstats["maxhp"]
				self.newline("You take a break for the day, tending to your wounds. Your health is fully restored!")
				break
			elif dt.lower() == "forage":
				self.forage()
				break
			elif dt.lower() == "status":
				self.status()
			else:
				print("You have entered an invalid response. Please try again.")

	def choices(self):

		out = f'''===================================
The next step of your journey awaits you.

Make your choice. (Type the word in the brackets like these.)
[ Continue your Journey (Continue) ]
[ Take a break, spend some Downtime (Downtime) ]
[ Quit the Game (Quit) ]
==================================='''
		while True:
			print(out)
			dt = input("What do you do? ")
			if dt.lower() == "continue":
				break
			elif dt.lower() == "downtime":
				self.newline("You decide to break from your journey for a bit to do other things.")
				self.downtime()
			elif  dt.lower() == "quit":
				self.newline("You have quit the game.")
				exit()
			else:
				print("You have entered an invalid response. Please try again.")