# Importujemy tylko te klasy, których potrzebujemy do uruchomienia
from przeszukiwanie_wszerz import PrzeszukiwanieWszerz
from przeszukiwanie_wglab import PrzeszukiwanieWglab

# Dobrą praktyką jest umieszczenie kodu startowego w bloku if __name__ == "__main__":
if __name__ == "__main__":

    nazwa_pliku_labiryntu = "5x5.csv"

    try:
        print(f"************* Rozpoczynam przeszukiwanie wszerz (BFS) dla {nazwa_pliku_labiryntu} *****************")
        rozwiazywacz_bfs = PrzeszukiwanieWszerz(nazwa_pliku_labiryntu)
        sciezka_bfs = rozwiazywacz_bfs.rozwiaz()
        rozwiazywacz_bfs.pokaz_wynik(sciezka_bfs)
    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić BFS: {e}")

    print("\n" + "=" * 80 + "\n")  # Separator

    try:
        print(f"************* Rozpoczynam przeszukiwanie w głąb (DFS) dla {nazwa_pliku_labiryntu} *****************")
        rozwiazywacz_dfs = PrzeszukiwanieWglab(nazwa_pliku_labiryntu)
        sciezka_dfs = rozwiazywacz_dfs.rozwiaz()
        rozwiazywacz_dfs.pokaz_wynik(sciezka_dfs)
    except (ValueError, FileNotFoundError) as e:
        print(f"Nie udało się uruchomić DFS: {e}")