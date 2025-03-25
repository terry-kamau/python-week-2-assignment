#create an empty list
my_list = []
print("empty list:" ,my_list)
#add the numbers 10, 20, 30, 40 using append ()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("list after appending 10,20,30,40:" ,my_list)
#insert the value 15 at the second position of the list
my_list.insert(1 ,15)
print("list after inserting 15 at the second position:" ,my_list)
#Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print("list after extending with 50,60,70:" ,my_list)
#Remove the last element from my_list.
my_list.pop(-1)
print("list after removing the last element:" ,my_list)
#Sorting my_list in ascending order.
my_list.sort()
print("list after sorting in ascending order:" ,my_list)
#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index (30)
print("index of 30:" ,index_of_30)