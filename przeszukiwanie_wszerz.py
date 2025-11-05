from collections import deque
from rozwiazywacz_labiryntu import RozwiazywaczLabiryntu


class PrzeszukiwanieWszerz(RozwiazywaczLabiryntu):
    """
    Implementuje strategię przeszukiwania wszerz (Breadth First Search).
    Używa kolejki (FIFO), aby znaleźć najkrótszą ścieżkę.
    """

    def rozwiaz(self):
        kolejka = deque([self.start])
        skad_przyszedl = {}
        odwiedzone = {self.start}

        # NOWA ZMIENNA: Śledzenie maksymalnej zajętości pamięci (kolejki)
        max_rozmiar_kolejki = 1

        while kolejka:
            # print('Bierząca kolejka : ', kolejka)
            # print(kolejka)
            biezacy = kolejka.popleft()
            # print('Zdejmujemy z kolejki : ', biezacy)

            if biezacy == self.meta:
                sciezka = self.odtworz_sciezke(skad_przyszedl, biezacy)
                # ZMODYFIKOWANY RETURN: Zwracamy też max rozmiar
                return sciezka, odwiedzone, max_rozmiar_kolejki

            for sasiad in self.pobierz_sasiadow(biezacy[0], biezacy[1]):
                if sasiad not in odwiedzone:
                    odwiedzone.add(sasiad)
                    skad_przyszedl[sasiad] = biezacy
                    kolejka.append(sasiad)

            # NOWA LOGIKA: Aktualizuj maksymalny rozmiar po dodaniu sąsiadów
            if len(kolejka) > max_rozmiar_kolejki:
                max_rozmiar_kolejki = len(kolejka)

        # ZMODYFIKOWANY RETURN: Zwracamy też max rozmiar w przypadku porażki
        return None, odwiedzone, max_rozmiar_kolejki