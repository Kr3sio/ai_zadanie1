import os

from rozwiazywacz_labiryntu import RozwiazywaczLabiryntu


class PrzeszukiwanieWglab(RozwiazywaczLabiryntu):
    """
    Implementuje strategię przeszukiwania w głąb (Depth First Search).
    Używa stosu (LIFO). Znajduje *jakąkolwiek* ścieżkę.
    """

    def rozwiaz(self):
        stos = [self.start]
        skad_przyszedl = {}
        odwiedzone = {self.start}

        max_rozmiar_stosu = 1
        if os.path.exists('wglab'):
            os.remove('wglab')
        while stos:
            zawartosc = ''
            zawartosc += f'Bierzący stos : {stos} '+ "\n"


            biezacy = stos.pop()
            zawartosc += f'Zdejmujemy ze stosu :  {biezacy}' +"\n"


            with open('wglab' ,'a', encoding='utf-8') as a:
                a.write(zawartosc)

            # print('Bierzący stos : ', stos)
            # print(stos)

            # print('Zdejmujemy ze stosu : ', biezacy)

            if biezacy == self.meta:
                sciezka = self.odtworz_sciezke(skad_przyszedl, biezacy)
                return sciezka, odwiedzone, max_rozmiar_stosu

            for sasiad in self.pobierz_sasiadow(biezacy[0], biezacy[1]):
                if sasiad not in odwiedzone:
                    odwiedzone.add(sasiad)
                    skad_przyszedl[sasiad] = biezacy
                    stos.append(sasiad)


            if len(stos) > max_rozmiar_stosu:
                max_rozmiar_stosu = len(stos)

        return None, odwiedzone, max_rozmiar_stos