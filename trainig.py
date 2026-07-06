#Q1.print index of all the values which are greater than 50
#Q2.sort the array column wise
import numpy as np
new1=np.array([23,34,56,67,78,34,56,787,9,90,7,4,5,6,7,5]).reshape(4,4)
new1.sort()
print(new1)
print(np.where(new1>50))
new1.sort(axis=0)
print(new1)
print(np.argmax(new1,axis=0))
for i in np.nditer(new1):
    print(i)



#write a program to concat two arrays
A=np.array([2,3,4,8])
B=np.array([4,5,6,8])
C=np.concatenate((A,B))
print(C)



#random
import numpy.random as rd


#Variables Assignment
a,b,c=10,20,30
#f-strings(formatting of the strings )
print(f"The value of a:{a} b:{b} c:{c}")

a=b=c=40
print(c)

ch='a'
print(type (ch))#String there is no character type datatype is there in the python.
                #we are writing c modules and attaching it to the python called cython.

n1="20"
word1="Twenty"
sentance1=word1+n1
print(sentance1)


n2=20
word2="Twenty"
sentance2=word1+str(n2)
print(sentance2)

#Assignment Operator(#Increment operators(i++,--i,etc) are supported in python)
i=10
i+=1
print(i)

n=7865
total=0
while(n!=0):
    rem=n%10 #5,6,8,7
    total+=rem #5,10,17,23
    total-=1 #4 ,9,16,22
    n=n//10 #786 ,78,7
    print(f"Sum {total}")

#Program to reverse the number without using the str() function
n1=7865
rev=0
while n1!=0:
    rem=n1%10
    rev=(rev*10)+rem
    n1=n1//10  
print(f"Reverse No: {rev}")

 #import this 

#Infinite Loop
#x=1
#i=0
#while i<=5: #This loop stops when condition becomes false
    #x+=3 #4
    #if x>6:
        #x-=1
        #continue #it helps to skip the execution of the current loop
    #i+=1
    #print(x)
   
x=1
i=0
while i<=5:
    x+=3
    i+=1
    if x>6:
       x-=1
       continue
    print(x)

x=1
i=0
while i<=5:
    x+=3
    i+=1
    if x>6:
       x-=1
       continue
    else:
        print("While Loop False Block")
    print(x)


    #for loop
    for i in range(1,6,2):
        print(i)

# program to print the number 7,6,5,4,3,2,1,0
    for i in range(7,-1,-1):
        print(i,end=" ") # end is used to print the values side by side .
        print("\n")

#Pattern for how nested for loop working
# X O X O
# o X O X
# X O X O
# O X O X
#Program to print the above pattern 
    for i in range (4):
        for j in range(4):
            if((i+j)%2)==0:
                print("X",end="")
            else:
                print("O",end="")
        print("")
       
#COLLECTIONS
# 1.List
# 2.Tuple
# 3.Dictionary
# 4.Set

#List:
# forward indexing    0  1   2  3  4       
data=[10,20,30,40,50]     
#backward indexing    -5  -4  -3  -2 -1

#append is used to add the values at the end of the list
# insert is used to add/insert the values where ever you want


data.append(60)
print(data)

data.insert(1,15)
print(data)

#Update
data[2]=35
print(data)

#Remove
data.pop()  #Removes last value
print(data)

data.pop(4)  #pop removes the index value
print(data)

data.remove(35)  #Remove is used to delete the particular value
print(data)

#READING\

for x in data:
    print(x)

#Leader Number ( Number which is greater than all the previous numbers in the list)
data=[7,9,6,2,5,3]
#o/p-> 3 5 6 9 

data=[7,9,6,2,5,3]
data_len=len(data)
leader_no=data[-1]
print(f"The leader no: {leader_no}",end=" ")
for i in range(data_len -2,-1,-1):
    if data[i]>leader_no:
        leader_no=data[i]
        print(leader_no,end=" ")
      

#Peak number that is greater than its neighbouring number.
data=[7,9,6,2,5,3]
# 5 9 ->o/p

data=[7,9,6,2,5,3]
data_len=len(data)
print("\nPeak Numbers are: ")
if data[0]>data[1]:
    print(data[0],end=" ")

if data[-1]>data[-2]:
    print(data[-1],end=" ")

for i in range(1,data_len -1):
    if data[i]>data[i-1] and data[i]>data[i+1]:
        print(data[i],end=" ")

#List Comprehension
data=[x for x in range(20) if x%2==0]
print("\n",data)

data=[45,71,35,40,55,89]
data=[x-1 for x in data if x%5==0]
print(data)

#Tuple #Properties of Tuple
#it is immutable data 
#it is store the value
#Order of tuple will not change
#we cannot do any sort of operations with the tuple
data=(123456,982335623)
print(type(data))

data=(123456,)
print(type(data))

data=(123456)
print(type(data))

tuple_data=(12,13,14)
list_data = list(tuple_data)
print(list_data)

#SET
#Syntax: Set_data={ }
#set doesnot contains the duplicate values
#It does not print in the order what we have given

set_data={10,15,35,35,40,52}
print(set_data)

set_data={10,65,35,65,40,52,35}
print(set_data)

#SET Operations

a={10,20,30,40,50}
b={20,30,60,70,80}
print(a.intersection(b))
print(a.union(b))
a.add(100)
print(a)
a.pop()  #pop is used to remove the random number in the set
print(a)
a.remove(100)
print(a)

for d in a:
    print(d)

#DICTIONARY
#The data is represented in the form of keys and values
#Syntax: name of syntax={ keys:value}
#duplicate keys are not allowed 

data={"name":"ranji","usn":"A009","usn":"B071","age":100}
print(f"Name :{data['name']}|usn:{data['usn']}|age:{data['age']}")

#Add Value to Dictionary
data['city']="mental hospital dharawad"
print(data)

#Update
data['age']=4990
print(data)

#Remove(pop is used to remove the last data we added)
data.popitem()
print(data)

data.pop("name")
print(data)

#List of Dictionary

data=[
     {"product_name":"iphone 17 pro","category" :"Smart Phone"},
     {"product_name":"Samsung Galaxy A23","category":"Smart Phone"},
     {"product_name":"Air Pods","category":"Ear Phones"}
   ]
print(data)

#display product names that belongs to the category smartphones
for d in data:
    if d['category']=='Smart Phone':
      print(d['product_name'])

ecom_data={"type":"ecommerce",
           "data":{
               "inventory_components":[{"name":"A","qty":"15","ratings":[4.5,4.6,3.9]},
                                        {"name":"B","qty":"25","ratings":[4.7,4.6,4.9]},
                                        {"name":"C","qty":"15","ratings":[3.8,4.2,4.4]} ] 
                                       }
}

#Display average ratings with respect to each product names
for data in ecom_data ['data']['inventory_components']:
   
    ratings_len=len(data['ratings'])
    total_ratings=0
    for ratings_data in data['ratings']:
        total_ratings+=ratings_data

    print(f"Name:{data['name']} | Avg Ratings:{total_ratings/ratings_len}")
   
for data in ecom_data['data'] ['inventory_components']:
    inventory_components_len=len(data['qty'])
    qty=0
    for qty_data in data['qty']:
       qty+=int(data['qty'])
       

    print(f"Total qty:{qty}")  


