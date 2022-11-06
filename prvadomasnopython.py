#prva zadaca
"""
x=int(input("Vnesi go prviot broj: "))
y=int(input("Vnesi go vtoriot broj: "))
if x+y<100:
    print("Zbirot {} na broevite {} i {} e pomal od 100".format(x+y,x,y))
elif x+y==100:
    print("Zbirot {} na broevite {} i {} e ednakov na 100".format(x+y,x,y))
else:
    print("Zbirot {} na broevite {} i {} e pogolem od 100".format(x+y,x,y))
"""
#vtora zadaca
"""
ime=input("Vnesi go tvoeto ime: ")
x=int(input("Vnesi ja tvojata godina na raganje: "))
godini=2022-x
if godini>=18:
    print("{} e polnoleten/na".format(ime))
else:
    print("{} e maloleten/na".format(ime))
"""
#treta zadaca. Mozev da ja resam so vnesuvanje na stranite na dvata pravoagolnici i samo so IF da gi sporedam plostinite. Jas ja resiv so FOR.
"""
P=0
for i in range(2):
    P1=P
    a=int(input("Vnesete ja dolzinata na pravoagolnikot "))
    b=int(input("Vnesete ja sirinata na pravoagolnikot "))
    P=a*b
    print(P)
if P1>P:
    print("Prviot pravoagolnik ima pogolema plostina")
else:
    print("Vtoriot pravoagolnik ima pogolema plostina")
"""
#cetvrta zadaca
"""
a=int(input("Vnesete go agolot 1: "))
b=int(input("Vnesete go agolot 2: "))
c=int(input("Vnesete go agolot 3: "))
zbir=a+b+c
if zbir==180:
    print("So aglite {}, {} i {} moze da se kreira triagolnik".format(a,b,c))
else:
    print("So aglite {}, {} i {} ne moze da se kreira triagolnik".format(a,b,c))
"""
#petta zadaca

from itertools import count


ime=input("Vnesete ime: ")
c=0
x=0
z=0
k=0
t=0
y=len(ime)
b=ime.lower()
print("{} e sostaveno od {} karakteri ".format(ime,y))
if "a" in b:
    c=b.count("a")
    print("a ja ima {} pati vo {}".format(c,ime))
else:
    print("a ja nema")

if "e" in b:
    x=b.count("e")
    print("e ja ima {} pati vo {}".format(x,ime))
else:
    print("e ja nema")

if "i" in b:
    z=b.count("i")
    print("i ja ima {} pati vo {}".format(z,ime))
else:
    print("i ja nema")

if "o" in b:
    k=b.count("o")
    print("o ja ima {} pati vo {}".format(k,ime))
else:
    print("o ja nema")

if "u" in b:
    t=b.count("u")
    print("u ja ima {} pati vo {}".format(t,ime))
else:
    print("u ja nema")



