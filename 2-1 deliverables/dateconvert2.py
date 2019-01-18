# dateconvert2.py
# Created by Jenna Folsom on 1/17/19
# This program converts the month, date, and year into number and word form.

def main():

    # This is an introduction
    print("This program converts the month, date, and year into number and word form.")
    
    # get the day month and year as numbers
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year (yyyy): "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    date2 = monthStr+" " + str(day) + ", " + str(year)
    
    # This is an outro
    print("The date is {0} or {1}.".format(date1, date2))

main()
