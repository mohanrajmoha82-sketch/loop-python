#jumping or teansfer statement
"""
1. continue
2. break
3. pass
"""
#1.continue
for i in range(6):
    if i==4:
        continue
    else:
        print(i)

#2.brack
for i in range(6):
    if i==4:
        break
    else:
        print(i)

#3.pass
for i in range(11):
    pass
print("hi")

for i in range(11):
    if True:
        pass

#1.plaindrome using integer
a=int(input("Enter the value :"))
b=0
t=a
while t>0:
    d=t%10
    b=b*10+d
    t=t//10
if b==a:
    print(b," is plaindrome")
else:
    print(b,"is not a plaindrome")
"""
#1
while 121>0:
    d=121%10 => 12.1 => d=1
    b=0*10+1 => 0+1 => b=1
    t=121//10 => 12.1 => t=12
#2
while 12>0:
    d=12%10 => 1.2 => d=2
    b=1*10+2 => 10+2 => b=12
    t=12//10 => 1.2 => t=1
#3
while 1>0:
    d=1%10 => 0.1 => d=1
    b=12*10+1 => b=121
    t=1//10 => 0.1 => t=0
#4
while 0>0 # flase
"""

#Armstrong number
a= int(input("Enter value :"))
b=0
t=a
while t>0:
    d=t%10
    b+=d**3
    t=t//10
if b==a:
    print(b,"is Amstrong number")
else:
    print(b,"is not a armtrong number")
"""
#1
while 153>0:
    d=153%10 => 15.3 => d=3
    b+=3**3 => b=27
    t=153//10 => 15.3 => t=15
#2
while 15>0:
    d=15%10 => 1.5 => d=5
    b+=5**3 => b=125
    t=15/10 => 1.5 => t=1
#3
while 1>0:
    d=1%10 => 0.1 d=1
    b=1**3 =>b=1
    t=1//10 => 0.1 => d=0
#4
while 0>0: # flase
"""















