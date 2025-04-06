a = []
b = []

while True:
    num = int(input("enter num:"))
    if num == 0:
        break
    a.append(num)
    b.append(num*2)

print("Added Random Num & Double")
print("array A", a)
print("array B", b)

print("Sorted A&B")
a.sort()
print("array A:",a)
b.sort()
print("array B:",b)
