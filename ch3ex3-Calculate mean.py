#Exercise 3
    #Finding the mean

#user enters list
numbers = input('Please enter a list of numbers: ')
num_list = numbers.split(' ')
#for exercise 5 and 7 -> reverse a list
#ex 5
num_list_rev = num_list[::-1]
print(num_list_rev)

#ex7
num_list_rev[::-1]
print(num_list_rev)

#finding the count and the sum
count = 0
sum_numbers = 0
for num in num_list:
  num = float(num)
  sum_numbers += num
  count += 1

#average
avg_num = sum_numbers / count
print(count, sum_numbers, avg_num)


