val = [5 , 2, 4, 3]
#prints
print(val)

#reassigns value
val[1] = "kevin"

#length of list
print(len(val))

#gives values in array
valLength = len(val)
sum = 0
for index in range (0, valLength):
    sum = sum + val[index]
    print(sum)

#does same as above
sum = 0
for value in val:
    sum = sum + value
    print(sum)


#  adds value to end
print(val)
val.append(20)

# #adds -1 to beginning
val.insert(0,-1)
print(val)

# #removes number 3 from list
val.remove(3)
print(val)

#remove value at index 1
print(val)
val.pop(1)
print(val)


#find value in list
if "value" in val:
    print('has value')
