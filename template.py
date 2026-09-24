# STRG+ALT+Umschlat+L+
"""
Modul-Dokumentation -- Ähnlich zu JavaDoc.
Wird angezeigt z.B. mit help(__name__)
Dieses Modul beinhaltet Funktionen zur Berechnung der Fläche und der
Diagonale eines Rechtecks.
"""


# Metadaten zu dieser Datei:
__author__ = "Michael Czizek"
__example__ = "SEW4/01/B" #Gegenstand/Übungsblatt/Aufgabe
__date__ = "01.09.2026"
__version__ = "1.2.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest


def main() -> None:
    """
    Hauptfunktion des Programms.
    Fragt den Benutzer nach Breite und Höhe und gibt Fläche und Diagonale aus.
    Führt außerdem die Doctests aus.
    """
    doctest.testmod()


if __name__=="__main__":
    main()