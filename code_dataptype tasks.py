#tasks
#1).sum all the iteme in a list
a=[10,20,30,40,50,60]
sum =0
for i in a:
    sum+=i
print(sum)

#2)largerst number from a list
a=[10,20,30,40,50,60]
m=0
for i in a:
    if i>m:
        m=i
print(m)


#3) smalllest number
a=[10,20,30,40,50,60]
m=a[0]
for i in a:
    if i<m:
        m=i
print(m)

#4) remove the duplicates form a list
a=[10,20,30,"mohan",40,50,50,60,"mohan"]
d=[]
for i in a:
    if i not in d:
        d.append(i)
print(d)

#5)copy a list
a=[10,20,30,40,50,60]
b=a.copy()
print("b :",b)

#6) reveres a list in python
a=[10,20,30,"mohan",40,"raj",50,60]
a.reverse()
print(a)

#7) create a list with random data type
a=[10,20.01,"hello",30,["wold"],40,50,60,True,False]
print(a)


#8) remove an empty element from a list
#m1
a=[10,20,30,"",40,50,60]
a.pop(3)
print(a)

#m2.
a=[10,20,30,"",40,50,60]
r=[]
for i in a:
    if i=="":
        r.append(i)
        a.remove(i)
print(a)

#m3
a=[10,20,30,40,"",50,60]
b=[]
for i in a:
    if i:
        b.append(i)
print(b)
#4
a=[10,20,30,40,"",50,60]
a.remove("")
print(a)

#9) append data of the secoun list to the first list
a=[10,20,30,40,50,60]
l=["hello","world"]
a.append(l)
print(a)

#10)choose random item in a list
a=[10,20,30,40,50,["mohan","raj"],60]
print(a[3])
print(a[-2])

#11) odd and even
a=[1,2,3,4,5,6,7,8,9,0]
odd=[]
even=[]
for i in a:
    if i%2==0:
        odd.append(i)
    else:
        even.append(i)
print(odd,even)


#12) sorting number in ascending order
a=[20,70,90,40,100,60]
a.sort()
print(a)
    

