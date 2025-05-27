from abc import ABC, abstractmethod
from datetime import datetime

#Absztrakt osztály
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass

    def __str__(self):
        return f"{self.jaratszam} - {self.celallomas} ({self.jarat_tipus()}) - {self.jegyar} Ft"

class BelfoldiJarat(Jarat):
    def jarat_tipus(self):
        return "Belföldi"
    
class NemzetkoziJarat(Jarat):
    def jarat_tipus(self):
        return "Nemzetközi"

class JegyFoglalas:
    def __init__(self, jarat, utas_nev, datum):
        self.jarat = jarat
        self.utas_nev = utas_nev
        self.datum = datum

    def __str__(self):
        return f"{self.utas_nev} - {self.jarat.jaratszam} ({self.jarat.celallomas}) - {self.datum.strftime('%Y-%m-%d')}"

class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def listaz_jaratok(self):
        for jarat in self.jaratok:
            print(jarat)

    def foglalas(self, jaratszam, utas_nev, datum_str):
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        if datum < datetime.now():
            print("Hiba: A megadott dátum már elmúlt.")
            return

        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                foglalas = JegyFoglalas(jarat, utas_nev, datum)
                self.foglalasok.append(foglalas)
                print(f"Foglalás sikeres! Ár: {jarat.jegyar} Ft")
                return
        print("Hiba: Nincs ilyen járatszám.")

    def lemondas(self, jaratszam, utas_nev):
        for foglalas in self.foglalasok:
            if foglalas.jarat.jaratszam == jaratszam and foglalas.utas_nev == utas_nev:
                self.foglalasok.remove(foglalas)
                print("Foglalás lemondva.")
                return
        print("Hiba: A megadott foglalás nem található.")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        for f in self.foglalasok:
            print(f)
def main():
    airline = Legitarsasag("Python Airlines")

    #Előre betöltött járatok
    j1 = BelfoldiJarat("B101", "Budapest", 15000)
    j2 = NemzetkoziJarat("N202", "London", 55000)
    j3 = NemzetkoziJarat("N303", "Berlin", 45000)

    airline.hozzaad_jarat(j1)
    airline.hozzaad_jarat(j2)
    airline.hozzaad_jarat(j3)

    elo_foglalasok = [
        ("Kovács Anna", "B101", "2025-07-01"),
        ("Szabó Béla", "N202", "2025-08-15"),
        ("Tóth Gábor", "N303", "2025-06-10"),
        ("Nagy Eszter", "N202", "2025-09-01"),
        ("Kiss József", "B101", "2025-07-20"),
        ("Horváth Dóra", "N303", "2025-06-15"),
    ]

    print("\n--- Előre betöltött foglalások ---")
    for nev, jaratszam, datum in elo_foglalasok:
        airline.foglalas(jaratszam, nev, datum)

    print("\n--- Jelenlegi foglalások ---")
    airline.listaz_foglalasok()

    print("\n--- Jegyfolaló rendszer elindítva ---")
    while True:
        print("\n--- Airlines ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("0. Kilépés")

        valasztas = input("Válasszon egy műveletet: ")

        if valasztas == "1":
            airline.listaz_jaratok()
            jaratszam = input("Add meg a járatszámot: ")
            utas = input("Utas neve: ")
            datum = input("Utazás dátuma (YYYY-MM-DD): ")
            airline.foglalas(jaratszam, utas, datum)

        elif valasztas == "2":
            utas = input("Utas neve: ")
            jaratszam = input("Add meg a járatszámot: ")
            airline.lemondas(jaratszam, utas)

        elif valasztas == "3":
            airline.listaz_foglalasok()

        elif valasztas == "4":
            airline.listaz_jaratok()

        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
