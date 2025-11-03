import copy
from narzedzia import wczytaj_labirynt_z_csv
# NOWY IMPORT
from colorama import Fore, Style


class RozwiazywaczLabiryntu:
    """
    Klasa bazowa do rozwiązywania labiryntów.
    Wczytuje labirynt z pliku CSV.
    """

    # --- Metody __init__, _znajdz_start_i_mete, pobierz_sasiadow, odtworz_sciezke ---
    # --- POZOSTAJĄ BEZ ZMIAN ---

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
        for r in range(self.wiersze):
            for c in range(self.kolumny):
                if self.labirynt[r][c] == 'S':
                    self.start = (r, c)
                elif self.labirynt[r][c] == 'M':
                    self.meta = (r, c)

        if not self.start:
            raise ValueError("Nie znaleziono startu 'S' w labiyncie.")
        if not self.meta:
            raise ValueError("Nie znaleziono mety 'M' w labiyncie.")

    def pobierz_sasiadow(self, r, c):
        sasiedzi = []
        kierunki = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in kierunki:
            nr, nc = r + dr, c + dc

            if 0 <= nr < self.wiersze and 0 <= nc < self.kolumny:
                if self.labirynt[nr][nc] != '1':
                    sasiedzi.append((nr, nc))
        return sasiedzi

    def odtworz_sciezke(self, skad_przyszedl, biezacy):
        sciezka = []
        while biezacy in skad_przyszedl:
            sciezka.append(biezacy)
            biezacy = skad_przyszedl[biezacy]
        sciezka.append(self.start)
        return sciezka[::-1]

    # --- KONIEC METOD BEZ ZMIAN ---

    # vvv ZASTĄP CAŁĄ PONIŻSZĄ METODĘ vvv

    def pokaz_wynik(self, sciezka, odwiedzone):
        """
        Drukuje wynik w formie macierzy liczbowej (0,1,2,3) ORAZ
        używa kolorów do wyróżnienia ścieżki (3) i ścian (1).
        """

        if not sciezka:
            print(f"{Fore.RED}PORAŻKA: Nie znaleziono ścieżki.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}SUKCES: Znaleziono ścieżkę o długości {len(sciezka)} kroków.{Style.RESET_ALL}")

        print("\nMacierz wyników (0: nieodwiedzone, 1: ściana, 2: odwiedzone, 3: ścieżka):")

        zbior_sciezki = set(sciezka) if sciezka else set()

        # Pętla budująca i drukująca macierz wiersz po wierszu
        for r in range(self.wiersze):
            elementy_rzedu_kolorowe = []  # Lista na kolorowe stringi

            for c in range(self.kolumny):
                wspolrzedne = (r, c)
                element_numeryczny = 0  # Domyślnie 0

                if self.labirynt[r][c] == '1':
                    element_numeryczny = 1
                elif wspolrzedne in zbior_sciezki:
                    element_numeryczny = 3
                elif wspolrzedne in odwiedzone:
                    element_numeryczny = 2
                else:
                    element_numeryczny = 0  # Pozostaje 0

                # Teraz dodajemy kolory na podstawie wartości numerycznej
                if element_numeryczny == 3:
                    # ŚCIEŻKA (jasnozielona)
                    elementy_rzedu_kolorowe.append(f"{Fore.GREEN}{element_numeryczny}{Style.RESET_ALL}")

                elif element_numeryczny == 2:
                    # ŚCIEŻKA (żółta)
                    elementy_rzedu_kolorowe.append(f"{Fore.YELLOW}{element_numeryczny}{Style.RESET_ALL}")
                else:
                    # NIEODWIEDZONE (0) (domyślny kolor)
                    elementy_rzedu_kolorowe.append(str(element_numeryczny))

            # Drukujemy cały wiersz złożony z pokolorowanych stringów
            print(" ".join(elementy_rzedu_kolorowe))

    # ^^^ ZASTĄP CAŁĄ POWYŻSZĄ METODĘ ^^^

    def rozwiaz(self):
        """Metoda abstrakcyjna - implementowana przez klasy potomne."""
        raise NotImplementedError("Należy zaimplementować w podklasie.")