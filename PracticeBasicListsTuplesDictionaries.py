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
# The Tuples
# Characteristics:
# The tuples are not allowed to modify, It does not allow to append, extend, and not remove
# Not Allow Find, A Tuple is not indexed.
# A tuple allows extracting a portion, but this portion is a new tuple.
# A tuple allows verification if an element exists in the tuple
# The tuples are more speedy and require minus space in memory.
# A tuple allows string formatting.
# A tuple can be used as a password in a Dictionary, (The lists do not allow this).
# Syntax:

firstTuple = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
mixTuple = ("Luis", 25, "Carlos", 45, "Jorge", 25)

print(firstTuple[3])
print(mixTuple[0:2])

ConvertTupleToList = list(mixTuple)

print(ConvertTupleToList[0:2])

ConvertListToTuple = tuple(ConvertTupleToList)

print(ConvertListToTuple[0:2])

print("Carlos" in ConvertListToTuple)
print("Pedro" in ConvertListToTuple)
print(ConvertListToTuple.count(45))
print(ConvertListToTuple.count(25))
print(len(ConvertListToTuple))
# Is possible create a tuple with one element.

UnitTuple = ("Unique Element",)

print(len(UnitTuple))

UnpackTuple = (2022, 11, 9)
year, month, day = UnpackTuple
print(year, month, day)

# Finish Video 8

# The Dictionaries
# It is a Data Structure that allows saving values of  different types including Lists, Tuples, and Other Dictionaries
# The values are structured with a Key and a Value
# The elements of a dictionary are not ordered.

FirstDictionary = {"Alemania": "Berlin", "Francia": "Paris", "Guatemala": "Guatemala", "España": "Madrid"}
print(FirstDictionary)

# Add Elements to a Dictionary
FirstDictionary["Italia"] = "Lisboa"  # The error is controlled, and it is by the way for another operation next.
print(FirstDictionary)

# Edit Elements to a Dictionary
FirstDictionary["Italia"] = "Roma"
print(FirstDictionary)

# Remove a Element
del FirstDictionary["España"]
print(FirstDictionary)

# Allow different types of keys and values.
mixDictionary = {"Pais": "Guatemala", "Edad": 45, 1: "Order"}
print(mixDictionary)

# Dictionary with Tuple
dictionaryTuple = {"Nombre": "Carlos", "Modelos": [2009, 2005, 2011, 2022]}
print(dictionaryTuple)
print(dictionaryTuple["Modelos"])
print(dictionaryTuple["Modelos"][1])

dictionaryDictionary = {"Nombre": "Carlos", "Modelos": {"Años": [2009, 2005, 2011, 2022]}}
print(dictionaryDictionary)
print(dictionaryDictionary["Modelos"]["Años"])
print(dictionaryDictionary["Modelos"]["Años"][2])

# Others Methods
print(dictionaryDictionary.keys())
print(dictionaryDictionary["Modelos"].keys())

print(dictionaryDictionary.values())
print(dictionaryDictionary["Modelos"].values())
print(len(dictionaryDictionary))

# Finish Video 9

