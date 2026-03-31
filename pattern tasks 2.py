#pattern tasks
#Q1
# 1.haif pyramid

n=6
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#2.inverted half pyramid
n=6
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

#3.hollow inverted haif pyramid
n=6

for i in range(n,0,-1):
    for j in range(i):
        if i==n or j==0 or j==i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#4.full pyramid
n=6
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

#5.inverted full pyramid
n=6
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

#Q2
#1.haif pyramid
n=6
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    print()

#2.inverted pyramid
n=6
for i in range(0,n):
    for j in range(i,n):
        print(j,end=" ")
    print()

#3.hollow inverted haif pyramid
n=6
for i in range(n,0,-1):
    for j in range(i):
        if i==n or j==0 or j==i-1:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

#4. full pyramid
n=6
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(j,end=" ")
    for j in range(i):
        print(j,end=" ")
    print()

#5.hollow  haif pyramid
n=6
for i in range(n+1):
    for j in range(i,i+1):
        if j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
