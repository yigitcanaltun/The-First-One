import sys
import random
sys.argv

ran_num=random.randint(1,10)

user_num = int(input("Enter a number between 1 and 10: "))
count=1

if user_num>10 or user_num<1:
	int(input("Out of boundaries. Enter a valid number between 1 and 10: "))
	count +=1

while ran_num!=user_num:
	try: 
		user_num_new = int(input("Enter a number between 1 and 10: "))
		count += 1
		if user_num_new==ran_num:
			print("Congrats")
			break
	except (TypeError, ValueError):
		input("Enter a valid number: ")
		continue
print(f"You have guessed the correct number in {count} times")