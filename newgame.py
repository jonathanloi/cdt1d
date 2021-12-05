from random import *
from monsters import *
from battlefield import battlefield
from menu import menus

class newgame():

	def start_instance(self,newchar,newstats):

		m = menus(newstats)

		m.newline(f'''The story begins, telling of a lone hero, living a simple life, living a peaceful life. You have enjoyed this peaceful life for a long time, but today that which you lived fo shall be tested. An evil being stands between you and your home! Pick up your sword and fight!''')
		a = battlefield(newchar,newstats,gobbo())
		a.action()
		m.newline(f'''The threat has now been vanquished, and you take some time to scan the surroundings. The village now stands in tatters, a flag bearing an evil crown revealing itself. The Demon King has awakened, and you are the only one who can slay him. Your journey now begins! The first thing to do is to find a place to rest, or get stronger.''')
		m.choices()

		return None
