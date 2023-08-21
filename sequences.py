#sequence of strings
name = "sunil"
print(name[0])

#sequence of list []
#mutable values
names = ["Sunil", "Harry", "robert"]

print(names[1])
names.append("Darke")
names.sort()
print(names)
#tuple related unit () grouping values together
# is immutable
coordinate = (10.0, 5.0)

print(coordinate[1])

#set
#create empyt set
s= set()
s.add(2)
s.add(4)
s.add(8)
s.add(2)
#2 is not added again
# there is no guranteed order
print(s)
print(f"The set has {len(s)} elements" )
#Collection of unique values

#dict
#key value pairs