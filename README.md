# Log Analyzer Tool
Narzędzie w Pythonie do automatycznej analizy logów systemowych i detekcji incydentów bezpieczeństwa.

## 🚀 Funkcjonalności
* Automatyczne czytanie plików `.log`
* Wykrywanie prób ataków (np. SQL Injection)
* Detekcja błędów krytycznych i nieudanych logowań
* Generowanie podsumowania incydentów

## 📂 Struktura
* `analyzer.py` - Główny kod skryptu
* `server.log` - Przykładowy plik logów do testów (symulacja ataku)

## 🛠️ Użycie
1. Pobierz repozytorium.
2. Upewnij się, że masz plik logów (np. `server.log`).
3. Uruchom analizę:
   ```bash
   python3 analyzer.py

 ##📊 Przykładowy wynik
   [!!!] ZNALEZIONE ZAGROŻENIA:
☠️ ATAK HAKERSKI: 2026-01-31 ... SQL Injection attempt detected!
🔴 KRYTYCZNE: 2026-01-31 ...
