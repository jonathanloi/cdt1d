class hero:
	def __init__(self,char_name):
		self.char_name=char_name
	def stats(self):
		statistics = {
			"name": self.char_name,
			"maxhp":20,
			"hp":20,
			"days":0,
			"eq":{
				"Weapon":"Basic Sword",
				"Shield":"None",
				"Armor":"None"
			},
			"inventory":{
				"Berry":{"count":5,"eline":"You regain 5 HP!","effect":"self.pstats['hp'] += 5"},
				"Bomb":{"count":1,"eline":"Your next attack does 5 extra damage!","effect":"self.pstats['tempbonus']+=5"}
				}
			}
		return statistics