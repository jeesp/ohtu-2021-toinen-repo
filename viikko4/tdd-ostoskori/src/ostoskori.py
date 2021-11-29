from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for element in self.kori:
            maara += element.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for element in self.kori:
            summa += element.hinta
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        eilistassa = True
        for element in self.kori:
            if element.tuote._nimi == lisattava._nimi:
                eilistassa = False
                element.muuta_lukumaaraa(1)
        if eilistassa:
            self.kori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for element in self.kori:
            if element.tuote._nimi == poistettava._nimi:
                element.muuta_lukumaaraa(-1)
                if element.lukumaara() == 0:
                    self.kori.remove(element)
                break

    def tyhjenna(self):
        self.kori.clear()
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
