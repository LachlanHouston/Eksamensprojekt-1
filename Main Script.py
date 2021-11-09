"""
Exam Project - Program for grading students
(02631) Introduction to Programming and Data processing
By: Lachlan Houston (s214593) og Frederik Ravnborg (s204078)
Due: 03/12/2021
"""

import numpy as np

# =============================================================================
# 1: Round Grade function:
# =============================================================================
def roundGrade(grades):
    
    possibleGrades = np.array([-3,0,2,4,7,10,12])
    gradesRounded = np.zeros(len(grades))
    smallestDifIndex = np.zeros(len(grades))
    for i in range(len(grades)):
        
        dif = np.abs(possibleGrades - grades[i])
        smallestDifIndex[i] = dif.argmin()
        gradesRounded[i] = possibleGrades[int(smallestDifIndex[i])]
    return gradesRounded
 
print(roundGrade(np.array([-2,0,3,5,5,6,6,2.3,6,3,7,9,11,12])))



"""
# =============================================================================
# 2: Final Grade function:
# =============================================================================
def computeFinalGrades(grades):
    
    
    
    return gradesFinal



# =============================================================================
# 3: Grades Plot function:
# =============================================================================
def gradesPlot(grades):
    



# =============================================================================
# 4: Main Script:
# =============================================================================
"""
