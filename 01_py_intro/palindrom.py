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
__example__ = "SEW4/01/F"  # Gegenstand/Übungsblatt/Aufgabe
__date__ = "24.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"

import doctest


def is_palindrom(s: str) -> bool:
    """
    Die Funktion prüft ob der mitgegebene String von hinten nach vorne und anders herum gleich sind
    :param s:
    :return:
    >>> is_palindrom("353")
    True
    """
    if s == s[::-1]:
        return True
    return False


def is_palindrom_sentence(s: str) -> bool:
    """
    Die Funktion prüft ob der mitgegebene String von hinten nach vorne und anders herum gleich sind
    :param s:
    :return:
    >>> is_palindrom_sentence("Was it a car or a cat I saw")
    True
    """
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        return True
    return False

def palindrom_product(x) -> int:
    """
    Die Funktion ermittelt die größte Palindrom-Dezimalzahl (Natürliche Zahl kleiner als x), die das
    Produkt von zwei 3-stelligen Zahlen ist.
    :param x:
    :return:
    >>> palindrom_product(600_000)
    595595
    """
    gratest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            erg = i * j
            if is_palindrom(str(erg)) and x > erg:
                if erg > gratest:
                    gratest = erg
    return gratest


def get_dec_hex_palindrom(x) -> int:
    """
    Die Funktion ermittelt die größte Zahl (kleiner als x), die sowohl im Dezimalsystem als auch
    im Hexadezimalsystem ein Palindrom ist.
    :param x:
    :return:
    >>> get_dec_hex_palindrom(400)
    353
    """
    gratest = 0
    for i in range(0, x):
        if is_palindrom(str(i)) and x > i:
            if is_palindrom(str(hex(i)[2:])):
                gratest = i
    return gratest


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
    """
    if not (2 <= base <= 36):
        raise ValueError("base muss zwischen 2 und 36 liegen")
    ziffern = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if number == 0:
        return "0"
    result = ""
    n = abs(number)
    while n > 0:
        n, rest = divmod(n, base) # returned tuble(n // base, n % base)
        result = ziffern[rest] + result

    if number < 0:
        result = "-" + result

    return result


def main() -> None:
    """
    Hauptfunktion des Programms.
    Fragt den Benutzer nach Breite und Höhe und gibt Fläche und Diagonale aus.
    Führt außerdem die Doctests aus.
    """
    doctest.testmod()
    # -------------------------------------------------------------------------------------------
    # is_palindrom("")
    print(is_palindrom_sentence("Was it a car or a cat I saw"))
    print(palindrom_product(100))
    print(get_dec_hex_palindrom(400))


if __name__ == "__main__":
    main()
