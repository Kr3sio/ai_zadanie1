import heapq
from rozwiazywacz_labiryntu import RozwiazywaczLabiryntu


"""algorytm A* (A-gwiazdka) to doskonały, wydajny sposób rozwiązywania tego typu problemów.
 W przeciwieństwie do BFS (który ślepo szuka we wszystkich kierunkach) i DFS (który idzie na ślepo w głąb),
  A* jest algorytmem "poinformowanym".Używa heurystyki, aby inteligentnie zgadywać,
   która ścieżka jest najbardziej obiecująca i bada ją w pierwszej kolejności.Jak to działa?
   A* wybiera następny krok na podstawie wzoru: $f(n) = g(n) + h(n)$$g(n)$ = Rzeczywisty koszt dotarcia 
   z punktu 'S' do bieżącego pola (czyli liczba kroków, którą już zrobiliśmy).$h(n)$ = Heurystyka, 
   czyli szacowany koszt dotarcia z bieżącego pola do mety 'M'. Użyjemy odległości Manhattan 
   (suma różnic w osi X i Y), ponieważ jest bardzo szybka i nigdy nie przeszacowuje kosztu.
   $f(n)$ = Łączny (rzeczywisty + szacowany) koszt.
 A* zawsze wybiera pole o najniższym $f(n)$."""

class PrzeszukiwanieAGwiazdka(RozwiazywaczLabiryntu):
    """
    Implementuje strategię przeszukiwania A* (A-gwiazdka).
    Używa kolejki priorytetowej do znajdowania optymalnej ścieżki.
    """

    def _heurystyka_manhattan(self, pozycja):
        """Oblicza heurystykę - odległość Manhattan do mety."""
        (r, c) = pozycja
        (meta_r, meta_c) = self.meta
        return abs(r - meta_r) + abs(c - meta_c)

    def rozwiaz(self):
        # Kolejka priorytetowa (min-heap) przechowuje krotki:
        # (f_score, pozycja)
        # f_score = g_score + h_score
        front_kolejka_prio = []

        # Słowniki do śledzenia kosztów
        # g_score: Rzeczywisty koszt od startu do węzła
        g_score = {self.start: 0}
        # f_score: Całkowity szacowany koszt (g + h)
        f_score = {self.start: self._heurystyka_manhattan(self.start)}

        # Dodajemy węzeł startowy do kolejki
        heapq.heappush(front_kolejka_prio, (f_score[self.start], self.start))

        skad_przyszedl = {}

        # Zbiór wszystkich węzłów, które kiedykolwiek trafiły do kolejki
        # Używany do raportowania 'odwiedzonych' pól (wartość 2)
        odwiedzone_do_raportu = {self.start}

        max_rozmiar_frontu = 1

        while front_kolejka_prio:
            # Pobierz węzeł o najniższym f_score
            _f_biezacy, biezacy = heapq.heappop(front_kolejka_prio)

            # --- Cel osiągnięty ---
            if biezacy == self.meta:
                sciezka = self.odtworz_sciezke(skad_przyszedl, biezacy)
                return sciezka, odwiedzone_do_raportu, max_rozmiar_frontu

            # --- Rozwijanie sąsiadów ---
            for sasiad in self.pobierz_sasiadow(biezacy[0], biezacy[1]):
                # Koszt dotarcia do sąsiada przez bieżący węzeł
                # W labiryncie koszt każdego kroku to 1
                tentatywny_g_score = g_score[biezacy] + 1

                # Pobieramy obecny g_score sąsiada (domyślnie nieskończoność)
                obecny_g_score_sasiada = g_score.get(sasiad, float('inf'))

                # Jeśli znaleźliśmy lepszą (krótszą) drogę do tego sąsiada
                if tentatywny_g_score < obecny_g_score_sasiada:
                    # Zapisujemy nową, lepszą ścieżkę
                    skad_przyszedl[sasiad] = biezacy
                    g_score[sasiad] = tentatywny_g_score

                    # Obliczamy nowy f_score dla sąsiada
                    h_sasiad = self._heurystyka_manhattan(sasiad)
                    nowy_f_score = tentatywny_g_score + h_sasiad
                    f_score[sasiad] = nowy_f_score

                    # Dodajemy sąsiada do kolejki priorytetowej
                    heapq.heappush(front_kolejka_prio, (nowy_f_score, sasiad))

                    # Oznaczamy węzeł jako "dotknięty"
                    odwiedzone_do_raportu.add(sasiad)

            # Aktualizacja statystyk pamięci
            if len(front_kolejka_prio) > max_rozmiar_frontu:
                max_rozmiar_frontu = len(front_kolejka_prio)

        # Nie znaleziono ścieżki
        return None, odwiedzone_do_raportu, max_rozmiar_frontu