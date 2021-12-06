from random import choice as ch
from monsters import *
from character import *
from questions import *
from menu import *

class battlefield:
	def __init__(self,newchar,newstats,monster):
		self.hero = hero
		self.pstats = newstats
		self.monster = monster
		self.mstats = self.monster.stats()



	def bstate(self):
		enemy = f'''{self.mstats["name"]} [{self.mstats["hp"]}/{self.mstats["maxhp"]}]'''
		you = f'''{self.pstats["name"]} [{self.pstats["hp"]}/{self.pstats["maxhp"]}]'''

		q = questions()
		qn = q.game_qn()
		qchoice = ch(list(qn.keys()))
		qview = qn[qchoice]
		qn = qn.pop(qchoice)

		battleground = f'''===================================
{enemy}

{you}

{qview}
==================================='''
		print(battleground)
		choice = input("What do you do? ")
		return choice.lower()		


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
			if c == "a":
				self.pstats["hp"]-=4
			elif c == "b":
				if self.pstats["hp"]<self.pstats["maxhp"]:
					self.pstats["hp"]+=2
				else:
					continue
			elif c == "c":
				continue
			else:
				print("You have entered an invalid action!")
				continue

		print(f'''===================================
{self.mstats["name"]} [{self.mstats["hp"]}/{self.mstats["maxhp"]}]
{self.pstats["name"]} [{self.pstats["hp"]}/{self.pstats["maxhp"]}]''')
		if self.pstats['hp']>=12:
			print("Congratulations! You are self-confident and do not give in to peer or societal pressures! Keep it up!")  
		else:
			print("You have succumbed to societal expectations and neglected your self-worth. It is time to start learning to love yourself and become stronger!")
		#return 0 if self.pstats['hp']>0 else 1
