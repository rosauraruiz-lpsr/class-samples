# Takes myNum, an integer
# Returns True if myNum is prime
# Returns False if myNum is composite
def isPrime(y, list):
 	x = range(1,int(y))
 	number = y - 2 
        num = 0
 	# We create a for loop
	for i in x:
		remainder = int(y) % int(i)
 		# Makes an if loop 
		if remainder != 0:
			num = num + 1
                        # if the number is prime it will append to the list 
	 		if num == number:
				print(y)
				list.append(y)
# Make an empty list.
primeLister = []
# Open the file 
myPrimes = open("primes.txt", "w")
# Make a range for the def function to use.
rangeList = range(2, 10000)
# make a for loop for the range to check each number
for i in rangeList:
	num =  isPrime(i, primeLister)
# For this loop we print the number everytime it's true.
for x in primeLister:
	myPrimes.write(str(x) + "\n")		
# This closes the file.
myPrimes.close()
