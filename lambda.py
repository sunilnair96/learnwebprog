people = [
    {"name":"Harry", "suburb": 3163},
    {"name":"Mark", "suburb": 3307},
    {"name":"Rob", "suburb": 3137}
]

def f(person):
    return person["name"]
people.sort(key=f)

print(people)

#using lambda 

people.sort(key = lambda  person:person["suburb"] )

print(people)