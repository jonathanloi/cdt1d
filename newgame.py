from random import *
from monsters import *
from battlefield import battlefield
from menu import menus
from questions import *

class newgame():

	def popup_question():
		#Something questions 2
		qchoice = random.choice(list(questions.keys()))
		qview = questions[qchoice]
		questions.pop(qchoice)
		while True:
			m.newline(qview)
			ans = input("Your choice. ")
			if ans == XYZ
				...

	def start_instance(self,newchar,newstats):

		m = menus(newstats)
		self.popup_question()
		m.newline(f'''We live in a highly competitive society. From academic, to family and our career, there are tons of expectations we have set as a society. It does not help that social media has become the norm in our generation. With the prevalence of social media, we are constantly comparing ourselves to others who live the 'perfect' life, pressured to follow the latest trends and subjected to FOMO. While struggling to keep up with societal expectations, we tend to lose focus on ourselves and put ourselves in a cycle of self-doubt.

Play this game to find out how self-confident you are!''')
		a = battlefield(newchar,newstats,gobbo()) # This is the object
		a.action() # This is the action module
		m.choices() # This runs after the fight and if u r alive -> what do u do next? -> If u choose continue it will run the next line of code
		a.action() # This is the action module
		m.newline(f'''Thank you for participating in our game!''')

		return None
	