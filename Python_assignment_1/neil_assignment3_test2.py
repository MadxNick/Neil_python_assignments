#write a program to find maximum and minimum number among three numbers.
a = float(input("enter a 1st number :"))
b = float(input("enter a 2st number :"))
c = float(input("enter a 3st number :"))
if a<b>c :
 print(b,"is the maximum")
if b<a>c :
 print(a,"is the maximum")
if a<c>b :
 print(c,"is the maximum")
if a==b==c :
 print("all are equal")
if a<b<c :
 print(a,"is the minimum")
if b<a<c :
 print(b,"is the minimum")
if c<b<a :
 print(c,"is the minimum")
if c<b==a :
 print(c,"is the minimum")
 print(a,b,"are equal")
if b<c==a :
 print(b,"is the minimum")
 print(a,c,"are equal")
if a<b==c :
 print(a,"is the minimum")
 print(c,b,"are equal")
if c>b==a :
 print(a,b,"are equal")
if b>c==a :
 print(a,c,"are equal")
if a>b==c :
 print(c,b,"are equal")