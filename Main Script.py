"""
Exam Project - Program for grading students
(02631) Introduction to Programming and Data processing
By: Lachlan Houston (s214593) og Frederik Ravnborg (s204078)
Due: 03/12/2021
"""


import numpy as np
from numpy import random

import pandas as pd
import matplotlib.pyplot as plt


# =============================================================================
# 1: Round Grade function:
    
# A function that takes a vector of grades as input and rounds them to their closest valid grade
# =============================================================================
def roundGrade(grades):
    
    # A zero array is created, which is going to contain the rounded grades
    shapeData = np.shape(grades)
    gradesRounded = np.zeros(shapeData)
    
    # An array is created with all the grades from the 7-step scale
    sevenstepGrades = np.array([-3,0,2,4,7,10,12])
    
    
    # A zero array is created
    smallestDifIndex = np.zeros(len(grades))
    
    # A for loop is created, which goes through all the grades in the function input
    for i in range(len(grades)):
        
        # An array, containing the differences between the i'th element of the function input and each round grade, is created
        dif = np.abs(sevenstepGrades - grades[i])

        # The index of the round grade with the smallest difference to the i'th grade is put into an array
        smallestDifIndex[i] = dif.argmin()
        
        # The round grades corresponding to the indexes are put into an array
        gradesRounded[i] = int(sevenstepGrades[int(smallestDifIndex[i])])
        
    return gradesRounded

# =============================================================================
# 2: Final Grade function:
    
# A function that takes a matrix input and calculates a final grade based on some defined rules
# =============================================================================
def computeFinalGrades(grades):
    
    # A zero array is created, which is going to contain the final grade for each student
    gradesFinal = np.zeros(np.shape(grades)[0])
    shapeData = np.shape(grades)
    
    # Creating a for loop that goes through all the rows
    for i in range (len(grades)):
        
        # If a student is given at least one -3 for an assignment, the final grade is set to -3
        if -3 in grades[i,:]:
            gradesFinal[i] = -3
        
        # If a student is given just one grade, that is the final grade for that student
        if shapeData[1] == 1:
            
            gradesFinal = grades[0]
            
        # If a student is given more than one grade, the lowest grade is removed and the mean is computed from the remaining
        else:
            
            # A zero array is created
            lowestRemoved = np.zeros(np.shape(grades)[1]-1)    
            
            # Creating a for loop that goes through all the grades of the i'th student
            for j in range(np.shape(grades)[1]-1):
                
                # The lowest grade for the i'th student is assigned a variable
                lowestGrade = np.min(grades[i,:])
                
                # Putting all the grades except the lowest grade into an array
                if grades[i,j] != lowestGrade:
                    lowestRemoved[j] = grades[i,j]
            
            # Computing the mean grade, having removed the lowest grade, for each student, and putting them into an array
            gradesFinal[i] = np.mean(lowestRemoved)
            
            # Using the roundGrade function to round the mean grades for each student
            gradesFinal = roundGrade(gradesFinal)
    
    # Returns a vector containing the students final grade
    return gradesFinal

# =============================================================================
# 3: Grades Plot function:
    
# A function that plots two different plots, one visualising final grade scores across all students in data set,
# other visualising grade data over assignments, across all students
# =============================================================================
def gradesPlot(grades):

# Plot 1: Final Grades
    # Creating the data for plot 1 by computing the final grade for each student
    plotData = computeFinalGrades(grades)
    
    # The y-axis is defined as a zero array
    y_axis = np.zeros(len(sevenstepGrades))
    
    # A for loop is used to put the number of occurences of each final grade into the y-axis array
    for i in range(len(sevenstepGrades)):
        y_axis[i] = np.sum(plotData == sevenstepGrades[i])
        
    
    # Creating a list of colors that will be used for each bar in the plot
    colors = ["r","g","b","m","c","peru","yellow"]
    
    # A for loop is used to define the bars in the plot with the round grade on the x-axis and the y-axis being the one we previously defined
    for i in range(len(sevenstepGrades)):
        plt.bar(str(sevenstepGrades[i]), y_axis[i], color=colors[i])
    
    # Designing and running the plot
    plt.title("Final Grades")
    plt.xlabel("Grade on the 7-step scale")
    plt.ylabel("Number of students")
    plt.xlim([-0.5, 6.5])
    plt.ylim([0, np.max(y_axis)+0.3])
    plt.show()

