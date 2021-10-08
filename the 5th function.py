import random
print("Number Guessing Game")
lower = 1
upper = random.randint(50,200)
print("The range for this round is ",lower,"-",upper)

x = random.randint(lower, upper)
attempts = 0
guess = 0

while x != guess:	
	guess = int(input("Make a guess : "))
	if x > guess:
		lower = guess
		print("The range is now ",lower,"-",upper)
		attempts = attempts + 1
	if x < guess:
		upper = guess
		print("The range is now ",lower,"-",upper)
		attempts = attempts + 1

else:
	attempts = attempts + 1
	print("BINGO! You took ",attempts," attempts to reach the answer!")