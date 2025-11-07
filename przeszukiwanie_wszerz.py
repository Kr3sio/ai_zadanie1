import os
from collections import deque
from rozwiazywacz_labiryntu import RozwiazywaczLabiryntu


class PrzeszukiwanieWszerz(RozwiazywaczLabiryntu):
    # Używa kolejki (FIFO), aby znaleźć rozwiązanie.

    def rozwiaz(self):
        kolejka = deque([self.start])
        skad_przyszedl = {}
        odwiedzone = {self.start}

        max_rozmiar_kolejki = 1
        if os.path.exists('wszerz'):
            os.remove('wszerz')
        while kolejka:
            zawartosc = ''
            zawartosc += f'Bierząca kolejka : { kolejka} '+ "\n"

            # print('Bierząca kolejka : ', kolejka)
            # print(kolejka)
            biezacy = kolejka.popleft()
            zawartosc += f'Zdejmujemy z kolejki :  {biezacy}' +"\n"
            # print('Zdejmujemy z kolejki : ', biezacy)
            if self.wiersze < 100 or self.kolumny < 100:
                with open('wszerz' ,'a', encoding='utf-8') as w:
                    w.write(zawartosc)

            if biezacy == self.meta:
                sciezka = self.odtworz_sciezke(skad_przyszedl, biezacy)
                return sciezka, odwiedzone, max_rozmiar_kolejki

            for sasiad in self.pobierz_sasiadow(biezacy[0], biezacy[1]):
                if sasiad not in odwiedzone:
                    odwiedzone.add(sasiad)
                    skad_przyszedl[sasiad] = biezacy
                    kolejka.append(sasiad)

            if len(kolejka) > max_rozmiar_kolejki:
                max_rozmiar_kolejki = len(kolejka)

        return None, odwiedzone, max_rozmiar_kolejki