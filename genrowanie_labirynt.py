import csv
from tqdm import tqdm  # pip install tqdm

# Rozmiar macierzy
N = 10000

# Nazwa pliku wyjściowego
filename = "macierz_10000x10000.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    for i in tqdm(range(N), desc="Generowanie CSV", unit="wiersz"):
        # Tworzymy wiersz wypełniony zerami
        row = ['0'] * N
        if i == 0:
            row[0] = 'S'  # Lewy górny róg
        if i == N - 1:
            row[-1] = 'M'  # Prawy dolny róg
        writer.writerow(row)

print(f"\n✅ Plik '{filename}' został utworzony pomyślnie ({N}x{N}).")
