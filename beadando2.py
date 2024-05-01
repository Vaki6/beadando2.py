from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def osszesites(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)  # Például 10 000 forint egyágyas szobára

    def osszesites(self):
        return self.ar

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # Például 15 000 forint ketágyas szobára

    def osszesites(self):
        return self.ar

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas1(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if not self.is_szoba_foglalt(szobaszam, datum):
                    foglalas_ar = szoba.osszesites()
                    self.foglalasok.append((szobaszam, datum))
                    return foglalas_ar, szobaszam
                else:
                    print("A szoba már foglalt ezen a dátumon.")
                    return None, None
        print("Nem található ilyen szobaszám.")
        return None, None
    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if not self.is_szoba_foglalt(szobaszam, datum):
                    foglalas_ar = szoba.osszesites()
                    self.foglalasok.append((szobaszam, datum))
                    print(f"Sikeres foglalás a(z) {szobaszam} szobára a következő dátumra: {datum}")
                    return foglalas_ar, szobaszam
                else:
                    print("A szoba már foglalt ezen a dátumon.")
                    return None, None
        print("Nem található ilyen szobaszám.")
        return None, None

    def is_szoba_foglalt(self, szobaszam, datum):
        # Ellenőrizzük, hogy a szoba már foglalt-e az adott dátumon
        for foglalas in self.foglalasok:
            if foglalas[0] == szobaszam and foglalas[1] == datum:
                return True
        return False

    def foglalas_lemondasa(self, szobaszam, datum):
        foglalas = (szobaszam, datum)
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print(f"A(z) {szobaszam} számú szoba foglalása a következő dátumra törölve lett: {datum}")
        else:
            print("A foglalás nem található.")

    def listazas(self):
        print("Összes foglalás:")
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas[0]}, Dátum: {foglalas[1]}")


def main():
    # Szálloda létrehozása
    szalloda = Szalloda("Példa Szálloda")

    # Szobák hozzáadása a szállodához
    szoba1 = EgyagyasSzoba(101)
    szoba2 = EgyagyasSzoba(102)
    szoba3 = KetagyasSzoba(201)

    szalloda.uj_szoba(szoba1)
    szalloda.uj_szoba(szoba2)
    szalloda.uj_szoba(szoba3)

    # Foglalások
    szalloda.foglalas1(101, "2024-05-26")
    szalloda.foglalas1(102, "2024-05-27")
    szalloda.foglalas1(201, "2024-05-28")
    szalloda.foglalas1(101, "2024-05-29")
    szalloda.foglalas1(101, "2024-05-30")

    # Felhasználói adatbekérés
    exit_flag = False

    while not exit_flag:
        print("\nVálassz egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Listázás")
        print("4. Kilépés")

        valasztas = input("Választás (1-4): ")

        if valasztas == "1":
            szobaszam = int(input("Add meg a foglalni kívánt szobaszámot: "))
            datum = input("Add meg a foglalni kívánt dátumot (YYYY-MM-DD): ")
            szalloda.foglalas(szobaszam, datum)
        elif valasztas == "2":
            szobaszam = int(input("Add meg a lemondani kívánt foglalás szobaszámát: "))
            datum = input("Add meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD): ")
            szalloda.foglalas_lemondasa(szobaszam, datum)
        elif valasztas == "3":
            szalloda.listazas()
        elif valasztas == "4":
            print("Kilépés...")
            exit_flag = True
        else:
            print("Érvénytelen választás. Kérlek, válassz egy számot 1 és 4 között.")


if __name__ == "__main__":
    main()
