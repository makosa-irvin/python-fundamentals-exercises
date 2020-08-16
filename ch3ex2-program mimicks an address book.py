#Exercise 2
    #A menu driven that works with an adress book file
        #Menu should have:1)Look up person by last name
                         #2)Add a person to address book
                         #3)Quit




#The menu
menu = input('Welcome to the address book.\nChoose your options:\n'
             '  1) Look up a person by Last name\n'
             '  2) Add a person to the address book.\n'
             '  3) Quit\n'
             'Enter your choice: ')

#choice 1
if menu == '1':
    #user inputs name
    last_name = input('Enter any name >')
    #open the file to read it
    option1_file = open('addressbook.txt', 'r')

    #iterate over
    for line in option1_file:
        all_lines = line.rstrip('\n')

    #Should check if last name in address book and print the address
        if last_name in all_lines:


            print(all_lines)
            street = option1_file.readline().rstrip('\n')
            print(street)
            citystatezip = option1_file.readline().rstrip('\n')
            print(citystatezip)
            homephone = option1_file.readline().rstrip('\n')
            print(homephone)
            mobilephone = option1_file.readline().rstrip('\n')
            print(mobilephone)

    option1_file.close()



#choice2
    #add a person in address book
if menu == '2':
    option2_file = open('addressbook.txt', 'a')
    option2_file.write('\n' + input('Enter the name of the person: ') + '\n')
    option2_file.write(input('Enter the street address of the person: ')+ '\n')
    option2_file.write(input('Enter the city, state and zip of the person: ')+ '\n')
    option2_file.write(input('Enter the home phone number of the person')+ '\n')
    option2_file.write(input('Enter the mobile number of the person')+ '\n')

    option2_file.close()

#option 3
    #quit
if menu == '3':
    print('You are exiting the address book')

else:
    print('Incorrect entry')




