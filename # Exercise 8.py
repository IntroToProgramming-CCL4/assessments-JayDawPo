# Exercise 8
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Enter name to search: ")

found = False
for name in names:
    if name == search_name:
        found = True

if found == True:
    print(search_name + " is in the list.")
else:
    print(search_name + " is not in the list.")