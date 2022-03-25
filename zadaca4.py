#4. Da se napravi programa vo koja korisnikot ke moze da vnese proizvolen broj na elementi vo set, da se ispecati setot, korisnikot da moze da izbere dali da se izbrise samo eden element - ako da da kaze koj element da se izbrise, ili da se izbrisat site elementi od setot i da mu se ispecati kolku elementi se bile izbrisani.
elementi=set()
ch='d'
while ch=='d' or ch=='D':
    x=  input ("Vnesete element : ")
    ch=input("Dali sakate da vnesete nov broj (D/N) : ")
    elementi.add(x)
    if ch.lower()!="d":
        print (elementi)
        odgovor=input("Sto sakate da izbrisete, cel set ili samo element")
        if odgovor.lower()==("cel"):
            elementi=list(elementi)
            elementi.clear
            elementi=set(elementi)
            print(elementi)
            print("Setot e prazen")
        if odgovor.lower()==("element"):
            element=input("Koj element sakate da go izbrisete? ")
            elementi=list(elementi)
            elementi.remove(element)
            elementi=set(elementi)
            print ("Elementot koj e izbrisan e  {}".format(element))
            print (elementi)

