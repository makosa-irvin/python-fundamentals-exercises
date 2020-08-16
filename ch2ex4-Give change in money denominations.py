#Exercise 4
    #Indicates the amount of change to give
    #The change is divided in groups of twenties,ten, fives, ones, quarters, dimes, nickels and pennies

#user inputs cost of item
cost_of_item = 65.64#float(input('Enter the cost of item >'))

#user inputs amount given
amount_given = 100.00#float(input('How much did the person give you >'))

#change to be given
raw_change = amount_given - cost_of_item

#making change
twenties = int(raw_change // 20)
rem_no20 = raw_change % 20

tens = int(rem_no20 // 10)
rem_no10 = rem_no20 % 10

fives = int(rem_no10 // 5)
rem_no5 = rem_no10 % 5

ones = int(rem_no5 // 1)
rem_no1 = rem_no5 % 1

quarters = int(rem_no1 // 0.25)
rem_noqts = rem_no1 % 0.25

dimes = int(rem_noqts // 0.10)
rem_nodms = rem_noqts % 0.10

nickels = (rem_nodms // 0.05)
rem_nonks = rem_nodms % 0.05

pennies = rem_nonks // 0.01

#Using singular and omitting those with 0 values
#for twenties
if twenties == 1:
    twenties_count = '{} twenty\n'.format(twenties)

elif twenties >1:
    twenties_count = '{} twenties\n'.format(twenties)

else:
    twenties_count = ''

#for tens
if tens == 1:
    tens_count = '{} ten\n'.format(tens)

elif tens > 1:
    tens_count = '{} tens\n'.format(tens)

else:
    tens_count = ''

#for fives
if fives == 1:
    fives_count = '{} five\n'.format(fives)

elif fives > 1:
    fives_count = '{} fives\n'.format(fives)

else:
    fives_count = ''


#for ones
if ones == 1:
    ones_count = '{} one\n'.format(ones)

elif ones > 1:
    ones_count = '{} ones\n'.format(ones)

else:
    ones_count = ''

#for quarters
if quarters == 1:
    quarters_count = '{} quarter\n'.format(quarters)

elif quarters > 1:
    quarters_count = '{} quarters\n'.format(quarters)

else:
    quarters_count = ''


#for dimes
if dimes == 1:
    dimes_count = '{} dime\n'.format(dimes)

elif dimes > 1:
    dimes_count = '{} dimes\n'.format(dimes)
else:
    dimes_count = ''

#for nickels
if nickels == 1:
    nickels_count = '{} nickel\n'.format(nickels)

elif nickels > 1:
    nickels_count = '{} nickels\n'.format(nickels)

else:
    nickels_count = ''


#for pennies
if pennies == 1:
    pennies_count = '{}penny'.format(pennies)

elif pennies > 1:
    pennies_count = '{}pennies'.format(pennies)

else:
    pennies_count = ''


print(ones_count)

print('The bills of change should be:\n{}{}{}{}{}{}{}{}'.format(twenties_count,tens_count,fives_count,ones_count,quarters_count,dimes_count,nickels_count,pennies_count))

