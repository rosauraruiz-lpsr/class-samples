print("Do you live less than 30 miles from Richmond State? Respond yes or no.")
miles = raw_input()
print("What is your GPA?")
GPA = float(input())
if miles == "yes":
	if GPA >= 2.0:
		print("You have been admitted to Richond State.")
	else:
		print("Sorry, you have not been admitted.")
else:
	if GPA >= 2.5:
		print("What is your ACT score?")
	if GPA <= 2.5:
ActScore = int(input())		
	print("Sorry,you have not been admitted")	
if ActScore >= 18:
	ActScore = int(input())
	print("You have been admitted to Richmond State.")
else:
	print("Sorry, you have not been admitted.")

