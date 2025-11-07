import copy
from narzedzia import wczytaj_labirynt_z_csv
from colorama import Fore, Style


class RozwiazywaczLabiryntu:


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


    def pokaz_wynik(self, sciezka, odwiedzone):


        if not sciezka:
            print(f"{Fore.RED}PORAŻKA: Nie znaleziono ścieżki.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}SUKCES: Znaleziono ścieżkę o długości {len(sciezka)} kroków.{Style.RESET_ALL}")


        # Pomijanie wypisywania w konsoli jeśli za duży rozmiar
        if self.wiersze > 50 or self.kolumny > 50:
            print(
                f"Macierz wyników jest za duża do wyświetlenia w konsoli ({self.wiersze}x{self.kolumny}). Pomijam drukowanie.")
        else:
            print("\nMacierz wyników (KONSOLA):")
            zbior_sciezki = set(sciezka) if sciezka else set()

            for r in range(self.wiersze):
                elementy_rzedu_kolorowe = []
                for c in range(self.kolumny):
                    wspolrzedne = (r, c)
                    element_numeryczny = 0

                    if self.labirynt[r][c] == '1':
                        element_numeryczny = 1
                    elif wspolrzedne in zbior_sciezki:
                        element_numeryczny = 3
                    elif wspolrzedne in odwiedzone:
                        element_numeryczny = 2
                    else:
                        element_numeryczny = 0

                    # Dodawanie kolorów na podstawie wartości numerycznej
                    if element_numeryczny == 3:
                        elementy_rzedu_kolorowe.append(f"{Fore.GREEN}{element_numeryczny}{Style.RESET_ALL}")
                    elif element_numeryczny == 1:
                        elementy_rzedu_kolorowe.append(f"{Style.DIM}{element_numeryczny}{Style.RESET_ALL}")
                    elif element_numeryczny == 2:
                        elementy_rzedu_kolorowe.append(f"{Fore.YELLOW}{element_numeryczny}{Style.RESET_ALL}")
                    else:
                        elementy_rzedu_kolorowe.append(str(element_numeryczny))

                print(" ".join(elementy_rzedu_kolorowe))

    def rozwiaz(self):
        #Metoda abstrakcyjna - implementowana przez klasy potomne
        raise NotImplementedError("Należy zaimplementować w podklasie.")