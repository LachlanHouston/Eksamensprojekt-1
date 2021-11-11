"""
Exam Project - Program for grading students
(02631) Introduction to Programming and Data processing
By: Lachlan Houston (s214593) og Frederik Ravnborg (s204078)
Due: 03/12/2021
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

roundGrades = np.array([-3,0,2,4,7,10,12])

# =============================================================================
# 1: Round Grade function:
# =============================================================================
def roundGrade(grades):
    
    gradesRounded = np.zeros(len(grades))
    smallestDifIndex = np.zeros(len(grades))
    for i in range(len(grades)):
        
        dif = np.abs(roundGrades - grades[i])
        smallestDifIndex[i] = dif.argmin()
        gradesRounded[i] = int(roundGrades[int(smallestDifIndex[i])])
        
    return gradesRounded
 
# print(roundGrade(np.array([-2,0,3,5,5,6,6,2.3,6,3,7,9,11,12])))



# =============================================================================
# 2: Final Grade function:
# =============================================================================
def computeFinalGrades(grades):

    pdGrades = pd.read_csv(grades, delimiter=";", header=None)
    npGrades = np.array(pdGrades)
    gradesFinal = np.zeros(np.shape(npGrades)[0])
    
    # For loop that goes through all the rows
    for i in range (len(npGrades)):
        
        if -3 in npGrades[i,:]:
            gradesFinal[i] = -3
        
        if len(npGrades) == 1:
            
            gradesFinal[i] = npGrades[i]
            
        else:
            lowestRemoved = np.zeros(np.shape(npGrades)[1]-1)    
            for j in range(np.shape(npGrades)[1]-1):
                
                
                
                lowestGrade = np.min(npGrades[i,:])
                print(lowestGrade)
                if npGrades[i,j] != lowestGrade:
                    lowestRemoved[j] = npGrades[i,j]
                
            gradesFinal[i] = np.mean(lowestRemoved)
            
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
# Main Script:
# =============================================================================
while (True):
    None
    break
