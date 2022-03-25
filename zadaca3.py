# 3. Da se napravi programa vo koja korisnikot ke moze da vnese proizvolen broj na elementi vo set, da se ispecati setot i korisnikot da moze da kaze koj element da se izbrise

elementi=set()

ch='d'
while ch=='d' or ch=='D':
    x= int (input ("Vnesete element-broj : "))
    ch=input("Dali sakate da vnesete nov broj (D/N) : ")
    elementi.add(x)
    if ch.lower()!="d":
        print ("Vasiot set e : {}".format(elementi))
        brishi=int(input("Koj element sakate da go izbrisete? "))
        elementi=list(elementi)
        elementi.remove(brishi)
        elementi=set(elementi)
print(elementi)


