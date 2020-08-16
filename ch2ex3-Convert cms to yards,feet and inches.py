#Exercise 3
    #Converts centimeters to yards, feet and inches

#user inputs cm
cm = float(input('How many centimeters do you need to convert >'))
yard = cm // 91.44
rem1 = cm % 91.44
foot = (rem1)//30.48
rem2 = rem1 % 30.48
inches = rem2/2.54

#should print yard if one yard and yards when many also no yard should be printed if none
#sama thing to apply in feet

if yard == 1:
    yard_count = '{} yard, '.format(yard)
elif yard > 1:
    yard_count = '{} yards, '.format(yard)

else:
    yard_count = ''

if foot == 1:
    foot_count = '{} foot, '.format(foot)
elif foot > 1:
    foot_count = '{} feet, '.format(foot)

else:
    foot_count = ''


print('This is {}{}{}inches'.format(yard_count, foot_count, inches))

