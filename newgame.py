from random import *
from monsters import *
from battlefield import battlefield
from menu import menus

class newgame():

	def start_instance(self,newchar,newstats):

		m = menus(newstats)

		m.newline(f'''We live in a highly competitive society. From academic, to family and our career, there are tons of expectations we have set as a society. It does not help that social media has become the norm in our generation. With the prevalence of social media, we are constantly comparing ourselves to others who live the 'perfect' life, pressured to follow the latest trends and subjected to FOMO. While struggling to keep up with societal expectations, we tend to lose focus on ourselves and put ourselves in a cycle of self-doubt.

Play this game to find out how self-confident you are!''')
		a = battlefield(newchar,newstats,gobbo())
		a.action()
		m.newline(f'''Thank you for participating in our game!''')
		m.choices()

		return None
