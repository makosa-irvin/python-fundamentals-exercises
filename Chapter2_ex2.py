#Exercise 2
    #Write a grading program

#Incase user fails to input a number
try:
#Prompt user for percentage of points
    user_percentage = float(input('Please enter your percentage achieved in the class: '))


#grading system scale
    if user_percentage >= 101:
        print('Incorrect percentage')
    elif user_percentage >= 93.33 :
        print('A')

    elif user_percentage >= 90:
        print('A-')

    elif user_percentage >= 86.67:
        print('B+')

    elif user_percentage >= 83.33:
        print('B')

    elif user_percentage >= 80:
        print('B-')

    elif user_percentage >= 76.67:
        print('C+')

    elif user_percentage >= 73.33:
        print('C')

    elif user_percentage >= 70:
        print('C-')

    elif user_percentage >= 66.67:
        print('D+')

    elif user_percentage >= 63.33:
        print('D')

    elif user_percentage >= 60:
        print('D-')

    elif user_percentage <= 60:
        print('F')


except ValueError:
    print('You have not entered a number')