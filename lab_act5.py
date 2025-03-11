def classify_age():
	print("This will categorized you based on your age.")
	
while True:
	try:
		age = int(input("Input your age: "))
		if age < 0:
			print("Invalid age! Please enter a non-negative number. ")
		elif age <= 12:
			print("You are a Child.")
		elif age <= 19:
			print("You are a Teen.")
		elif age <= 64:
			print("You are a Adult.")
		else:
			print("You are a Senior.")
	except ValueError:
		print("Invalid age! Please enter a non-negative number. ")