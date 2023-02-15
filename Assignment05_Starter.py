# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ANaidu,2.12.2023,Added code to check for file and then read in rows
# ANaidu,2.13.2023,Read list to dictionary then form a list of dictionaries
# ANaidu,2.14.2023,Add functionality for each option.
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # A string that represents a filename
lstData = ""  # A list of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:     # first check to see that the text file is present
    objFile = open(strFile, "r")
    for row in objFile:
        lstData = row.split(",")       # read data into list
        dicRow = {"Task": lstData[0].strip(), "Priority": lstData[1].strip()}  # read list into dictionary
        lstTable.append(dicRow)   # add dictionary row into list table
    objFile.close()
except FileNotFoundError:
    print("Error: ToDoList.txt doesn't exist in this directory.  Please create and try again.")
    exit(-1)


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for objRow in lstTable:
            print(objRow["Task"], objRow["Priority"])


        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = input("Please enter a new task: ")
        newPriority = input("Please enter the task priority: ")
        newRow = {"Task": newTask, "Priority": newPriority}
        lstTable.append(newRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        removeItem = int(input("Please enter the line number to remove: "))
        lstTable.pop(removeItem-1)
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open(strFile, "w")
        for row in lstTable:
            myKey = row["Task"]
            myValue = row["Priority"]
            objFile.write(myKey + ',' + myValue + '\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
