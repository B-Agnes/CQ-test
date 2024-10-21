#slicing -returns part of a list.
nmbr1 = 4
nmbr2 = 24
nmbr3 = 50
nmbr4 = 80
print(nmbr1)
print(nmbr2)
print(nmbr3)
print(nmbr4)

list1 = list(range(4,24))
print(list1)

list2 = list(range(50,80))
print(list2)

print(list1[0:3])
print(list2[0:4])
print(list1[4:9])
print(list1[4:9])
print(list2[5:10])
print(list1[10:30])
print(list2[20:100])
print(list1[-10:-2])
print(list2[-25:-5])
print(list1[5:-2])
print(list2[-25:5])

print(list1[3:])
print(list2[:5])

"""
Exercise 15
"""
numbers = list(range(5,30))
print(numbers)
print(numbers[0:5])
print(numbers[:8])
print(numbers[6:])
print(numbers[10:])

items_list = list["sugar","salt","butter","soap","milk"]
print(items_list)


#adding elements to a list using append and extend
listA = ["Mama", "D.A.D", "Baby", "Brother", "Sister"]
listB = [3, 4 ,5, 5, 6, 9, 25]
listC = list(range(5,50,4))
listD = [3.6, 7.42, 8.34, 23.6, 12.4]

print(listA)
print(listB)
print(listC)
print(listD)

listA.append("Hallo")
print(listA)
listB.append("25000")
print(listB)
listC.append(450)
print(listC.append(450))
test = listC.append(450)
print(listC)
listD.append(8.00006)
print(listD)

listA.extend(listC)
print(listA)
listB.extend(listD)
print(listB)
listA.extend((1000, 2000, 3000, "Girl", "Boy"))
print(listA)
listD.extend("Girl")
print(listD)
listD.extend(("Boy"))
print(listD)

#remove elements from a list using .remove method
list_bath = ["Soap", "Tissue", "Spay", "Comb", "Brush"]
list_fruits = ["Apples","Mangoes", "Bananas", 45, 8000.32, True]
list_numbers = [34, 1000, 56, 2, 53, 78, 1000, 35]

print(list_bath)
print(list_fruits)
print(list_numbers)
print()

list_bath.remove("Comb")
print(list_bath)
list_fruits.remove(8000.32)
print(list_fruits)
list_fruits.remove(45)
print(list_fruits)
list_fruits.remove(True)
print(list_fruits)
list_numbers.remove(1000)
print(list_numbers)
print()

list_numbers.remove(1000)
print(list_numbers)
print()

print(list_bath)
print(list_fruits)
print(list_numbers)
print()

#exercise 18 -inserting elements in a list. to add an element at an index of your choice.
listH = [3, 4, 5, 6, 7, 8, 8, 10]
listI = [0.1, 0.4, 0.67, 1, 5, 0.8, 50]
listJ = [100, 300, 450, 690, 200, 500000, 279, 1000000]

print(listH)
print(listI)
print(listJ)
print()

listH.insert(1,55)
print(listH)
listI.insert(2, 0.99)
print(listI)
listJ.insert(5, "Size")
print(listJ)
listH.insert(-1, 900)
print(listH)
listH.insert(-5, 80000)
print(listH)
print()

insertA = 5500
insertB = "Crazy Mama"
listH.insert(7, insertA)
listI.insert(0,insertB)
print(listH)
print(listI)

#reverse() to reverse order of list eg listC=[5,8,1] to reverse listC.reverse() gives [1,8,5]

# sort()_ in ascending order eg listC.sort() gives [1,5,8] then listC.sort(reverse=True)  gives [8,5,1}

#clear() eg listC.clear gives []

# index()- gives fisrt appearnace of an element eg listC.index(5) gives 1 while listC(8) gives 2

#count()- tells how often the argument appears eg listD= [5,6,5,7] then listD.count(5) gives 2
 #copy()-to create a copy eg list_copy = list.copy(listD)- not sure


#use dir to check what methods are available for use- the ones without underscore
print(dir(listI))
print()

#exercise 19- generating dictinaries and inserting/delting key/value pair


seqDNA = {"PatientA": 12345, "PatientB": 6789, "PatientC": 101112,
          "PatientD": 131415}
print(seqDNA)
print()

dictA = {}
dictA["Agnes"] = 35
dictA["Danny"] = 34
# or 2nd method
dictB = { "Agnes":"35", "Danny":"34"}
print(dictB["Danny"])
dictA.keys()
dictA.values()
#dictA.keys() gives dictA.keys(["Agnes", "Danny"]) to get specific keys
#dictA.values() gives dictA.values([35,34]} to get the values

del(seqDNA["PatientB"])
print(seqDNA)
print()


#Tuples, excercise 20
# tupleB = ("Apples" ,) to get a single element. Dont forget the comma
tupleA = ("sugar","salt","butter","soap","milk")
tupleB = ("Apples","Mangoes", "Bananas", True)
tupleC = tuple(range(10))
tupleD = tuple(listI)
tupleF = (2, 4, 5, 6, 4, 4, 7, 8.5, 9)

print(tupleA)
print(tupleB)
print(tupleC)
print(tupleD)
print(tupleF)
print()

print(tupleA[2])
print(tupleB[3])
print(tupleC[4:6])
print(tupleC[2:9])
print(tupleD[-1])
print(tupleD[-5])
print(tupleF.count(4))
tupleA = ("salt" ,)
print()

print(type(tupleA))
print(type(tupleB))
print(type(tupleC))
print(type(tupleD))
print(type(tupleF))