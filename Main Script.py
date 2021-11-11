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
roundGrades = np.array([-3,0,2,4,7,10,12])

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
    
    # The input is converted to a pandas matrix and a numpy array
    pdGrades = pd.read_csv(grades, delimiter=";", header=None)
    npGrades = np.array(pdGrades)
    
    # An empty array is created, which is going to contain the final grade for each student
    gradesFinal = np.zeros(np.shape(npGrades)[0])
    
    # Creating a for loop that goes through all the rows
    for i in range (len(npGrades)):
        
        # If a student is given at least one -3 for an assignment, the final grade is set to -3
        if -3 in npGrades[i,:]:
            gradesFinal[i] = -3
        
        # If a student is given just one grade, that is the final grade for that student
        if len(npGrades) == 1:
            
            gradesFinal[i] = npGrades[i]
            
        # If a student is given more than one grade, the lowest grade is removed and the mean is computed from the remaining
        else:
            
            # An empty array is created
            lowestRemoved = np.zeros(np.shape(npGrades)[1]-1)    
            
            # Creating a for loop that goes through all the grades of the i'th student
            for j in range(np.shape(npGrades)[1]-1):
                
                # The lowest grade for the i'th student is assigned a variable
                lowestGrade = np.min(npGrades[i,:])
                
                # Putting all the grades except the lowest grade into an array
                if npGrades[i,j] != lowestGrade:
                    lowestRemoved[j] = npGrades[i,j]
            
            # Computing the mean grade, having removed the lowest grade, for each student, and putting them into an array
            gradesFinal[i] = np.mean(lowestRemoved)
            
            # Using the roundGrade function to round the mean grades for each student
            gradesFinal = roundGrade(gradesFinal)
        
    return gradesFinal

print(computeFinalGrades("test1.csv"))


# =============================================================================
# 3: Grades Plot function:
# =============================================================================
# def gradesPlot(grades):


plotData = computeFinalGrades("test1.csv")
l = np.zeros(len(roundGrades))
for i in range(len(roundGrades)):
    l[i] = np.sum(plotData == roundGrades[i])
    

# Designing and running the plot
colors = ["r","g","b","m","c","peru","yellow"]
for i in range(len(roundGrades)):
    plt.bar(str(roundGrades[i]), l[i], color=colors[i])

plt.title("Final grades")
plt.xlabel("Grade on the 7-step scale")
plt.ylabel("Number of students")
plt.xlim([-0.5, 7])
plt.ylim([0, np.max(l)+0.3])
plt.show()




#     return



# =============================================================================
# 4: Main Script
# =============================================================================
