print()
print("Welcome to Library Book Reading Schedule Calculator!")
print()

title = input("What is the title of your library book? ")
start = input("Have you started reading your book? (yes/no): ")

while(True):
	if(start == "yes"):
		pagesRead = input("How many pages have you read so far? ")
		pages = input("Please enter how many pages your book has: ")
		pages = int(pages) - int(pagesRead)
		break
	if(start == "no"):
		pages = input("Please enter how many pages your book has: ")
		break
	else:
		print("I'm sorry, can you enter either yes or no to the previous questions")



from datetime import date


def daysBetween(date1, date2):
	if date2 > date1: 
		return (date2-date1).days
	else:
		return (date1-date2).days


print()
todaysDate = input("Please enter today's date (mm/dd/yyyy): ")
isLeapYear = False
if(todaysDate[0] == "0" and todaysDate[1] == "2"):
	leapYear = input("Is the current year a leap year? (yes/no) : ")
	if(leapYear == "yes"):
		isLeapYear = True
	
print()
dueDate = input("Please enter your book's due date (mm/dd/yyyy): ")
print()


#Convert current date input into integers
if(todaysDate[0] == "0"):
	CurrentMonthVal = int(todaysDate[0]) + int(todaysDate[1])
else:
	CurrentMonthVal = int(todaysDate[0] + todaysDate[1])


if(todaysDate[3] == "0"):
	CurrentDayVal = int(todaysDate[3]) + int(todaysDate[4])
else:
	CurrentDayVal = int(todaysDate[3] + todaysDate[4])

CurrentYearVal = int(todaysDate[6] + todaysDate[7] + todaysDate[8] + todaysDate[9])




#Convert due date input into integers 
if(dueDate[0] == "0"):
	DueMonthVal = int(dueDate[0]) + int(dueDate[1])
else:
	DueMonthVal = int(dueDate[0] + dueDate[1])


if(dueDate[3] == "0"):
	DueDayVal = int(dueDate[3]) + int(dueDate[4])
else:
	DueDayVal = int(dueDate[3] + dueDate[4])

DueYearVal = int(dueDate[6] + dueDate[7] + dueDate[8] + dueDate[9])



date1 = date(CurrentYearVal, CurrentMonthVal, CurrentDayVal)
date2 = date(DueYearVal, DueMonthVal, DueDayVal)
readingTime = daysBetween(date1, date2)

#Option to give user a break from reading 
pacer = input("Would you like a break from reading after a certain number of days? (yes/no): ")
if(pacer == "yes"):
	pacerAmount = input("After how many days would you like a reoccuring break? ")
	readingTime = readingTime - (readingTime / int(pacerAmount)) 
	print()
	print()
	print("Calculating...")
	print()
if(pacer == "no"):
	print("Ok! I will calculate the amount of pages you should read each day to be on track before your book's due date.")
	print()
	print()
	print("Calculating...")
	print()

	

pagesPerDay = int(int(pages) / readingTime)
print()
if(pagesPerDay == 0 or pagesPerDay < 0):
	print("Sweet! You need to read less than 1 page each day to finish <<", title, ">> before it's due!")
	print("Happy reading!")
elif(pagesPerDay == 1):
	print("Nice! You only need to read 1 page each day to finish <<", title, ">> before it's due!")
	print("Happy reading!")
else:
	print("You will need to read", pagesPerDay, "pages each day you intend to read to finish <<", title, ">> before", dueDate)
	print("Happy reading!")
print()
print("Thank you for using Library Book Reading Schedule Calculator!")
print()




#maybe make a chart like the one in notion 





