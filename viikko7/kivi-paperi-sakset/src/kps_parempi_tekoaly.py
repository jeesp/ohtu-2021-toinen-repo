from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps import KPS


class KPSParempiTekoaly(KPS):
    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = TekoalyParannettu(10)

        ekan_siirto = super().ensimmaisen_siirto()
        tokan_siirto = tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = super().ensimmaisen_siirto()
            tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")
            tekoaly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)
