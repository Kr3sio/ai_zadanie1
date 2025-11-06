
import colorama
from przeszukiwanie_wszerz import PrzeszukiwanieWszerz
from przeszukiwanie_wglab import PrzeszukiwanieWglab
from przeszukiwanie_a_gwiazdka import PrzeszukiwanieAGwiazdka
from time import perf_counter
import os

from narzedzia import zapisz_rozwiazanie_do_txt


colorama.init()

if __name__ == "__main__":

    nazwa_pliku_labiryntu = "5x5.csv"
    nazwa_pliku_txt = "rozwiazanie.txt"

    # Czyszczenie starego pliku tekstowego
    if os.path.exists(nazwa_pliku_txt):
        os.remove(nazwa_pliku_txt)
        print(f"Usunięto stary plik wyników: {nazwa_pliku_txt}")

    # --- Sekcja BFS ---
    try:
        print(f"\n************* Rozpoczynam przeszukiwanie wszerz (BFS) dla {nazwa_pliku_labiryntu} *****************")
        rozwiazywacz_bfs = PrzeszukiwanieWszerz(nazwa_pliku_labiryntu)

        start_bfs = perf_counter()
        sciezka_bfs, odwiedzone_bfs, max_kolejka = rozwiazywacz_bfs.rozwiaz()
        czas_bfs = perf_counter() - start_bfs

        # 1. Wywołanie drukowania na KONSOLI (z kolorami)

        rozwiazywacz_bfs.pokaz_wynik(sciezka_bfs, odwiedzone_bfs)

        # 2. Wywołanie zapisu do PLIKU (bez kolorów)
        zapisz_rozwiazanie_do_txt(
            nazwa_pliku_txt, "BFS", sciezka_bfs, odwiedzone_bfs,
            rozwiazywacz_bfs.labirynt, rozwiazywacz_bfs.wiersze, rozwiazywacz_bfs.kolumny
        )

        print("\n--- Statystyki BFS ---")
        print(f"Czas wykonania: {czas_bfs:.6f} s")
        print(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_bfs)}")
        print(f"Maksymalna zajętość pamięci (węzły w kolejce): {max_kolejka}")

    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić BFS: {e}")

    print("\n" + "=" * 80 + "\n")  # Separator

    # --- Sekcja DFS ---
    try:
        print(f"************* Rozpoczynam przeszukiwanie w głąb (DFS) dla {nazwa_pliku_labiryntu} *****************")
        rozwiazywacz_dfs = PrzeszukiwanieWglab(nazwa_pliku_labiryntu)

        start_dfs = perf_counter()
        sciezka_dfs, odwiedzone_dfs, max_stos = rozwiazywacz_dfs.rozwiaz()
        czas_dfs = perf_counter() - start_dfs

        # 1. Wywołanie drukowania na KONSOLI (z kolorami)
        rozwiazywacz_dfs.pokaz_wynik(sciezka_dfs, odwiedzone_dfs)

        # 2. Wywołanie zapisu do PLIKU (bez kolorów)
        zapisz_rozwiazanie_do_txt(
            nazwa_pliku_txt, "DFS", sciezka_dfs, odwiedzone_dfs,
            rozwiazywacz_dfs.labirynt, rozwiazywacz_dfs.wiersze, rozwiazywacz_dfs.kolumny
        )

        print("\n--- Statystyki DFS ---")
        print(f"Czas wykonania: {czas_dfs:.6f} s")
        print(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_dfs)}")
        print(f"Maksymalna zajętość pamięci (węzły na stosie): {max_stos}")

    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić DFS: {e}")

    print("\n" + "=" * 80 + "\n")  # Separator

    # --- Sekcja A* ---
    try:
        print(f"************* Rozpoczynam przeszukiwanie A* (A-gwiazdka) dla {nazwa_pliku_labiryntu} *****************")
        rozwiazywacz_a_gwiazdka = PrzeszukiwanieAGwiazdka(nazwa_pliku_labiryntu)

        start_a_gwiazdka = perf_counter()
        sciezka_a, odwiedzone_a, max_front = rozwiazywacz_a_gwiazdka.rozwiaz()
        czas_a_gwiazdka = perf_counter() - start_a_gwiazdka

        # 1. Wywołanie drukowania na KONSOLI (z kolorami)
        rozwiazywacz_a_gwiazdka.pokaz_wynik(sciezka_a, odwiedzone_a)

        # 2. Wywołanie zapisu do PLIKU (bez kolorów)
        zapisz_rozwiazanie_do_txt(
            nazwa_pliku_txt, "A* (A-gwiazdka)", sciezka_a, odwiedzone_a,
            rozwiazywacz_a_gwiazdka.labirynt, rozwiazywacz_a_gwiazdka.wiersze, rozwiazywacz_a_gwiazdka.kolumny
        )

        print("\n--- Statystyki A* ---")
        print(f"Czas wykonania: {czas_a_gwiazdka:.6f} s")
        print(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_a)}")
        print(f"Maksymalna zajętość pamięci (węzły w kolejce priorytetowej): {max_front}")

    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić A*: {e}")