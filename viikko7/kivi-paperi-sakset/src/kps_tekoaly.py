from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS


class KPSTekoaly(KPS):
    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = Tekoaly()

        ekan_siirto = super().ensimmaisen_siirto()
        tokan_siirto = self.toisen_siirto(tekoaly)

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = super().ensimmaisen_siirto()
            tokan_siirto = self.toisen_siirto(tekoaly)

            print(f"Tietokone valitsi: {tokan_siirto}")

        print("Kiitos!")
        print(tuomari)

    def toisen_siirto(self, tekoaly):
        return tekoaly.anna_siirto()
