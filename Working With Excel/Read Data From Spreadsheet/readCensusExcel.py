"""
This is what the program does:
•	 Reads the data from the Excel spreadsheet.
•	 Counts the number of census tracts in each county.
•	 Counts the total population of each county.
•	 Prints the results.

This means the code will need to do the following:
•	 Open and read the cells of an Excel document with the openpyxl module.
•	 Calculate all the tract and population data and store it in a data structure.
•	 Write the data structure to a text file with the .py extension using the 
pprint module.

"""
import openpyxl, pprint

print("Opening workbook...")

# Load the file to work on
workbook = openpyxl.load_workbook("censuspopdata.xlsx")

# specify the sheet we are to work on
sheet  = workbook["Population by Census Tract"]

# create and empty dictionary to store the data 
countyData = {}

# filling in the above dictionary with each county's pop and tracts
print("Reading rows...")

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop = sheet["D" + str(row)].value

    # make sure the key for this state exists.
    countyData.setdefault(state, {})
    
    # make sure the key for this county in this state xists
    countyData[state].setdefault(county, {"tracts": 0, "pop": 0})
    
    # each row reps one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    
    # Increase the county pop by pop in this census tract
    countyData[state][county]['pop'] += int(pop)   
    
# Open a new text file and write the contents of countyData to it
print("Writing Results...")

# creating a file from which the result is written to can be of any extension
resultFile = open('census2010.txt', 'w')

resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()

print("Done")
