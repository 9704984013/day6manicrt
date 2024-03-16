#q1:
##s1 = input("enter string:")
##fst=s1[0].upper()
##lst=s1[-1].upper()
##print(fst+s1[1:len(s1)-1]+lst)

#q2:
##n = 128
##temp = n
##f1 = 0
##while n!=0:
##    rem = n%10
##    check = temp%rem
##    if check!=0:
##        f1 = 0
##    n = n//10
##
##if f1==0:
##    print("yes")
##else:
##    print("no")

##l1 = [8, 9, 0, 7]
##l2 = [7, 6, 5, 4]
##l3 =[]
##print(l1[0]+l2[0], l1[1]+l2[1])
##
##for val in range(len(l1)):
##    ans = l1[val]+l2[val]
##    l3.append(ans)
##print(l3)

# ! ------>set

# ! ---> character of list
##? charctristics of set
##1.) set can be treated using {}
##2.) the elements inside set are not indexed
##3.) does not allow duplicate values
##4.) it unordered----> accept the only unmutable datatypes
##5.) heterogenous
##6.) mutable or changable


# Eg:1,
##s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
##print(s1)

# Eg:2,
##s2 = {5, 8, 98, [9, 0]}
##print(s2)------>error

# Eg:3,
# min(), max(), len()

# Eg:4,
# ? to add element inside set
#s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
#print(s1)

# update()
##s1.update(9, 0)
##print(s1)

#To deleat element inside set

#s1 = {8, 78, 67, 'u'}

#pop() # to deleat one element randomly
##s1.pop()
##print(s1)
##
##remove()
##s1.remove(78)
##
##print(s1)

#discard()
##s1.discard(67)
##print(s1)

#clear()
##l1 = []
##print(type(l1))------>datatype is dictonary

#s1 = set() #to creat empty set
#print(type(s1))

##s1 ={8, 9, 0}
##s1.clear()
##print(s1)
###del s1
##print(s1)


# joining the set
##s1 = {9, 0, 8}
##s2 = {9.90, "card", 't', 56}
# union()-----> to combine 2 set
##s3 = s1.union(s2)
##print(s3)

#intersection()-------> to get common elements inside set
##s1 = {4, 5, 6}
##s2 = {5, 6, 7, 8}
##print(s1.inserset(s2))

# difference()
##s1 = {4, 5, 6}
##s2 = {5, 6, 7, 8}
##print(s1.difference(s2))
##print(s2.difference(s2))
##print(s1.symmetric_difference(s2))

#isdisjoint(), issubset(), issuperset

##s1 = {8, 9, 0}
##s2 = {6, 7, 5, 8, 9, 0}
##print(s1.issubset(s2))
##print(s2.issuperset(s1))

# 0/p ---> Its a joinset
##s1 = {1, 2, 3, 4, 5}
##s2 = {3, 2, 7, 8, 9}
##
##for val in s1:
##    if val in s2:
##        str1 = "Its joint set"
##print(str1)

# !-----> dictionary

#Eg:1;

##d1 = {1:100, 'a':200, 4.5:"hello"}
##print(d1)
##print(len(d1))

#Eg:2;
##mech_name="name1", name "name"]
##mech_age [23,22,24]
##mech_mark [89, 78, 60]
##mech_email = ["name2@gmail.com", "name3@gmail.com"]

# ? char of dictinory
##1.) have to be surrounded by {}
##2.) It have to be in form of key, value pair
##3.) It is mutable
##4.) duplicate keys are not allowed, duplicate values are allowed
##5.) It is unindexed
##6.) It is ordered
##7.) key does not allow mutable datatypes, values allow mutable datatypes

#d1 = {1:100, 2:200, 3:300, 4:400}
# * to access element in dictionary

##print(d1)
##or
##To access the values, have to use key
##print(d1[1]) # 0/p---> 100

# ? some common functions
##len(), min, max()
##print(min(d1)
##print(max(d1))
      
# To find min, max, based on values
##print(min(d1.values()))
##print(max(d1.values()))

# ? dictionary based functions
# to add element(key and value pair) in dict
##d1 = {1:100, 2:200, 3:300, 4:400}
##d1[5] = 500
##print(d1)

# ? To replace a value in dictionary
##d1 = {1:100, 2:200, 3:300, 4:400}
##d1[2] = "mango"
##print(d1)

# ? delete element from dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
# popitem() # ----> to delete last key value pair in dist
# d1.popitem()
#print(d1)

##pop()
##d1.pop(2) # 2 is the key dictionary
##print(d1)

# clear(), del

# * join 2 dictionary

# update
##d1= (1:100, 2:200, 3:308, 4:400)
##d2 =("a":"apple", "b": "boy","g":"game")
##d1.update(d2)
##    print(d1)

# get()
##d1 = {1:100, 2:200, 3:300, 4:400}
##print(d1[90])
##print(d1.get(90))


# to print all the keys
##print(d1.keys())
##print(type(d1.keys())
##
##to print all the values
##print(d1.values())

# * Iterating dictionary
##for val in d1:
##    print(val)

##for val in d1.values(): # to iterate values alone
##    print(val)
    
#to get both key and values
##for key, val in d1.items():
##      print(key, val)


# ! problem:1;

##n = int(input("enter no of times"))
##integer=[]
##float_value=[]
##string=[]
##
##for val in range(n):
##    val= eval(input("enter the value: "))
##    if type(value)==int:
##        integer.append(value)
##    elif type (value)==float:
##        float_value.append(value)
##    elif type(value)==str:
##        string.append(value)
##    else:
##        print("pls provide data in int, float, string")
##print(integer)
##print(float_value)
##print(string)

#Return a set of elements present in Set A or B, but not both
##s1 = {10, 20, 30, 40, 50}
##s2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

##for val in s1:
##   if val in s2:
##     str1 = "20, 70, 10, 60"
##print(str1)

##set3 set()
##for val in set1:
##  if val not in set2:
##    set3.add(val)
##for val in set2:
##    if val not in set1:
##    set3.add(val)

# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

# ! -------->problem 3
##l1 = [1,2,3,4]
##l2 = ["a","b","c","d"]
##for val in range(len(l1)):
## d1.(l1[val]) =l2[val]
##d1[l1[2]] =l2[2]
##d1[l1[3]] =l2[3]
##d1[l1[4]] =l2[4]
#print(d1)




   
