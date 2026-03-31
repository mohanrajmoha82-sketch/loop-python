#patterns
#1.square pattern
'''
n=5
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()    

n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()    

n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()  

#haif pyramid or inc pattern(i+1)
n=6
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    print()

n=6
for i in range(n):
    for j in range(i+1):
        print(i,end=" ")
    print()

n=6
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#invertep haif pyramid or dec pattern(i,n)
n=5
for i in range(n):
    for j in range(i,n):
        print(j,end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print(i,end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

#full pyramid
"""
outer loop-->i
inner loop
1.dec pattern
2.inc pattern
3.inc pattern
"""
n=5
#dec
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
        #1.inc
    for i in range(i+1):
        print(i,end=" ")
        #2.inc
    for j in range(i):
        print(j,end=" ")
    print()

n=5
#dec
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    #1.inc
    for i in range(i+1):
        print("*",end=" ")
    #2.inc
    for j in range(i):
        print("*",end=" ")
    print()
'''
#invertep full pyramid


"""
1.inc pattern
2.inc pattern
3.dec pattern
"""
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(i,end=" ")
    for j in range(i,n):
        print(j,end=" ")
        
    print()
'''     
    for j in range(1,n):
        print(i,end=" ")
    print()    
 '''   
    
    



