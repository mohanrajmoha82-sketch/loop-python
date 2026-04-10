#string
"""
1.string is immutalde data type
2.string is squence of character
3." " or ''
"""

#Q1. palindrome
a=input("Enter :")
if a[::-1]==a:
    print(True)
else:
    print(False)
    

#Q2.vowel count
#m1
a=input("Enter the value :")
vowel="aeiouAEIOU"
b=0
for i in a:
    if i in vowel:
        b+=1
print(b)

#m2
a=input("Enter the value :")
b=0
for i in a:
    if i in "aeiouAEIOU":
        b+=1
print(b)

#Q3.reverse a string without using built-in function
a=input("Enter the atoz : ")
print(a[::-1])

#Q4.count how uppercase and lowercase letters are in a string
"""
.islower = all letter is lower[abcd to z] letter
.isupper =  all letter is upper[ABCD to Z] letter
"""
a= "MOHSbff"
b=0
c=0
for i in a:
    if i.isupper():
        b+=1
    elif i.islower():
        c+=1
print(b)
print(c)

#Q5.remove all duplicate character form a string
a="programming"
c=""
for i in a:
    if i not in c:
        c+=i
print(c)

#Q6.Anagram
"""
sorted = iterable line [124536] = [123456]
"""
a="lister"
b="silent"
if (sorted(a))==(sorted(b)):
    print("yas")
else:
    print("no")

#Q7. remove all non-aiphabetic
"""
alpha is only alphabets[a ton z] characters
"""
a="Hello! @world  $python$"
b=""
for i in a:
    if i.isalpha():
        b+=i
print(b)

#Q8. count the number of words in a string
"""
.split = this one line is who many words or count tha words 
"""
a=input("Enter the string :")
b=len(a.split())
print(b)

#Q9. digits in a string
a="abc123"
print(len(a))

#Q10. replace all spaces with hyphens
a="Hello world"
print(a)
b=a.replace (" ","-")
print("replace :",b)

#Q11.capitalize
"""
title = every word is first letter is capital letter
"""
a="walcome to python"
print(a.title ())

#Q12. print only digits
"""
.isdigit =  this is only string number 
"""
a=input("Enter the string :")#mohanraj1234
for i in a:
    if i.isdigit():
        print(i, end=" ")#1 2 3 4

#Q13. extract every second  character from a string
"""
reverse  string =variable[::2]
"""
a=input("Enter the name :")
print(a[::2])

#Q14.startwith() and endwith()
"""
.startswith() = >>>start letter same letter is true
                >>>start letter not same letter is false
.endwith() = >>>end letter same letter is true
             >>>end letter not same letter is false
"""
a="Hello World"

if a.startswith (input("Enter the start letter :")):
    print("True")
elif a.endswith (input("Enter the end letter :")):
    print("True")
else:
    print("False")
print()
    


