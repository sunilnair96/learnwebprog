thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

#Duplicate values will overwrite existing values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2000,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
print(len(thisdict))
print(type(thisdict))

#use dict class to create dictionary
newdict = dict(name = "John", age = 36, country = "Norway")
print(newdict)