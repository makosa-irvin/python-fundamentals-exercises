#Exercise 10
    #Computes GPA on a 4 point scale
        #Each grade on a 4 point scale is multiplied by number of credits
        #the sum of it is divided by number of credits
        #A=4.0, A-=3.7, B+ ->3.3, B ->3.0, B- ->2.7, C+ ->2.3
        #C ->2.0, C- ->1.7, D+ ->1.3, D ->1.0, D- ->0.7, F ->0

print('This program computes your GPA\n'
        'Please enter your completed courses\n'
        'Terminate your entry by entering 0 credits')

#The number of credits
total_credits = 0

#Sum of all credit,grade products
grade_products = 0

#grades and value
grading = { 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,'B-':2.7,
           'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0}

#the credit
gpa_credit = int(input('Credits? '))
while gpa_credit != 0:
    gpa_grade = input('Grade? ')
    #Check value of grade
    grade_value = grading[gpa_grade]

    #Multiply grade value with credit
    credit_grade = grade_value * gpa_credit

    #Add to the grade, credit product
    grade_products += credit_grade

    #Count the credits
    total_credits += gpa_credit



    gpa_credit = int(input('Credits? '))

gpa = grade_products / total_credits
print('Your GPA is',str(gpa))


