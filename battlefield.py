from random import choice
# from monsters import *
from character import *
from questions import *
from menu import *

class battlefield:
	def __init__(self,newchar,newstats,monster):
		self.hero = hero
		self.pstats = newstats
		# self.monster = monster
		self.mstats = self.monster.stats()


	def bstate(self, qn):
		enemy = '''Society [20/20]'''
		you = f'''{self.pstats["name"]} [{self.pstats["hp"]}/{self.pstats["maxhp"]}]'''

		qchoice = choice(list(qn.keys()))
		qview = qn[qchoice]
		qn.pop(qchoice)

		battleground = f'''===================================
{enemy}

{you}

{qview}
==================================='''
		print(battleground)
		pchoice = input("What do you do? ")
		return pchoice.lower(),qn		



	def inventory(self):
		inv1 = '\n'.join([f'''{k}: {v["count"]}''' for k,v in self.pstats["inventory"].items()])
		inv2 = f'''===================================
{inv1}

Return
==================================='''
		print(inv2)
		return self.pstats["inventory"]



	def action(self):
		q = questions()
		qn = q.game_qn()
		for i in range(5):
			c,qn = self.bstate(qn)
			while True:
				if c == "a":
					self.pstats["hp"] -= 3
					if self.pstats["hp"] <= 0:
						print("""===================================

You have lost the game. 

===================================""")
						input("Press ENTER to continue")
						exit()
					else:
						break
				elif c == "b":
					if self.pstats["hp"] <= self.pstats["maxhp"]-2:
						self.pstats["hp"]+=2
						break
					else:
						break
				elif c == "c":
					break
				else:
					print("You have entered an invalid action!")
					continue

		print(f'''===================================
{self.mstats["name"]} [{self.mstats["hp"]}/{self.mstats["maxhp"]}]
{self.pstats["name"]} [{self.pstats["hp"]}/{self.pstats["maxhp"]}]
''')
		if self.pstats['hp']>=12:
			print("""Congratulations! You are self-confident and do not give in to peer or societal pressures! Keep it up!
===================================""")  
		else:
			print("""You have succumbed to societal expectations and neglected your self-worth. It is time to start learning to love yourself and become stronger!

You will now be brought to learn the importance resting and exercising to build up your self confidence.
===================================""")
		input("Press ENTER to continue.")