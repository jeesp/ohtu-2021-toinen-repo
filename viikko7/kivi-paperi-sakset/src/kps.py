class KPS:
    def pelaa(self):
        pass

    def ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def toisen_siirto(self, tekoaly=None):
        return 'k'

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
