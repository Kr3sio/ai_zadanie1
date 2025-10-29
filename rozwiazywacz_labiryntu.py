import copy
# Importujemy naszą funkcję pomocniczą z innego pliku
from narzedzia import wczytaj_labirynt_z_csv


class RozwiazywaczLabiryntu:
    """
    Klasa bazowa do rozwiązywania labiryntów.
    Wczytuje labirynt z pliku CSV.
    """

    def __init__(self, nazwa_pliku_csv):
        self.labirynt = wczytaj_labirynt_z_csv(nazwa_pliku_csv)

        if not self.labirynt:
            raise ValueError(f"Nie udało się wczytać labiryntu z pliku: {nazwa_pliku_csv}")

        self.wiersze = len(self.labirynt)
        self.kolumny = len(self.labirynt[0]) if self.wiersze > 0 else 0
        self.start = None
        self.meta = None
        self._znajdz_start_i_mete()

    def _znajdz_start_i_mete(self):
        """Pomocnicza metoda do znalezienia współrzędnych 'S' i 'M'."""
        for r in range(self.wiersze):
            for c in range(self.kolumny):
                if self.labirynt[r][c] == 'S':
                    self.start = (r, c)
                elif self.labirynt[r][c] == 'M':
                    self.meta = (r, c)

        if not self.start:
            raise ValueError("Nie znaleziono startu 'S' w labiryncie.")
        if not self.meta:
            raise ValueError("Nie znaleziono mety 'M' w labiryncie.")

    def pobierz_sasiadow(self, r, c):
        """Zwraca listę ważnych (ruchomych) sąsiadów dla danej komórki."""
        sasiedzi = []
        kierunki = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in kierunki:
            nr, nc = r + dr, c + dc

            if 0 <= nr < self.wiersze and 0 <= nc < self.kolumny:
                if self.labirynt[nr][nc] != '1':
                    sasiedzi.append((nr, nc))
        return sasiedzi

    def odtworz_sciezke(self, skad_przyszedl, biezacy):
        """Odtwarza ścieżkę od mety do startu na podstawie mapy 'skad_przyszedl'."""
        sciezka = []
        while biezacy in skad_przyszedl:
            sciezka.append(biezacy)
            biezacy = skad_przyszedl[biezacy]
        sciezka.append(self.start)
        return sciezka[::-1]

    def pokaz_wynik(self, sciezka):
        """Wypisuje labirynt z zaznaczoną znalezioną ścieżką."""
        if not sciezka:
            print("PORAŻKA: Nie znaleziono ścieżki.")
            return

        print(f"SUKCES: Znaleziono ścieżkę o długości {len(sciezka)} kroków.")

        labirynt_wynikowy = copy.deepcopy(self.labirynt)

        for (r, c) in sciezka:
            if labirynt_wynikowy[r][c] not in ('S', 'M'):
                labirynt_wynikowy[r][c] = '*'

        for rzad in labirynt_wynikowy:
            print(" ".join(element.ljust(1) for element in rzad))

    def rozwiaz(self):
        """Metoda abstrakcyjna - implementowana przez klasy potomne."""
        raise NotImplementedError("Należy zaimplementować w podklasie.")