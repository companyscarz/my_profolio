contactbook=[] #variable that will store the contacts
#it should be oit of while loop so that data is not cleared on looping 
while True:
	try:
		name = input("Username: ") #get user name
		phonenumber = input("phone number: ") #get number
		location = input("location: ") #get location
		company =  input("company: ") #get company
		#get more details u wish
		
		if (name, phonenumber, location, company): #if data is entered add it to phone book
			contactbook.append({name:[phonenumber, location, company]})
		else: #when not added pass and show book details 
			pass
		for contacts in contactbook:
			print(contacts)
	except Exception as e: #if any error show it
		print(e)

