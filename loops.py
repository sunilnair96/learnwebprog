#go through the elements i list and print each element
for i in [0, 1,2,3]:
    print(i)

#range starts from 0 by deafult
x = range(6)
for i in x:
    print(i)
print("Start from 5, increment by 3 , end at 20. 20 is excluded")
x = range(5, 20, 3)    
for i in x:
    print(i)

names = ["Sunil", "Appu", "John"]
for name in names:
    print(name)
    for character in name:
        print (character)