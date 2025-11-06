import csv


def wczytaj_labirynt_z_csv(nazwa_pliku):
    # Wczytuje labirynt z pliku CSV
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




def zapisz_rozwiazanie_do_txt(nazwa_pliku, nazwa_algorytmu, sciezka, odwiedzone, labirynt, wiersze, kolumny):
    """
    Zapisuje macierz wyników (0,1,2,3) do pliku tekstowego w trybie DOŁĄCZANIA (append).
    """
    print(f"Dopisywanie rozwiązania (tekst) dla {nazwa_algorytmu} do pliku: {nazwa_pliku}...")

    zbior_sciezki = set(sciezka) if sciezka else set()

    try:
        # 'a' (append/dołącz)
        with open(nazwa_pliku, 'a', encoding='utf-8') as f:

            f.write(f"\n" + "=" * 80 + "\n")
            f.write(f"--- WYNIK DLA: {nazwa_algorytmu} ---\n")
            if not sciezka:
                f.write("PORAŻKA: Nie znaleziono ścieżki.\n\n")
            else:
                f.write(f"SUKCES: Znaleziono ścieżkę o długości {len(sciezka)} kroków.\n\n")

            # Zapisanie macierzy
            for r in range(wiersze):
                elementy_rzedu = []
                for c in range(kolumny):
                    wspolrzedne = (r, c)
                    element_numeryczny = 0

                    if labirynt[r][c] == '1':
                        element_numeryczny = 1
                    elif wspolrzedne in zbior_sciezki:
                        element_numeryczny = 3
                    elif wspolrzedne in odwiedzone:
                        element_numeryczny = 2
                    else:
                        element_numeryczny = 0

                    elementy_rzedu.append(str(element_numeryczny))

                # Zapisz wiersz do pliku, oddzielony spacjami
                f.write(" ".join(elementy_rzedu) + "\n")

        print(f"Pomyślnie dopisano rozwiązanie (tekst) do {nazwa_pliku}.")

    except Exception as e:
        print(f"BŁĄD: Nie udało się zapisać pliku rozwiązania. {e}")

