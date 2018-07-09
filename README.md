# Práce se soubory

Cílem tohoto cvičení je prakticky naučit základní práci se soubory.
Základní práce se soubory obnáší:

* Otevření souboru
* Načtení souboru
* Zapsání do souboru
* Projití celé složky a vylistování souborů, co mne zajímají

## Úkol 1: Načtení souboru

Velmi jednoduché cvičení.
Cílem je otevřít soubor ve složce `test_files/file_1.txt` a vypsat jeho obsah.

Výstup může vypadat třeba takto:
```
Otevřen soubor
Obsah je
6
Zavřen soubor
```

Cílem je naučit se otevírat a zavírat soubory a číst z nich.

Zdroje ze kterých čerpat:

* [Python pro začátečníky, práce se soubory](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python) je moc pěkné vysvětlení jak to celé funguje.


Výsledné zdrojové soubory odevzdat prosím do složky results, zde na git.
Odevzdává se pull requestem, který já projdu a mergnu :).

## Úkol 2: Projití složky

Druhé velmi jednoduché cvičení.
Cílem je naučit se procházet složku a postupně načítat soubory z ní.
Úkol je projít celou složku a na konci vypsat počet souborů v ní.
Soubory číst ze složky `test_files`.

Výstup může vypadat třeba takto:
```
Procházím složku
Souborů ve složce: 10
```

Odevzdává se stejně :)

## Úkol 3: Projití a zpracování složky

Třetí snadné cvičení.
Úkolem je projít složku, načíst každý soubor, obsahy všech souborů sečíst a na konci vypsat.
Cílem je procvičit si práci s proměnnými.
TIP: Bude potřeba proměnná do které se bude přičítat obsah souborů.
TIP: Soubory se načítají jako text. Pro součet je třeba přeést na číslo pomocí int()

Výstup může vypadat třeba takto:
```
Otevírám složku
Souborů ve složce: 10
Součet obsahu: 100
```

Odevzdává se stejně.

## Úkol 4: Vypsání do souboru

Čtvrté pohodové cvičení.
Úkol je stejné jako v přechozím úkolu.
Tentokrát se výsledek vypíše do souboru i na obrazovku.

Výstup může vypadat třeba:
```
Otevíám složku
Souborů ve složce: 10
Součet obsahu: 100
Zapisuji výsledek do: vysledek.txt
```

Obsah `vysledek.txt`:
```
Souborů ve složce: 10
Součet obsah: 100
```

Odevzdává se stejně.

## Úkol 5: Filtrování načítání souborů

Obtížnější cvičení.
Úkol je stejný jako v predchozím cvičení.
Rozdíl je v tom, že se budou ignorovat všechny soubory co mají příponu `.ignore`.

Výstup:
```
Otevírám složku
Souborů ve složce 20
Ignorováno: 10
Součet obsahu: 100
Zapisuji do: vysledek.txt
```

Obsah `vysledek.txt`:
```
Souborů ve složce: 20
Ignorovano: 10
Soucet obsahu: 100
```

Odevzdava se stejně.








