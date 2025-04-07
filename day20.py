name = input()
place = input()
age = input()
intAge = int(input())
print("I'm", name)
print("I'm from", place)
print("I'm", age, "years old")
print(type(name))
print(type(age))
print(type(intAge))


favNames = []
n = 3
for i in range(n):
    temp = input()
    favNames.append(temp)
print(favNames)


li=[]
# s = "1 4 1"
s = input()
temp = s.split()
print(temp)
for i in range(len(temp)):
    li.append(int(temp[i]))
print(li)

lis = list(map(int, input().split()))
print(lis)
