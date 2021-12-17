from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def kaynnista():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        abc = {
            'a': KPSPelaajaVsPelaaja(),
            'b': KPSTekoaly(),
            'c': KPSParempiTekoaly()
        }
        if vastaus in 'abc':
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            pelimuoto = abc[vastaus]
            pelimuoto.pelaa()
        else:
            break
