import colorama
from PrzeszukiwanieWszerz import PrzeszukiwanieWszerz
from PrzeszukiwanieWglab import PrzeszukiwanieWglab
# NOWY IMPORT: Do pomiaru czasu
from time import perf_counter

colorama.init()

if __name__ == "__main__":

    nazwa_pliku_labiryntu = "5x5v3.csv"

    try:
        print(f"************* Rozpoczynam przeszukiwanie wszerz (BFS) dla {nazwa_pliku_labiryntu} *****************")
        rozwiazywacz_bfs = PrzeszukiwanieWszerz(nazwa_pliku_labiryntu)

        # Mierzenie czasu START
        start_bfs = perf_counter()

        # ZMODYFIKOWANE WYWOŁANIE: Odbieramy 3 wartości
        sciezka_bfs, odwiedzone_bfs, max_kolejka = rozwiazywacz_bfs.rozwiaz()

        # Mierzenie czasu STOP
        czas_bfs = perf_counter() - start_bfs

        rozwiazywacz_bfs.pokaz_wynik(sciezka_bfs, odwiedzone_bfs)

        # NOWE INFORMACJE: Wyświetlanie statystyk
        print("\n--- Statystyki BFS ---")
        print(f"Czas wykonania: {czas_bfs:.6f} s")
        print(f"Maksymalna zajętość pamięci (węzły w kolejce): {max_kolejka}")

    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić BFS: {e}")

    print("\n" + "=" * 80 + "\n")  # Separator

    try:
        print(f"************* Rozpoczynam przeszukiwanie w głąb (DFS) dla {nazwa_pliku_labiryntu} *****************")
        rozwiazywacz_dfs = PrzeszukiwanieWglab(nazwa_pliku_labiryntu)

        # Mierzenie czasu START
        start_dfs = perf_counter()

        # ZMODYFIKOWANE WYWOŁANIE: Odbieramy 3 wartości
        sciezka_dfs, odwiedzone_dfs, max_stos = rozwiazywacz_dfs.rozwiaz()

        # Mierzenie czasu STOP
        czas_dfs = perf_counter() - start_dfs

        rozwiazywacz_dfs.pokaz_wynik(sciezka_dfs, odwiedzone_dfs)

        # NOWE INFORMACJE: Wyświetlanie statystyk
        print("\n--- Statystyki DFS ---")
        print(f"Czas wykonania: {czas_dfs:.6f} s")
        print(f"Maksymalna zajętość pamięci (węzły na stosie): {max_stos}")

    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić DFS: {e}")