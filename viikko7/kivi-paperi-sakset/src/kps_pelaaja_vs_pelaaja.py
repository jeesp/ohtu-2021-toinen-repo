from tuomari import Tuomari
from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = super().ensimmaisen_siirto()
        tokan_siirto = self.toisen_siirto()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = super().ensimmaisen_siirto()
            tokan_siirto = self.toisen_siirto()

        print("Kiitos!")
        print(tuomari)

    def toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")
