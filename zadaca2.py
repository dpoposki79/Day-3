#2. Da se napravi programa vo koja korisnikot ke moze da vnese proizvolen broj na elementi vo set, da se pomine niz elementite so setot i parnite da se dodadat vo drug set, a ne patnite vo drug
elementi=set()
parni=set()
neparni=set()
ch='d'
while ch=='d' or ch=='D':
    broj= int (input("Vnesete broj : "))
    elementi.add(broj)
    ch=input("Dali sakate da vnesete nov broj (D/N) : ")

    if (broj % 2)==0:
        parni.add(broj)
    else:
        neparni.add(broj)
print(parni)
print (neparni)


