import colorama
from przeszukiwanie_wszerz import PrzeszukiwanieWszerz
from przeszukiwanie_wglab import PrzeszukiwanieWglab
from przeszukiwanie_a_gwiazdka import PrzeszukiwanieAGwiazdka
from time import perf_counter
import os

colorama.init()

if __name__ == "__main__":

    liczczasy = False

    plikBFS = open("plikBFS.txt", "a", encoding='utf-8')
    plikDFS = open("plikDFS.txt", "a", encoding='utf-8')
    plikAStar = open("plikAStar.txt", "a", encoding='utf-8')

    czasBFS = 0
    czasDFS = 0
    czasAStar = 0

    sredniCzasBFS = 0
    sredniCzasDFS = 0
    sredniCzasAStar = 0


    nazwa_pliku_labiryntu = "macierz_10000x10000.csv"
    # nazwa_pliku_labiryntu = "5x5.csv"
    nazwa_pliku_txt = "rozwiazanie.txt"

    # Usuwanie pliku z wynikami jeśli istniał
    if os.path.exists(nazwa_pliku_txt):
        os.remove(nazwa_pliku_txt)
        print(f"Usunięto stary plik wyników: {nazwa_pliku_txt}")


    for i in range(5):
        # --- Sekcja BFS ---
        try:
            print(f"\n************* Rozpoczynam przeszukiwanie wszerz (BFS) dla {nazwa_pliku_labiryntu} *****************")
            rozwiazywacz_bfs = PrzeszukiwanieWszerz(nazwa_pliku_labiryntu)

            start_bfs = perf_counter()
            sciezka_bfs, odwiedzone_bfs, max_kolejka = rozwiazywacz_bfs.rozwiaz()
            czas_bfs = perf_counter() - start_bfs

            rozwiazywacz_bfs.pokaz_wynik(sciezka_bfs, odwiedzone_bfs)

            # Zapisz do pliku
            # zapisz_rozwiazanie_do_txt(
            #     nazwa_pliku_txt, "BFS", sciezka_bfs, odwiedzone_bfs,
            #     rozwiazywacz_bfs.labirynt, rozwiazywacz_bfs.wiersze, rozwiazywacz_bfs.kolumny
            # )

            print("\n--- Statystyki BFS ---")
            print(f"Czas wykonania: {czas_bfs:.6f} s")
            print(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_bfs)}")
            print(f"Maksymalna zajętość pamięci (węzły w kolejce): {max_kolejka}")

            plikBFS.write(f"Czas wykonania: {czas_bfs:.6f} s \n")
            plikBFS.write(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_bfs)} \n")
            plikBFS.write(f"Maksymalna zajętość pamięci (węzły w kolejce): {max_kolejka} \n\n")

            plikBFS.write("Nowe przejście \n")

            sredniCzasDFS += czas_bfs

            if(liczczasy):

                if(czas_bfs < czasBFS or czasBFS == 0):
                    czasBFS = czas_bfs

                sredniCzasBFS = sredniCzasBFS/5
                plikBFS.write(f"Średni czas wykonania BFS: {sredniCzasBFS} \n")


                plikBFS.write(f"Minimalny czas wykonania: {czasBFS:.6f} s \n")

        except (ValueError, FileNotFoundError) as e:
            print(f"Nie udało się uruchomić BFS: {e}")

        print("\n" + "=" * 80 + "\n")  # Separator


    for i in range(5):
        # --- Sekcja DFS ---
        try:
            print(f"************* Rozpoczynam przeszukiwanie w głąb (DFS) dla {nazwa_pliku_labiryntu} *****************")
            rozwiazywacz_dfs = PrzeszukiwanieWglab(nazwa_pliku_labiryntu)

            start_dfs = perf_counter()
            sciezka_dfs, odwiedzone_dfs, max_stos = rozwiazywacz_dfs.rozwiaz()
            czas_dfs = perf_counter() - start_dfs

            rozwiazywacz_dfs.pokaz_wynik(sciezka_dfs, odwiedzone_dfs)

            # Zapisz do pliku
            # zapisz_rozwiazanie_do_txt(
            #     nazwa_pliku_txt, "DFS", sciezka_dfs, odwiedzone_dfs,
            #     rozwiazywacz_dfs.labirynt, rozwiazywacz_dfs.wiersze, rozwiazywacz_dfs.kolumny
            # )

            print("\n--- Statystyki DFS ---")
            print(f"Czas wykonania: {czas_dfs:.6f} s")
            print(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_dfs)}")
            print(f"Maksymalna zajętość pamięci (węzły na stosie): {max_stos}")

            plikDFS.write(f"Czas wykonania: {czas_dfs:.6f} s \n")
            plikDFS.write(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_dfs)} \n")
            plikDFS.write(f"Maksymalna zajętość pamięci (węzły w kolejce): {max_stos} \n\n")

            plikDFS.write("Nowe przejście \n")

            if (liczczasy):
                sredniCzasDFS += czas_dfs

                if (czas_dfs < czasDFS or czasDFS == 0):
                    czasDFS = czas_dfs

                sredniCzasDFS = sredniCzasDFS / 5
                plikDFS.write(f"Średni czas wykonania BFS: {sredniCzasDFS} \n")

                plikDFS.write(f"Minimalny czas wykonania: {czasDFS:.6f} s \n")


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

        rozwiazywacz_a_gwiazdka.pokaz_wynik(sciezka_a, odwiedzone_a)

        # Zapisz do pliku
        # zapisz_rozwiazanie_do_txt(
        #     nazwa_pliku_txt, "A* (A-gwiazdka)", sciezka_a, odwiedzone_a,
        #     rozwiazywacz_a_gwiazdka.labirynt, rozwiazywacz_a_gwiazdka.wiersze, rozwiazywacz_a_gwiazdka.kolumny
        # )

        print("\n--- Statystyki A* ---")
        print(f"Czas wykonania: {czas_a_gwiazdka:.6f} s")
        print(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_a)}")
        print(f"Maksymalna zajętość pamięci (węzły w kolejce priorytetowej): {max_front}")

        plikAStar.write(f"Czas wykonania: {czas_a_gwiazdka:.6f} s \n")
        plikAStar.write(f"Liczba przeszukanych pól (odwiedzone + ścieżka): {len(odwiedzone_a)} \n")
        plikAStar.write(f"Maksymalna zajętość pamięci (węzły w kolejce): {max_front} \n\n")

        plikAStar.write("Nowe przejście \n")

        if (liczczasy):
            sredniCzasAStar += czas_a_gwiazdka

            if (czas_a_gwiazdka < czasAStar or czasAStar == 0):
                czasAStar = czas_a_gwiazdka

            sredniCzasAStar = sredniCzasAStar / 5
            plikAStar.write(f"Średni czas wykonania BFS: {sredniCzasAStar} \n")

            plikAStar.write(f"Minimalny czas wykonania: {czasAStar:.6f} s \n")



    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić A*: {e}")