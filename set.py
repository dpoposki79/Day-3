from turtle import clear


#SET se koristi za cistenje na duplikati vo setot

x = [1,2,3]  #list
z = (1,2,3) #tuple
y = {1,2,3} #set nema index i ne se znae koj element na koe mesto e

print(x[1]) #pecatenje na element od lista
print(y)

for i in y:
    print(i)

y.add("jaboilki") #dodavanje element vo set
y.remove(3) #brisenj na element no ako ne postoi ke javi greska
y.discard(2) #brisenje na element bez greska i dokolku ne postoi
y.pop() #ke se izbrise element ama nema da znaeme koj element ke bide toa bidejki nema indeksi vo set
y.clear() #gi brise site elementi vo setot
del y #go brise cel set
print(y)