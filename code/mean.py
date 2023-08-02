import numpy as np

#create a list of numbers

numbers = [1,2,3,4,5,6,7,8,9,10]

#calculate the mean

mean = np.mean(numbers)
print("The mean of the list of numbers is: " + str(mean))

#calulate the mean of first 5 numbers

mean = np.mean(numbers[0:5])
print("The mean of the first 5 numbers is: " + str(mean))

#calculate the mean of last 5 numbers

mean = np.mean(numbers[5:10])
print("The mean of the last 5 numbers is: " + str(mean))
