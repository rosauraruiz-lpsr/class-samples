# Class defines Players 
class Player(object):
	def __init__(self,name,age,goals):
		self.name = name
		self.age = age
		self.goals = goals
	def printStats(self):
		print("Name:" + self.name)
		print("Age:" + self.age)
		print("Goals:" + self.goals)
# Creates an empty list for myPlayers
myPlayers = []
# Introduces the soccer team
print("Welcome to our soccer team! If you want to add a player enter 1. If you want to view player enter 2.")
answer = raw_input()
# When user chooses option 0 it will take user out of the program
while answer != "0":
# When user chooses option  it will let the user add players to the list
	if answer == "1":
		print("You want to add a player so fill in the folowing")
		print("Name:")
		name = raw_input()
		print("Age:")
		age = raw_input()
		print("Goals:")
		goals = raw_input() 
		myPlayers.append(Player(name,age,goals))
		print("Done. Do you want to add a player (1), or do you want view the players (2), or do you want to exit(0)")
		answer = raw_input()	
# When user chooses option it will show a list of players
	elif answer == "2":

		print("Lets see the stats.")
		for info in myPlayers:
			info.printStats()
		print("Done. Do you want to add a player (1), or do you want view the players (2), or do you want to exit(0)")
		answer = raw_input()
