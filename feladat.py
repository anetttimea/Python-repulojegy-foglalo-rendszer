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