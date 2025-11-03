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

        # NOWA ZMIENNA: Śledzenie maksymalnej zajętości pamięci (stosu)
        max_rozmiar_stosu = 1

        while stos:
            print('Bierzący stos : ', stos)
            # print(stos)
            biezacy = stos.pop()
            print('Zdejmujemy ze stosu : ', biezacy)

            if biezacy == self.meta:
                sciezka = self.odtworz_sciezke(skad_przyszedl, biezacy)
                # ZMODYFIKOWANY RETURN: Zwracamy też max rozmiar
                return sciezka, odwiedzone, max_rozmiar_stosu

            for sasiad in self.pobierz_sasiadow(biezacy[0], biezacy[1]):
                if sasiad not in odwiedzone:
                    odwiedzone.add(sasiad)
                    skad_przyszedl[sasiad] = biezacy
                    stos.append(sasiad)

            # NOWA LOGIKA: Aktualizuj maksymalny rozmiar po dodaniu sąsiadów
            if len(stos) > max_rozmiar_stosu:
                max_rozmiar_stosu = len(stos)

        # ZMODYFIKOWANY RETURN: Zwracamy też max rozmiar w przypadku porażki
        return None, odwiedzone, max_rozmiar_stosu