import sys
import random

number = input("> ")

if number != "random":
	convtnumber = int(number)
else:
	convtnumber = "random"
	
total = 0

def calculate(convtnumber, total):
	
	if convtnumber == 4:
		print("total:", total, "numbers before 2-4-1 pattern")
		sys.exit()
	elif convtnumber % 2:
		convtnumber = (convtnumber * 3) + 1
		print(convtnumber)
		total += 1
		calculate(convtnumber, total)
	else:
		convtnumber = convtnumber / 2
		print(convtnumber)
		total +=1
		calculate(convtnumber, total)
		
def randomcalc(convtnumber, total):
	
	convtnumber = random.randint(5, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
	calculate(convtnumber, total)
		
if number != "random":
			
	calculate(convtnumber, total)

else:

	randomcalc(convtnumber, total)
