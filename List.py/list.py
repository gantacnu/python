# List is the collection of elements with different data type elements.
# list ia the mutable (we can change the value or data after creating list).
# we can decleare list with [ ]
# list has postive index value and negative index value.
# postive start with 0 and negative start with -1.
# postive value start with left to right and negative value right to left.

#  if we  want declare list in runtime then we have to use "eval" and we have decleare [ ] in runtime.
# ex
# L1=[]
# print(type(L1))
# L2=eval(input("enter values"))
# print(L2)
# print(type(L2))

# List methods()
# append()
# extend()
# insert()
# remove()
# pop()
# sort()
# reverse()
# index()
# copy()
# count()
# clear()

 #1 append()
# it adds the elements at the end of list
# l=[2,7,8]
# l.append([4,18,11])
# print(l)
#  or
# l=[2,7,8]
# l.append(88)
# print(l)

# 2.extend()
# # it adds the elements in the list
# q=[5,10,15]
# q.extend([44,22,33])
# print(q)

# 3. insert()
# to insert used for the insert element in the list.
# l=[2,4,6,8,10]
# l.insert(1,24)
# print(l) 
# or
# l=[2,4,6,8,10]
# l.insert(44,88)
# print(l)
# or
# l=[2,4,6,8,10]
# l.insert(-44,88)
# print(l)

# 4.remove()
# its remove the elements.
# s=[2,4,3,3,5]
# s.remove(3)
# print(s)

# 4.pop()
# its remove the elements by using index number
# s=[55,66,65,65,2]
# s.pop()
# print(s)
# s.pop(0)
# print(s)

# 5.sort()
# gives the assending order are elements.
# t=[5,8,2,99]
# t.sort()
# print(t)

# assending order and deassending order.
# t=[5,8,2,99]
# t.sort()
# print(t)
# t.reverse()
# print(t)

# 6. reverse()
# gives the diassending order are elements.
# T=[5,8,2,99]
# T.sort(reverse==true)
# print(T)

# 7.index()
# its print the elements by using index number
# s=[3,5,9,11]
# s.index(2,3)
# print(s)

# 8.copy()
# its copy elements form one list to another list .
# s=[2,4,6,8]
# r=s.copy()
# print(r)

#9.count()
# its count the elements in the list.
# r=[2,4,6,8,8,9]
# r.count(1)
# print(8)

# 10.clea()
# its clear the data.
# T=[5,8,2,2,99]
# T.clear()
# print(T)