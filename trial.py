from array import *

class TrackingJobs:

	def __init__(self):
		pass

# Based on estimate number entered, all the details will be displayed

	def option_A(self):
		self.user_input = input("Please enter an estimate number: ")
		with open('paintingJobs.txt') as file:
			lines = [i.strip() for i in file]		
			for line in lines:
				x = line.split(",")				
				if self.user_input == x[0]:
					print("Estimate Number:",x[0])
					print("Customer ID:",x[1])
					print("Estimate Amount:",x[2])
					print("Estimate Date:",x[3])
					print("Status:",x[4])
					
 # Displays all the outstanding payments 

	def option_B(self):
		approved = []
		payments = []
		total = 0
		# converts the file into an array
		with open('paintingJobs.txt') as file:
			lines = [i.strip() for i in file]		
			for line in lines:
				x = line.split(",")
				if x[4] == "A":
					approved.append(x)
		print("The outstanding values are as follows:")	
		for value in approved:
			if value[5] < value[3]:
				print(value[0],value[2],value[3],value[5])
			payments.append(value[5])
		for figure in payments:
			total = total + int(figure)
		print("The total outstanding payment now is:",total)

# Displays the total revenue so far

	def option_C(self):
		figures = []
		values = []
		items = 0
		with open('paintingJobs.txt') as file:
			lines = [i.strip() for i in file]		
			for line in lines:
				x = line.split(",")
				if x[4] == "A":
					figures.append(x)

		for value in figures:
			values.append(value[3])
		for item in values:
			items = int(item) + items
		print("The company's total revenue so far is:",items)


test1 = TrackingJobs()

# Based on user input, the following method will be running

print("Option A: Search for an estimate")
print("Option B: Display outstanding payments")
print("Option C: Display total revenue")
print("Enter Q to quit")

option_input = str(input("Please select an option: "))

if option_input == "A":
	test1.option_A()
elif option_input == "B":
	test1.option_B()
elif option_input == "C":
	test1.option_C()
else:
	None