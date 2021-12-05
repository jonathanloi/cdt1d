from random import *
from monsters import *
from character import *

class battlefield:
	def __init__(self,newchar,newstats,monster):
		self.hero = hero
		self.pstats = newstats
		self.monster = monster
		self.mstats = self.monster.stats()

	def bstate(self):
		enemy = f'''{self.mstats["name"]} [{self.mstats["hp"]}/{self.mstats["maxhp"]}]'''
		you = f'''{self.pstats["name"]} [{self.pstats["hp"]}/{self.pstats["maxhp"]}]'''
		battleground = f'''===================================
{enemy}

{you}

Attack	Block	Item
==================================='''
		print(battleground)
		choice = input("What do you do? ")
		return choice.lower()

	def attack(self,t1,t2):
		d = randint(t1["minatk"],t1["maxatk"])+t1["tempbonus"]
		t2["hp"] += -d
		t1["tempbonus"] = 0
		print(f'''{t1["name"]} attacks {t2["name"]} for {d} damage! {t2["name"]} is now at {t2["hp"]} HP.''')
		return None

	def inventory(self):
		inv1 = '\n'.join([f'''{k}: {v["count"]}''' for k,v in self.pstats["inventory"].items()])
		inv2 = f'''===================================
{inv1}

Return
==================================='''
		print(inv2)
		return self.pstats["inventory"]

	def action(self):
		while self.mstats['hp']>0 and self.pstats['hp']>0:
			c = self.bstate()
			if c == "attack":
				self.attack(self.pstats,self.mstats)
			elif c == "block":
				self.pstats["block"] += 1
				print("You lean in, reducing some damage!")
			elif c == "item":
				self.inventory()
				c2 = input("What do you use? ").capitalize()
				if c2 in self.inventory().keys():
					exec(self.inventory()[c2]["effect"])
					self.inventory()[c2]["count"] += -1
					print(self.inventory()[c2]["eline"])
				elif c2 == "return":
					continue
				else:
					print("You have entered an invalid action!")
					continue
			else:
				print("You have entered an invalid action!")
				continue
			self.monster.ai(self.pstats)

		print("You are victorious!") if self.pstats['hp']>0 else print("You have lost.")
		return 0 if self.pstats['hp']>0 else 1
