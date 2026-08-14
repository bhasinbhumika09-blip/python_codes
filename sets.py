#sets ---collection of non-repetitive elements (different datatypes can be used)

#d{} --empty dictionary
#e=set() --empty set
#set is ---unordered, inindexed, cannot contain duplicate values, there is no way to change items in set

a={1,4,2,6,5,7,9,8,23,65,21}

print(len(a))

print(a)

a.add(87)
print(a)

a.remove(7)
print(a)

a.pop()   #remove random elements of the set
print(a)

a.intersection({1,5,3,6,7,9,10}) #contains intersection of both sets
print(a)

a.union({12,65,34,87})   #contains union of both seta 
print(a)

a.clear()
print(a)
