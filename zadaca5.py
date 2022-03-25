#5. Da se napravi programa vo koja korisnikot ke moze da vnese proizvloen broj na elementi vo LISTA, da se izbrisaat duplikatite vo listata i da se ispecatat unikatnite vrednosti. *Dopolnitelni korisnikot da moze da izbere dali unikatnite podatoci da se ispecatat kako lista ili set
elementi=[]
ch='d'
while ch=='d' or ch=='D':
    x= input ("Vnesete element : ")
    ch=input("Dali sakate da vnesete nov broj (D/N) : ")
    elementi.append(x)
    if ch.lower()!="d":
        elementi=set(elementi)
        print(elementi)
        odgovor=input("Dali sakate da se ispecatat kako lista ili kako set? ")
        if odgovor.lower()==("lista"):
            elementi=list(elementi)
            print(elementi)
        if odgovor.lower()==("set"):
            elementi=set(elementi)
            print (elementi)