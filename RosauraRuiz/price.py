
print("Enter amount of purchase, in cents:")
x = int(input())
cents1 = x * .10
y = int(cents1)
cents2 = x - cents1
if x < 1000:
    print("You get no discount.")
else: 
    print("You get a discount. your total will be " + str(cents2) +"  ")
