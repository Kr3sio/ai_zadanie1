import csv


def wczytaj_labirynt_z_csv(nazwa_pliku):
    """Wczytuje labirynt z pliku CSV i zwraca jako listę list."""
    labirynt_mapa = []
    try:
        with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
            czytnik_csv = csv.reader(plik)
            for rzad in czytnik_csv:
                if rzad:
                    labirynt_mapa.append([komorka.strip() for komorka in rzad])
    except FileNotFoundError:
        print(f"BŁĄD: Nie znaleziono pliku {nazwa_pliku}")
        return None
    except Exception as e:
        print(f"BŁĄD podczas wczytywania pliku: {e}")
        return None

    if not labirynt_mapa:
        print("BŁĄD: Plik CSV jest pusty lub niepoprawnie sformatowany.")
        return None

    return labirynt_mapa