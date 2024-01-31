import csv
import math

# -------------------------------------------------------------------------------------------------------------
# lists
ID = []
Name = []
StudyHours = []
Score = []

# -------------------------------------------------------------------------------------------------------------
# Welcome funtion
def Welcome():
    print("""
    
    HELLO THIS IS A SIMPLE DATA ANALYSIS SYSTEM
    written in python programming language 
    
    """)

# -------------------------------------------------------------------------------------------------------------
# The Menu "it will return the value to choose another function"
def Menu():
    print("""Choose from the list below :- 
    
        1. Read data
        2. List data
        3. Show Grades
        4. Search
        5. Statistics
        6. Regression Analysis
        7. Prediction 
        8. Exit
        """)
    temp = input("Enter a number of the process you want to make : ")
    return temp


# -------------------------------------------------------------------------------------------------------------
# Calculate Mean, Variance, Standard deviation and RegressionEquation after the file reading
def Calculate():
    # -----------------Global variables--------------------------
    global MeanHours
    global MeanScore
    global VarH
    global VarS
    global SHours
    global SScore
    global b0
    global b1
    # ------Assigning 0 to all variables to do a full calculation if another file requested--------
    b0 = 0
    b1 = 0
    MeanHours = 0
    MeanScore = 0
    VarH = 0
    VarS = 0
    SHours = 0
    SScore = 0
    temp1 = 0
    temp2 = 0
    DataLen = len(StudyHours)
    # -----------------Mean calculation-------------------------
    for i in range(DataLen):
        if i == 0:
            continue
        else:
            temp1 += int(StudyHours[i])
            temp2 += int(Score[i])
    MeanHours = round(temp1 / (DataLen - 1), 2)
    MeanScore = round(temp2 / (DataLen - 1), 2)
    # ------------Variance and standard deviation---------------
    # ------------Variance------------
    temp1 = 0
    temp2 = 0
    for i in range(DataLen):
        if i == 0:
            continue
        else:
            temp1 += (int(Score[i]) - MeanScore) ** 2
            temp2 += (int(StudyHours[i]) - MeanHours) ** 2
    VarS = round(temp1 / (DataLen - 2), 3)
    VarH = round(temp2 / (DataLen - 2), 3)
    # -------Standard Deviation--------
    SHours = round(math.sqrt(VarH), 3)
    SScore = round(math.sqrt(VarS), 3)
    # -----------------Regression Equation---------------------
    temp1 = 0
    temp2 = 0
    for i in range(DataLen):
        if i == 0:
            continue
        else:
            temp1 += int(StudyHours[i]) * int(Score[i])
            temp2 += int(StudyHours[i]) * int(StudyHours[i])
    temp1 = temp1 - ((DataLen - 1) * MeanScore * MeanHours)
    temp2 = temp2 - ((DataLen - 1) * (MeanHours * MeanHours))
    # -------Final result of b0 and b1-------
    b1 = round((temp1 / temp2), 3)
    b0 = round(MeanScore - (b1 * MeanHours), 3)

# -------------------------------------------------------------------------------------------------------------
# Reading File function and storing it in global lists
def Read():
    i = 0
    FileName = input("Enter a file name:- ") + ".csv"
    File = open(FileName)
    data = csv.reader(File)
    for row in data:
        ID.append(row[0])
        Name.append(row[1].lower())
        StudyHours.append(row[2])
        Score.append(row[3])
        i += 1
    print("Data has been read successfully\n\n")
    # Calculate values (mean, var, standard deviation and regression equation)
    Calculate()


# -------------------------------------------------------------------------------------------------------------
# Function that lists all students data
def List():
    dash = '-' * 54
    for i in range(len(ID)):
        if i == 0:
            print(dash)
            print('{:<10s}{:<30s}{:<8s}{:<12s}'.format(ID[i], Name[i], StudyHours[i], Score[i]))
            print(dash)
        else:
            print('{:<10s}{:<30s}{:<8s}{:<12s}'.format(ID[i], Name[i], StudyHours[i], Score[i]))


# -------------------------------------------------------------------------------------------------------------
# Print a table of Students and their Grades
def Grades():
    dash = '-' * 54
    for i in range(len(ID)):
        if i == 0:
            print(dash)
            print('{:<10s}{:<30s}{:<12s}'.format(ID[i], Name[i], "Grade"))
            print(dash)
        else:
            print('{:<10s}{:<30s}{:<12s}'.format(ID[i], Name[i], GradeOfStudent(int(Score[i]))))


# -------------------------------------------------------------------------------------------------------------
# Used in Grades function to Grade each student and return his grade
def GradeOfStudent(score):
    if 100 >= score >= 90:
        return "A"
    elif 90 > score >= 75:
        return "B"
    elif 75 > score >= 60:
        return "C"
    elif 60 > score >= 50:
        return "D"
    elif score < 50:
        return "F"
    else:
        return "Wrong entry"


# -------------------------------------------------------------------------------------------------------------
# Search for a name by typing a part of it or the full name
def Search():
    dash = '-' * 54
    SearchName = input("Enter Student's Name: ")
    SearchName = SearchName.lower()
    print(dash)
    print('{:<10s}{:<30s}{:<8s}{:<12s}'.format(ID[0], Name[0], StudyHours[0], Score[0]))
    print(dash)
    for i in range(len(ID)):
        if Name[i].find(SearchName) > -1:
            print('{:<10s}{:<30s}{:<8s}{:<12s}'.format(ID[i], Name[i], StudyHours[i], Score[i]))


# -------------------------------------------------------------------------------------------------------------
# Print Statistics
def Statistics():
    print(f"""
        Mean of Study Hours = {MeanHours}
        Variance of Study Hours = {VarH}
        Standard deviation of Study Hours =  {SHours}
        
        ********************************************************
        
        Mean of the Score = {MeanScore}
        Variance of the Score = {VarS}
        Standard deviation of the Score = {SScore}
        """)


# -------------------------------------------------------------------------------------------------------------
# print the Regression Equation formula
def RegEquation():
    print(f"""Regression Equation is : Y= {b0} + {b1}X
    """)


# -------------------------------------------------------------------------------------------------------------
# print the prediction value
def Prediction():
    X = int(input("Enter the number you want to predict : "))
    print(f"""
    Y={b0 + (b1 * X)}
    """)


# Main program----------------------------------------
Welcome()
# while loop to keep the program working until termination
while (1):
    NumberOfMenu = Menu()
    if NumberOfMenu == "1":
        Read()
        print("----------------------------------------------------------------")
    elif NumberOfMenu == "2":
        List()
        print("----------------------------------------------------------------")
    elif NumberOfMenu == "3":
        Grades()
        print("----------------------------------------------------------------")
    elif NumberOfMenu == "4":
        Search()
        print("----------------------------------------------------------------")
    elif NumberOfMenu == "5":
        Statistics()
        print("----------------------------------------------------------------")
    elif NumberOfMenu == "6":
        RegEquation()
        print("----------------------------------------------------------------")
    elif NumberOfMenu == "7":
        Prediction()
        print("----------------------------------------------------------------")
    elif NumberOfMenu == "8":
        break
    else:
        print("Please Enter a correct value")
        NumberOfMenu = Menu()
