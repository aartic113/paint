# ******************************************************************************

print("WELCOME")

class UserManagement:

	def __init__(self):
		pass

# Asks user for employee details and displays onto screen

	def employee_details(self):
		print("Employee Details")
		answer = True
		while answer:
			self.employee_name = str(input("Please enter employee's name: "))
			self.employee_id = str(input("Please enter employee's ID: "))
			employee_number = str(input("Please enter employee's number: "))
			self.qualification_level = str(input("Please enter AP for Apprentice or FQ for fully-qualified: "))
			
			if self.qualification_level == "AP":
				print("Apprentice")
			else:
				print("Fully Qualified")

			self.confirm = str(input("Please confirm all information is correctly entered? "))
			if not self.confirm[0].lower() == "n":
				answer = False
			
			else:
				print("Please enter the details again.")
				self.employee_details()
			return self.qualification_level
	
	
# The three functions generates an estimate for the user

	def information(self):
		self.customer_number = int(input("Enter customer's number: "))
		self.date_of_estimate = str(input("Enter date of estimate: "))
		self.number_of_rooms = int(input("Please enter the number of rooms: "))
		return self.number_of_rooms

	
	def rooms(self):
		self.information()
		
		for x in range(1,self.number_of_rooms+1):
			self.name = str(input("Please enter the name of the room: "))
			self.height = int(input("Please enter height of the room:" ))
			self.width = int(input("Please enter width of the room: "))
			self.wall_paper = str(input("Does the wallpaper need to be removed?"))
			if self.wall_paper[0].lower() == "y":
				self.wall_paper_rooms = int(input("How many rooms will the wall-paper need to be removed for: "))
			else:
				self.wall_paper_rooms = 0
		
		return self.height
		return self.width
		return self.wall_paper_rooms


	def figures(self):
			self.rooms()

			self.surface_area = self.height * self.width
			print("The total surface area for", self.name, "is: ",self.surface_area)

			self.price = (self.surface_area * 15) + (self.wall_paper_rooms*70)
			
			return self.price			

# Based on all the information received, a final total will be displayed

	def job_role(self):
		self.employee_details()
		self.figures()

		if self.qualification_level == "Apprentice":
			self.price = self.price + 100
		else:
			self.price = self.price + 250

		print("The total payment so far is £",self.price)
		self.price = self.price * 1.20
		print("With VAT, the total price now becomes £",self.price)

		self.query = str(input("Would you like to generate another estimate? "))
		if self.query[0].lower() == "y":
			self.employee_details()
		else:
			return self.query

copy = UserManagement()
# ---
copy.job_role()
