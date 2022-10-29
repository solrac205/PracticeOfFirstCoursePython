# Lists, Tuples, Dictionaries

# The Lists Python can save data of different types.
# The Lists Python can automatically expand.

FirstList = [10, 20, 30, 40, 50, 60]

for i in range(len(FirstList)):
    print(FirstList[i])

NamesList = ["Carlos", "Alejandra", "Any"]

for i in range(len(NamesList)):
    print(NamesList[i])

# Is possible to assign a negative integer number to the index of a list.
j = 0
for i in range(len(NamesList)):
    j = i*-1
    print(NamesList[j])

# The lists in Python are possible to use across the init value and end value
# into the range method and extract a sublist, the end value is excluded

print(FirstList[0:3])

# Add to end list.
NamesList.append("Maria")

for i in range(len(NamesList)):
    print(NamesList[i])

# Add and any position
NamesList.insert(2, "Andrea")

for i in range(len(NamesList)):
    print(NamesList[i])

# Add multiple elements
FirstList.extend([70, 80, 90])

for i in range(len(FirstList)):
    print(FirstList[i])

# Find and index number of a element of list.
print(FirstList.index(30))
print(NamesList.index("Alejandra"))

# Validate if a element exists in a list.
print("Maria" in NamesList)
print(100 in FirstList)

mixList = ["Carlos", 10, 50.5, True, "Alejandra", 100]
for i in range(len(mixList)):
    print(mixList[i])

# Remove a element of the list.

mixList.remove("Carlos")
for i in range(len(mixList)):
    print(mixList[i])

# Remove the last element of the list.
mixList.pop()
for i in range(len(mixList)):
    print(mixList[i])

# Merge two lists.
MergeList = NamesList + FirstList
for i in range(len(MergeList)):
    print(MergeList[i])

print(MergeList[:])
# Repeat lists
print(MergeList*3)

# Video 7
