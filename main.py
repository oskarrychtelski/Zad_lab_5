# zad.1
# class material:
#     def __init__(self,rodzaj,dlugosc,szerokosc):
#         self.rodzaj=rodzaj
#         self.dlugosc=dlugosc
#         self.szerokosc=szerokosc
#     def wyswietl_nazwe(self):
#         return "Nazwa materialu: {}".format(self.rodzaj)
#
#
# class ubrania(material):
#     def __init__(self,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc):
#         material.__init__(self,rodzaj,dlugosc,szerokosc)
#         self.rozmiar=rozmiar
#         self.kolor=kolor
#         self.dla_kogo=dla_kogo
#     def wyswietl_dane(self):
#         return "Dane ubrania: {}, {}, {}, {}, {}, {}".format(self.rozmiar,self.kolor,self.dla_kogo,self.rodzaj,self.dlugosc,self.szerokosc)
#
#
# class sweter(ubrania):
#     def __init__(self,rodzaj_swetra,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc):
#         ubrania.__init__(self,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc)
#         self.rodzaj_swetra=rodzaj_swetra
#     def wyswietl_dane(self):
#         return "Dane sweterka: {}, {}, {}, {}, {}, {}, {}".format(self.rodzaj_swetra,self.rozmiar,self.kolor,self.dla_kogo,self.rodzaj,self.dlugosc,self.szerokosc)
#
#     bela=material("kaszmir",20,5)
#     szalik=ubrania("xl","czarny","mezczyzni","poliester","45","15")
#     sweterek=sweter("kardigan","xs","zielony","kobiety","jedwab","50","50")
#     print(bela.wyswietl_nazwe())
#     print(szalik.wyswietl_dane())
#     print(sweterek.wyswietl_dane())



#zad.2 chyba nie rozumiem pytania
# class Kwadrat:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,z):
#         return self.x+z.x
#     def policz(self):
#         return self.x*4+self.x
#     def instancja(self):
#         return Kwadrat(self.policz())
#
# kwadrat=Kwadrat(5)
# print(kwadrat.instancja())



#zad.3
# class Kwadrat:
#     def __init__(self,x):
#         self.x=x
#     def __gt__(self,z):
#         if self.x>z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
#     def __ge__(self,z):
#         if self.x>=z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
#     def __lt__(self,z):
#         if self.x<z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
#     def __le__(self,z):
#         if self.x<=z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
# print(Kwadrat(5)>Kwadrat(6))


#zad.4
# class point:
#     def __init__(self,x):
#         self.x=x
#     def __gt__(self,z):
#         if self.x>z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
#     def __ge__(self,z):
#         if self.x>=z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
#     def __lt__(self,z):
#         if self.x<z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
#     def __le__(self,z):
#         if self.x<=z.x:
#             return "prawda"
#         else:
#             return "nieprawda"
# y=point(5)
# z=point(9)
# a=point(1)
# counter=6
# print(counter<y, counter>z, counter>=a)
# counter=10


#zad.5
# class osoba:
#     def __init__(self,imie,nazwisko):
#         self.imie=imie
#         self.nazwisko=nazwisko
# class pracownik(osoba):
#     def __init__(self,imie,nazwisko,pensja):
#         osoba.__init__(self,imie,nazwisko,)
#         self.pensja=pensja
# class manager(pracownik):
#     def __init__(self,imie,nazwisko,pensja):
#         pracownik.__init__(self,imie,nazwisko,pensja)
# osoba1=osoba("adam","kuciapka")
# osoba2=pracownik("marek","nowacki",3000)
# osoba3=manager("zdzichu","babol",12000)
# print(isinstance(osoba1,manager))
# print(isinstance(osoba2,pracownik))
# print(isinstance(osoba3,manager))
# print(issubclass(osoba,pracownik))
# print(issubclass(manager,manager))
# print(issubclass(manager,osoba))


#zad.6 w powyższym zadaniu nie użyłem iteratora



#zad.7
# class parzyste:
#     def __init__(self,data):
#         self.data=data
#         self.index=-1
#     def __iter__(self):
#         if self.index % 2 == 0:
#             return self
#     def __next__(self):
#         self.index = self.index + 1
#         if self.index%2==0:
#             return self.data[self.index]
#         if self.data[self.index]=='\0':
#             raise StopIteration
#
# test=parzyste("ziemniak")
# print(test)
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))


#zad.8
# class samogloski:
#     def __init__(self,data):
#         self.data=data
#         self.index=-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index=self.index+1
#         if self.data[self.index].lower() in 'aeiou':
#             return self.data[self.index]
#         if self.data[self.index]=='\0':
#             raise StopIteration
#     def spr(self):
#         if isinstance(self.data,samogloski)==1:
#             return "dobrze"
#
#
# test=samogloski("ziemniak")
# print(test)
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(test.spr())

#zad.9
# def parzyste(data):
#     for index in range(len(data)):
#         if index%2==0:
#             yield data[index]
# test=parzyste("fifarafa")
# print(test)
# print(next(test))
# print(next(test))
# print(next(test))



#zad.10
# def ciag(a0,n,len):
#     for i in range(len):
#         yield a0+i*n
# test=ciag(0,2,4)
# print(test)
# print(next(test))
# print(next(test))
# print(next(test))