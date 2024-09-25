from array import *
my_array = array('i' , [1,2,3,4,5])

#Append any value to the array using append()method
my_array.append(15)
print(my_array)

#Insert any value to the array using insert()method
my_array.insert(4,15)
print(my_array)

#Extend python array using extend() method
array2 = array('i' , [1,22,2])
my_array.extend(array2)
print(my_array)

#Add items from list into array using fromlist() method
array2 =  [1,22342,2]
my_array.fromlist(array2)
print(my_array)

#Remove any array element using remove() method
my_array.remove(15)
print(my_array)

#Remove last array element using pop()method
my_array.pop()
print(my_array)

#Fetch any element through its index using index() method
print(my_array.index(5))

#Reverse a python array using reverse() method
my_2 = my_array.reverse()
print(my_2)

#Get array buffer information through buffer_info() method
print(my_array.buffer_info())

#Check for number of occurences of an element using count() method
print('number of occurences of an element 15:',my_array.count(15))

#Convert an array to string using tostring() method
my_2 = my_array.tostring() 
print(my_2)

#Convert array to a python list with same elements using tolist() method
print(my_array.tolist())

#Append a string to char array using fromstring() method
arr = array('i')
arr.fromstring(my_2)

#Slice Elements from an array
print(my_array[4:6])
