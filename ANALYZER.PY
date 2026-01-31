import sys

def analyze_logs(filename):
    print(f"--- ROZPOCZYNAM ANALIZĘ PLIKU: {filename} ---")
    
    try:
        # Otwieramy plik do odczytu ('r' = read)
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        error_count = 0
        critical_count = 0
        
        print("\n[!!!] ZNALEZIONE ZAGROŻENIA:")
        
        # Pętla sprawdzająca każdą linię po kolei
        for line in lines:
            line = line.strip() # Czyścimy puste znaki
            
            # Szukamy słów kluczowych
            if "CRITICAL" in line:
                print(f"🔴 KRYTYCZNE: {line}")
                critical_count += 1
            elif "ERROR" in line:
                print(f"🟠 BŁĄD: {line}")
                error_count += 1
            elif "SQL Injection" in line:
                print(f"☠️ ATAK HAKERSKI: {line}")
        
        print("-" * 40)
        print(f"Raport:")
        print(f"Znaleziono {error_count} błędów")
        print(f"Znaleziono {critical_count} zdarzeń krytycznych")
        print("-" * 40)
        
    except FileNotFoundError:
        print("BŁĄD: Nie znaleziono pliku z logami!")

if __name__ == "__main__":
    # Domyślnie szukamy w pliku server.log
    analyze_logs("server.log")