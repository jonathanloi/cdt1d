from random import choice as ch
from monsters import *
from battlefield import battlefield
from menu import *
from questions import *

class newgame:

	def popup_question(self,newstats):
		#Something questions 2
		m = menus(newstats)
		q = questions()
		rand_qn = q.random_qn()
		qchoice = ch(list(rand_qn.keys()))
		qview = rand_qn[qchoice]
		rand_qn.pop(qchoice)
		while True:
			print(f"""===================================
{qview}
===================================""")
			ans = input("Your choice: ")
			if ans.lower() == 'yes':
				break
			elif ans.lower() == 'no':
				print("GAME OVER")
				exit()
			else: 
				print("You have entered an invalid action!")
				continue


	def start_instance(self,newchar,newstats):

		m = menus(newstats)
		self.popup_question(newstats)
		m.newline(f'''We live in a highly competitive society. From academic, to family and our career, there are tons of expectations we have set as a society. It does not help that social media has become the norm in our generation. With the prevalence of social media, we are constantly comparing ourselves to others who live the 'perfect' life, pressured to follow the latest trends and subjected to FOMO. While struggling to keep up with societal expectations, we tend to lose focus on ourselves and put ourselves in a cycle of self-doubt.

Play this game to find out how self-confident you are!''')
		a = battlefield(newchar,newstats,gobbo()) # This is the object
		a.action() # This is the action module
		m.choices() # This runs after the fight and if u r alive -> what do u do next? -> If u choose continue it will run the next line of code
		a.action() # This is the action module
		m.newline(f'''Thank you for participating in our game!''')

		return None