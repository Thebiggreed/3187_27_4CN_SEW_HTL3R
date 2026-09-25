# STRG+ALT+Umschlat+L+
"""
Modul-Dokumentation -- Ähnlich zu JavaDoc.
Wird angezeigt z.B. mit help(__name__)
Dieses Modul beinhaltet Funktionen zur Berechnung der Fläche und der
Diagonale eines Rechtecks.

Doctests:

"""

# Metadaten zu dieser Datei:
__author__ = "Michael Czizek"
__example__ = "SEW4/01/F" #Gegenstand/Übungsblatt/Aufgabe
__date__ = "24.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"

import doctest

def is_palindrom(s:str) -> bool:
    """
    Die Funktion prüft ob der mitgegebene String von hinten nach vorne und anders herum gleich sind
    :param s:
    :return:
    """
    if s == s[::-1]:
        return True
    return False

def is_palindrom_sentence(s:str) -> bool:
    """
    Die Funktion prüft ob der mitgegebene String von hinten nach vorne und anders herum gleich sind
    :param s:
    :return:
    """
    s = s.lower().strip()
    if s == s[::-1]:
        return True
    return False


def palindrom_product(x) -> int:
    """
    Die Funktion ermittelt die größte Palindrom-Dezimalzahl (Natürliche Zahl kleiner als x), die das
    Produkt von zwei 3-stelligen Zahlen ist.
    :param x:
    :return:
    """
    gratest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            erg = i * j
            if is_palindrom(str(erg)):
                if erg > gratest:
                    gratest = erg
    return gratest

def get_dec_hex_palindrom(x) -> int:
    """
    Die Funktion ermittelt die größte Zahl (kleiner als x), die sowohl im Dezimalsystem als auch
    im Hexadezimalsystem ein Palindrom ist.
    :param x:
    :return:
    """
    gratest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            erg = i * j
            if is_palindrom(str(erg)):
                if is_palindrom(str(hex(erg))):
                    gratest = erg
    return gratest

def main() -> None:
    """
    Hauptfunktion des Programms.
    Fragt den Benutzer nach Breite und Höhe und gibt Fläche und Diagonale aus.
    Führt außerdem die Doctests aus.
    """
    doctest.testmod()
#-------------------------------------------------------------------------------------------
    is_palindrom("")
    is_palindrom_sentence("")
    palindrom_product("")
    get_dec_hex_palindrom("")


if __name__=="__main__":
    main()
