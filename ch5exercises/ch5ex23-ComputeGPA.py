#Exercise 23
    #Compute a user GPA.Should have a function that takes in parallel lists and compute average

def computeAverage(lstCredit,lstGrade):
    

    total_credits = sum(lstCredit)
    grade_products = 0

    for i in range(len(lstCredit)):
        credit_grade = lstCredit[i]*lstGrade[i]
        grade_products += credit_grade

    #compute
    gpa = grade_products / total_credits
    print('Your GPA is',str(gpa))
    return

def get_gradeValuencredit():
    grading = { 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,'B-':2.7,
           'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0}

    gpa_creditList = []
    grade_valueList = []

    gpa_credit = int(input('Credits? '))
    while gpa_credit != 0:
        gpa_grade = input('Grade? ')
        #Check value of grade
        grade_value = grading[gpa_grade]

        gpa_creditList.append(gpa_credit)
        grade_valueList.append(grade_value)

        gpa_credit = int(input('Credits? '))

    return computeAverage(gpa_creditList,grade_valueList)

get_gradeValuencredit()     

