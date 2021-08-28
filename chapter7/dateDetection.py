import re

dateDetector = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9][0-9][0-9])')  # Regex that looks for dates matching the format DD/MM/YYYY. Days range 01 - 31, Months Range 01 - 12, Years range 1000 - 2999

dates = ['05/13/1995', '09/09/1998', '29/02/2000', '29/02/1900', '29/02/1999', '31/04/2016', '32/05/2012', '01/01/2001', '99/99/9999', '28/08/2021', '01/00/1234', '00/01/1234', '10/10/1010']    # List of dates to be searched through

for currentDate in dates:
    date = dateDetector.search(currentDate) # Runs the current date through the regex search
    
    if date == None:    # If regex search doesn't find anything, print that current item isn't a date and continue to next item
        print(currentDate + ' is not a valid date.')
        continue
    
    if date.group(1) == '00' or date.group(2) == '00': # If month or day are 00, it is not a valid date. Unable to figure out how to get regex to not search this.
        print(currentDate + ' is not a valid date.')
        continue

    # Assigns regex group matches to int variables for easy comparing
    day = int(date.group(1))
    month = int(date.group(2))
    year = int(date.group(3))
    isLeapYear = False
    is30DayMonth = False

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # Checks if current year is a leap year
        isLeapYear = True
    if month in [4, 6, 9, 11]:   # Checks if current month should only have 30 days
        is30DayMonth = True

    # Logic that checks whether the date is valid or not
    if isLeapYear and month == 2 and day > 29:
        print(date.group() + ' is not a valid date.')
    elif not isLeapYear and month == 2 and day > 28:
        print(date.group() + ' is not a valid date.')
    elif is30DayMonth and day > 30:
        print(date.group() + ' is not a valid date.')
    elif day > 31:
        print(date.group() + ' is not a valid date.')
    else:
        print(date.group() + ' is a valid date.')