# Plot 2: Grades per Assignment
    # Defining the number of students and the number of assignments as the row and column dimension of of our matrix
    nrOfStudents = np.shape(grades)[0]
    nrOfAs = np.shape(grades)[1]
    
    # Creating an array containing the assignment numbers by using a for loop
    asNr = np.zeros(nrOfAs)
    for i in range(nrOfAs):
        asNr[i] = i+1

    # An empty array is created to be able to contain the x-axis elements
    xAxis = np.array([])
    
    # A for loop, that goes through each assignment, is initiated
    for i in range(nrOfAs):
        
        # Creating an array with the (i+1)'th assignment number repeated as many times as there are students
        asNrX = np.ones(nrOfStudents)*(i+1)
        
        # Appending the array to xAxis so we end up having each assignment number repeated as many times as there are students
        xAxis = np.append([xAxis],[asNrX])
    
    # An empty array is created to be able to contain the y-axis elements    
    yAxis = np.array([])
    
    # A for loop, that goes through each assignment, is initiated
    for i in range(nrOfAs):
        
        # Every grade for the every assignment is added to yAxis
        yAxis = np.append([yAxis],[np.array(grades[:,i])])
    
    # A small number between -0.1 and 0.1 is added to each element of both axes to increase visibility in the plot
    xAxisDeviated = np.array(xAxis + [random.uniform(-0.1,0.1) for i in range(len(xAxis))])
    yAxisDeviated = np.array(yAxis + [random.uniform(-0.1,0.1) for i in range(len(yAxis))])
    
    # An empty array is created to be able to contain the mean grade of each assignment
    AsMean = np.zeros(nrOfAs)
    
    # Using a for loop the mean grade of each assignment is put into the array
    for i in range(nrOfAs):
        AsMean[i] = np.mean(np.array(grades[:,i]))
    
    # Designing and running the plot
    plt.plot(xAxisDeviated,yAxisDeviated,"o")
    plt.plot(asNr,AsMean)
    plt.title("Grades per assignment")
    plt.xlabel("Assignment number")
    plt.ylabel("Grade")    
    plt.legend(["Every assignment of every student", "Mean grade of each assignment"], loc ="upper left")
    plt.ylim([-3.5, np.max(yAxisDeviated)+4])     
    plt.show()


# =============================================================================
# 4: Main Script

# A loop that contains an user interactive menu, that starts with loading specified data, afterwards a choice between loading new data, checking for errors in data,
# generate plots over data, display grade lists sorted alphabetically, and lastly an option to quit the program
# =============================================================================

# Initialize by asking for file name of data
sevenstepGrades = np.array([-3,0,2,4,7,10,12])


while True:
    print("Please input a file name (including .csv)")
    try:
        filename = input()
        pdGrades = pd.read_csv(filename, delimiter=",")
    except FileNotFoundError:
        print("You have entered a incorrect file name, please try again")
    
    else:
        # Split the data file into seperated rows and collumns, and load into a numpy array
        pdGrades = pd.read_csv(filename, delimiter=",")
        npGrades = np.array(pdGrades)
        grades = pdGrades.drop(['StudentID',"Name"],axis = 1)
        grades = grades.reset_index(drop=True)
        grades = np.array(grades)
        
        shapeData = np.shape(grades)
        break


