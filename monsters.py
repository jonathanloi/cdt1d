from random import *

class gobbo:

	def stats(self):
		statistics = {
			"name":"Goblin",
			"maxhp":10,
			"hp":10
			}
		return statistics

	def ai(self,stats):
		decision = randint(1,3)
		if decision < 3:
			attack = "uses a Shiv"
			d = randint(1,3)
		else:
			attack = "throws a Bomb"
			d = randint(2,5)
			
		d//2 if stats["block"] == 1 else None
		stats["block"] == 0
		stats["hp"] += -d
		print(f'''Goblin {attack}, dealing {d} damage! {stats["name"]} is now at {stats["hp"]} HP.''')