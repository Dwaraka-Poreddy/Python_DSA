plan = [5, "Wake Up & Siri Class", 6, "Gym", 8, "Python DSA", 10, "Go to Office",]
print(plan[0])
print(plan[1])
print(plan[2])

for i in range(9):
    print(plan[i])

print(range(9))
print(list(range(9))) #Single variable : ending - 1
#[0, 1, 2, 3, 4, 5, 6, 7, 8]

print(list(range(2,9))) #2 variable : first starting, ending - 1
#[2, 3, 4, 5, 6, 7, 8]

print(list(range(2,9,2))) #3 variable : first starting, ending - 1, step
#[2, 4, 6, 8]

li = [1, 2, 3]
for i in li:
    print(i)
    print("hello")
# 1
# hello
# 2
# hello
# 3
# hello


# Count the number of 1's in the list
arr = [1, 5, 6, 8, 1, 2, 3, 4, 1, 6]
countOfOnes = 0
for i in arr:
    if i == 1:
        countOfOnes += 1
print(countOfOnes) 
# 3

names = ["Dwaraka", "Siri", "Srinivas", "Simone"]

for name in names:
    print(name)

for i in range(4):
    print(names[i])

for i in range(len(names)): #len() is a built-in function
    print(names[i])

for i in range(names.__len__()): #__len__() is a built-in function
    print(names[i])

# Dwaraka
# Siri
# Srinivas
# Simone