# Opens the haiku 3 and 4
myThirdHaiku = open('haiku3.txt', 'r')
myFourthHaiku = open('haiku4.txt', 'r')
# Welcomes you and gives you options
print("Hi, welcome to the Haiku Reader!")
print(" 3 For a haiku about a silly person. ") 
print(" 4 For a haiku about writing haiakus. ") 
response = raw_input()
# It will print the 3rd haiku if 3 was inserted
if response == '3':
	print(myThirdHaiku.read())
# It will give the 4th haiku if 4 was inserted
elif response == "4":
	print(myFourthHaiku.read())