# Main loop initialized
while True:
    
    # Checks whether there are any rows in the data
    if np.shape(grades)[0] == 0:
        print("\nThere are no students in the dataset.")
        while True:
            print("Please input a file name (including .csv)")
            try:
                filename = input()
                pdGrades = pd.read_csv(filename, delimiter=",")
            except FileNotFoundError:
                print("You have entered a incorrect file name, please try again")
            
            else:
                # Split the data file into seperated rows and collumns, and load into a numpy array
                pdGrades = pd.read_csv(filename, delimiter=",")
                npGrades = np.array(pdGrades)
                grades = pdGrades.drop(['StudentID',"Name"],axis = 1)
                grades = grades.reset_index(drop=True)
                grades = np.array(grades)
                
                # Update shapeData and break
                shapeData = np.shape(grades)
                break
    
    # Takes input and directs to where the user wants to go
    print(" ","You have the following options:"," ", "1) Load new data","2) Check for data errors", "3) Generate plots","4) Display list of grades","5) Quit the program",sep='\n')
    userInput = input()
    userInput = userInput.lower()
    print("")
    
    # User can load new data file
    if userInput == "1" or userInput == "load data" or userInput == "load new data":
        while True:
        
            # Ask for filename
            print("Please type the name of the file (including .csv)","\n")
            
            # Load data, if wrong file name given, loop back to user input
            try:
                filename = input()
                pdGrades = pd.read_csv(filename, delimiter=",")
            except FileNotFoundError:
                print("You have entered a incorrect file name, please try again")
            else:
                # Split the data file into seperated rows and collumns, and load into a numpy array
                npGrades = np.array(pdGrades)
                grades = pdGrades.drop(['StudentID',"Name"],axis = 1)
                grades = grades.reset_index(drop=True)
                grades = np.array(grades)
                
                # Redefine matrix shape data
                shapeData = np.shape(grades)
                break
        
    # User can see errors in data file, and can choose whether to delete data with error or not
    elif userInput == "2" or userInput == "check for errors" or userInput == "check for data errors":
        # ID- & Names data are saved seperately for later use
        studentID = npGrades[:,0]
        studentName = npGrades[:,1]
        
        # Further variable declation, anyErrors is used to hide the 'delete data' option when set to false
        # errorIndexID & errorIndexGrades are arrays used to store index locations of data to delete
        npgradesData = np.array(grades)
        anyErrors = False
        errorIndexID = np.array([])
        errorIndexGrades = np.array([])
        
        # A loop to ensure a valid input
        while True:
            
            # A loop that checks through every element of StudentID and replaces duplicates with "error"
            for i in range(len(npGrades)):
                for j in range(len(npGrades)):
                    
                    # Skips comparing elements with themselves
                    if j == i:
                        None
                        
                    # If student ID are identical, set first data entry studentID to 'error' so the pair doesn't get counted twice
                    elif studentID[i] == studentID[j]:
                        print(studentName[i],"and",studentName[j], "have identical student IDs (" + str(studentID[i]) + ")" )
                        studentID[i] = "Error"
                        
                        # Stores the placement of the error in an array
                        errorIndexID = np.append(errorIndexID, i)
                        
                        # Give option to delete studentID errors
                        anyErrors = True
            
            # Saves the shape data in a variable
            shapeData = np.shape(npgradesData)
            
            # A loop that checks through every element and compares it to the list of allowed grades
            for i in range(shapeData[0]):
                for x in range(shapeData[1]):
                    if npgradesData[i,x] not in sevenstepGrades:
                        print(npgradesData[i,x], "is an errornous grade (" + str(studentName[i]) + "'s assignment " + str(x+1) + ")")
                        
                        # Stores the placement of the error in an array
                        errorIndexGrades = np.append(errorIndexGrades, i)
                        
                        # Give option to delete grade errors
                        anyErrors = True
            
            # If errors are detected, gives option to delete data with error from set
            if anyErrors == True:            
                
                # Asks the user if they want to delete the rows with errors
                print("\nDo you want to remove students with errornous grades/IDs?","1) Yes","2) No",sep='\n')
                choice = input()
                choice = choice.lower()
                
                if choice == "1" or choice == "yes":
                    
                    # Removes the rows that contain duplicate studentID's
                    for i in range(len(errorIndexID)):
                        try:
                            pdGrades = pdGrades.drop(errorIndexID[i],axis=0)
                        except KeyError:
                            None
                        else:
                            print("Row ", int(errorIndexID[i]), " has been removed (", studentName[int(errorIndexID[i])], ")",sep='')
                        
                    # Removes the rows with incorrect grade inputs
                    for x in range(len(errorIndexGrades)):
                        try:
                            pdGrades = pdGrades.drop(errorIndexGrades[x],axis=0)
                        except KeyError:
                            None
                        else:
                            print("Row ", int(errorIndexGrades[x]), " has been removed (", studentName[int(errorIndexGrades[x])], ")",sep='')
                    
                    # Resets the index and stores the new data in a numpy array
                    pdGrades = pdGrades.reset_index(drop=True)
                    npGrades = np.array(pdGrades)
                    grades = npGrades[:,2:]
                    
                    # Update matrix shape data
                    shapeData = np.shape(grades)
                    break
            
                # Do nothing if input is "2" or "no"
                elif choice == "2" or choice == "no":
                    None
                    break
                
                # Wrong input given, loop restarts
                else:
                    print("You have entered a wrong input, please try again\n")
            
            elif anyErrors == False:
                print("\nThere are no errors in the data")
                break
                
    # User generates plots and prints them
    elif userInput == "3" or userInput == "plots" or userInput == "generate plots":
        gradesPlot(grades)
    
    # User access list over grades alphabetically sorted with final grade given
    elif userInput == "4" or userInput == "display list" or userInput == "display list of grades":
        
        # Sort an erray based 'npGrades' collumn of names, sorts alphabetically
        sortedArray = npGrades[np.argsort(npGrades[:, 1])]
        
        # Print every data entry in following setup: "Name (string), StudentID (string):" "Every grade assignment: (list)" "Final grade: (number)"
        for i in range(np.shape(sortedArray)[0]):
            print("\n", sortedArray[i,1], " (", sortedArray[i,0],"):", sep="")
            print("    Assignment grades:", sortedArray[i,2:])
            print("    Final grade:", int(computeFinalGrades(sortedArray[:,2:])[i]))
        
    # User quits the program, this is done by breaking out of main loop, ending the program            
    elif userInput == "5" or userInput == "quit" or userInput == "quit the program":
        print("Bye")
        break
    
    # If wrong input is given
    else:
        print("You have entered an incorrect input, please try again")
