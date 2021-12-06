from random import *
from monsters import *
from character import *

class battlefield:
	def __init__(self,newchar,newstats,monster):
		self.hero = hero
		self.pstats = newstats
		self.monster = monster
		self.mstats = self.monster.stats()

	def bstate(self,i):
		enemy = f'''{self.mstats["name"]} [{self.mstats["hp"]}/{self.mstats["maxhp"]}]'''
		you = f'''{self.pstats["name"]} [{self.pstats["hp"]}/{self.pstats["maxhp"]}]'''
		question={1:"""You've got homework and assignments due the next day and your friend asked you to hang out together with her. Would you ...

a. join her because of peer pressure
b. decline politely and said you would join next time
c. None of the above""", 2:"""Upon hearing negative comments about yourself from others, how would you react?

a. Self-blame and self-hate
b. React to it positively
c. None of the above""", 3:"""You see your friends post stories with other groups of friends, you...

a. wonder why you do not have as many friends as them
b. feel happy for them
c. None of the above""", 4:"""Your group members are experienced in the topic for your school assignment, but you are completely new to the topic. You...

a. feel bad about yourself for not knowing as much as them and cannot contribute much to the project
b. see it as an opportunity to learn from your group mates and improve yourself
c. None of the above""", 5:"""You are out with your friends for dinner and they suggest to go for a few drinks. Based on past experience, it never stops at a few. Your friends are all trying to convince you but you have an important meeting tomorrow that could greatly affect your life. What will you do?

a. YOLO join them and get completely wasted! A little alcohol in your body will increase confidence during the meeting.
b. Reject their bad influence and get new friends.
c. None of the above."""}

		qn=question[i]

		battleground = f'''===================================
{enemy}

{you}

{qn}
==================================='''
		print(battleground)
		choice = input("What do you do? ")
		return choice.lower()		


# 	def inventory(self):
# 		inv1 = '\n'.join([f'''{k}: {v["count"]}''' for k,v in self.pstats["inventory"].items()])
# 		inv2 = f'''===================================
# {inv1}

# Return
# ==================================='''
# 		print(inv2)
# 		return self.pstats["inventory"]

	def action(self):
		for i in range(1,6):
			c = self.bstate(i)
			if c == "b":
				if self.pstats["hp"]<10:
					self.pstats["hp"]+=1
			elif c == "a":
				self.pstats["hp"]-=2
			elif c == "c":
				continue
			else:
				print("You have entered an invalid action!")
				input("Press ENTER to continue.")
				continue

		print(f'''===================================
{self.mstats["name"]} [{self.mstats["hp"]}/{self.mstats["maxhp"]}]
{self.pstats["name"]} [{self.pstats["hp"]}/{self.pstats["maxhp"]}]''')
		if self.pstats['hp']>=5:
			print("Congratulations! You are self-confident and do not give in to peer or societal pressures! Keep it up!")  
		else:
			print("You have succumbed to societal expectations and neglected your self-worth. It is time to start learning to love yourself and become stronger!")
		#return 0 if self.pstats['hp']>0 else 1
