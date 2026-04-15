"""
list => to access multipic datatype and multiple value in a single variable. mulable datatype
1.denoted by => squere bracked []
2.Element => ordered element
3.duplicate => it allows duplicats because it is access by using element its index postion left to ringt ->form 0(Zero)
Right to left -> starts from 1(minus 1)
"""
#cord data type
a=10
print(a)
print("mohan")
print(a)

#list
a=[10,"mohan","mohan",20,False,44.22]
#indexing
print(a[3])
print(a[-1])
#silicing
print(a[2:6])
#revers
print(a[::-1])
a=[10,"mohan","mohan",20,["hello",True],False,44.22]
print(a[4][1])

#build in function in list
"""
syntex of build function
variable.build_in_functions
"""

#1) .index()
a=[10,"mohan","mohan",20,["hello",True],False,44.22]
print(a.index(False))

#2) .count()
a=[10,"mohan","mohan",20,["hello",True],False,44.22]
print(a.count("mohan"))

#add

#3) .append
a=[1,2,3,4,["mohan","raj"],8,False,True,23.4]
a.append("Djano")
print(a)

#4) .insert
a=[1,2,3,4,["mohan","raj"],8,False,True,23.4]
a.insert(3,"hello")
print(a)

#5) .extend
a=[1,2,3,4,"hello"]
b=[5,6,7,"world"]
a.extend(b)
print(a)

#remove

#6) .remove
a=[10, 20,30, 40, 70, 80, 90, "world"]
a.remove(30)
print(a)

#7) .pop()

a=[10, 20, 40, 70, 80, 90, 22,"bye"]
a.pop(-1)
print(a)
a.pop(4)
print(a)
a.pop()
print(a)

#8) .clear()
a=[10, 20, 40, 70, 80, 90, 22]
a.clear()
print(a)


#9) .copy
a=[10, 20, 40, 70, 80, 90, 22]
b=a.copy()
print(b)

#10) .reverse
a=[1,2,3,4,"hello","world",5,6,7,8]
a.reverse()
print(a)

#11) .sort()
s=[7,8,4,5,6,0,3,2,1,9]
s.sort()
print(s)
s.sort(reverse=True)
print(s)
      
