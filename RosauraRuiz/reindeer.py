import random
reindeer = ['ruldoph', 'donner', 'blitzen', 'dancer', 'prancer', 'comet']

count = 0 
while count < 10:
	index = random.randint(0,6)
	print(reindeer[index])
	count = count + 1
