"""
Exam Project - Program for grading students
(02631) Introduction to Programming and Data processing
By: Lachlan Houston (s214593) og Frederik Ravnborg (s204078)
Due: 03/12/2021
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# An array is created with all the grades from the 7-step scale

# =============================================================================
# 1: Round Grade function:
# =============================================================================
def roundGrade(grades):
    
    # An empty array is created, which is going to contain the rounded grades
    gradesRounded = np.zeros(len(grades))
    
    # An empty array is created
    smallestDifIndex = np.zeros(len(grades))
    
    # A for loop is created, which goes through all the grades in the function input
    for i in range(len(grades)):
        
        # An array, containing the differences between the i'th element of the function input and each round grade, is created
        dif = np.abs(roundGrades - grades[i])
        
        # The index of the round grade with the smallest difference to the i'th grade is put into an array
        smallestDifIndex[i] = dif.argmin()
        
        # The round grades corresponding to the indexes are put into an array
        gradesRounded[i] = int(roundGrades[int(smallestDifIndex[i])])
        
    return gradesRounded
 
#print(roundGrade(np.array([-2,0,3,5,5,6,6,2.3,6,3,7,9,11,12])))



# =============================================================================
# 2: Final Grade function:
# =============================================================================
def computeFinalGrades(grades):
    
    # An empty array is created, which is going to contain the final grade for each student
    gradesFinal = np.zeros(np.shape(grades)[0])
    
    # Creating a for loop that goes through all the rows
    for i in range (len(grades)):
        
        # If a student is given at least one -3 for an assignment, the final grade is set to -3
        if -3 in grades[i,:]:
            gradesFinal[i] = -3
        
        # If a student is given just one grade, that is the final grade for that student
        if len(grades) == 1:
            
            gradesFinal[i] = grades[i]
            
        # If a student is given more than one grade, the lowest grade is removed and the mean is computed from the remaining
        else:
            
            # An empty array is created
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
        
    return gradesFinal

# =============================================================================
# 3: Grades Plot function:
# =============================================================================
def gradesPlot(grades):

# Plot 1: Final Grades
# =============================================================================

    l = np.zeros(len(roundGrades))
    for i in range(len(roundGrades)):
        l[i] = np.sum(grades == roundGrades[i])
        
    
    # Designing and running the plot
    colors = ["r","g","b","m","c","peru","yellow"]
    for i in range(len(roundGrades)):
        plt.bar(str(roundGrades[i]), l[i], color=colors[i])
    
    plt.title("Final Grades")
    plt.xlabel("Grade on the 7-step scale")
    plt.ylabel("Number of students")
    plt.xlim([-0.5, 7])
    plt.ylim([0, np.max(l)+0.3])
    plt.show()
    
    return



# Plot 2: Grades per Assignment
# =============================================================================

# pdGrades = pd.read_csv("test1.csv", delimiter=";", header=None)
# npGrades = np.array(pdGrades)

# dim0 = np.shape(npGrades)[0]
# dim1 = np.shape(npGrades)[1]

# # Number of assignments on the x axis
# Assignment_nr = np.zeros(np.shape(npGrades)[1])
# for i in range(len(Assignment_nr)):
#     Assignment_nr[i] = i+1

# # Going through students
# for i in range(dim0):
    
#     # Going through assignments
#     for j in range(dim1):
#         xy = np.array(Assignment_nr[j],npGrades[j,i])
# print(xy)





#     return



# =============================================================================
# 4: Main Script
# =============================================================================
while True:   
    print("Start")
    # The input is converted to a pandas matrix and a numpy array
    pdGrades = pd.read_csv("test1.csv", delimiter=",")
    npGrades = np.array(pdGrades)
    roundGrades = np.array([-3,0,2,4,7,10,12])
    
    errorIndexID = np.array([])
    errorIndexGrades = np.array([])
    
    studentID = npGrades[:,0]
    print(studentID)
    
    gradesData = pdGrades.drop(['StudentID',"Name"],axis = 1)
    npgradesData = np.array(gradesData)
    
    print(" ","You have the following options:"," ", "1) Load data from file","2) See errors in data", "3) Generate data plots from file data","5) Quit the program",sep='\n')
    userInput = input()
    
    # If user chooses "2", lets them see errors and remove them
    if userInput == "2":
        
        # 
        while True:
            for i in range(len(npGrades)):
                for j in range(len(npGrades)):
                    if j == i:
                        None
                    elif studentID[i] == studentID[j]:
                        print("Row",i,"and row",j, "are identical")
                        studentID[i] = "Error"
                        errorIndexID = np.append(errorIndexID, i)
            
            shape = np.shape(npgradesData)
            
            for i in range(shape[0]):
                for x in range(shape[1]):
                    if npgradesData[x,i] not in roundGrades:
                        print(npgradesData[x,i], "is an errornous grade type")
                        errorIndexGrades = np.append(errorIndexGrades, x)
            print(errorIndexGrades)
            print("Do you want to delete the errornous rows/collumns?","1) Yes","2) No",sep='\n')
            choice = input()
            if choice == "1" or choice == "yes":
                for i in range(len(errorIndexID)):
                    try:
                        pdGrades = pdGrades.drop(errorIndexID[i],axis=0)
                    except KeyError:
                        None
                    else:
                        print("Row", errorIndexID[i], "has been removed")
                    
                for x in range(len(errorIndexGrades)):
                    try:
                        pdGrades = pdGrades.drop(errorIndexGrades[x],axis=0)
                    except KeyError:
                        None
                    else:
                        print("Row", errorIndexGrades[x], "has been removed")
            
                pdGrades = pdGrades.reset_index(drop=True)
                npGrades = np.array(pdGrades)
                break
                
            elif choice == "2" or choice == "no":
                None
                break
                
            else:
                print("You have entered a wrong input, please try again")
    
    print(npGrades)
    
    if userInput == "3":
        gradesPlot(npGrades)

    
    if userInput == "5":
        break
