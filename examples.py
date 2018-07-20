# -*- coding: utf-8 -*-

# Ukázky toho jak funguje práce se soubory v pythonu
# Postupně ukáži jak funguje:
#   - spojování cest
#   - vypsání složek
#   - vypsání souborů
#   - procházení adresářové struktury
#   - filtrování

import glob
import os


# získání cesty pro aktuální spuštěný skript
# __file__ je systémová proměnná obsahující jméno
# aktuálního skriptu
script_dir = os.path.dirname(os.path.realpath(__file__))

# nebo můžu definovat cestu ručně podle své potřeby
manual_script_dir = 'moje rucne definova cesta kam chci'


# Tahle podmínka slouží k odlišení hlavního skriptu od ostatních
# Není nezbytná pro malé skripty, ale když už je program větší
# je dobré jí tu mít
if __name__ == '__main__':

    # spojení cesty dokupy abych dostal cestu, kterou potřebuji
    files_folder = 'test_files'
    select_folder = 'folder_1'

    work_path = os.path.join(script_dir, files_folder, select_folder)

    # získá všechny položky z adresáře
    # vrací jak soubory tak složky
    work_files = os.listdir(work_path)

    # normální cyklus pro projití nalezených souborů
    for f in work_files:
        print('Only file name')
        print(f)

        print('Full path')
        print(os.path.join(work_path, f))

        print('-----')


    work_path = os.path.join(script_dir, files_folder)
    work_item = os.listdir(work_path)

    print('=========\n')

    # položka v listdir se dá otestovat jestli je složka nebo soubor
    for item in work_item:
        if os.path.isdir(os.path.join(work_path, item)):
            items = os.listdir(os.path.join(work_path, item))
            print('Items in ', os.path.join(work_path, item), ' : ', len(items))

        if os.path.isfile(os.path.join(work_path, item)):
            print('Item is file')


    print('==========\n')

    # Pro procházení souborů se dá použít os.walk
    # je to procházení stromu souborů

    work_path = os.path.join(script_dir, files_folder)

    for root, dirs, files in os.walk(work_path):
        print('root: ', root)
        print('dirs: ', dirs)
        print('files: ', files)
        print('_________')
        for f in files:
            print('file: ', os.path.join(root, f))

        print('--------')


    print('==========\n')

    work_path = os.path.join(script_dir, files_folder)

    files = glob.glob(os.path.join(work_path, '*/*.ignore'))

    for f in files:
        # glob vrací celou cestu
        print('file: ', f)


    print('===========\n')

    work_path = os.path.join(script_dir, files_folder, select_folder)
    files = os.listdir(work_path)

    for f in files:
        # Soubory se dají otevřít buď pomocí open a zavřít pomocí close
        file_open = open(os.path.join(work_path, f), 'r')
        data = file_open.read()
        print('File content for: ', os.path.join(work_path, f), ': ', data)
        file_open.close()

        # Nebo lze použít context manager a ten se postará o zavření sám
        with open(os.path.join(work_path, f), 'r') as file_open:
            data = file_open.read()
            print('File content for: ', os.path.join(work_path, f), ': ', data)

        print('---------')


    print('===========\n')

    work_path = os.path.join(script_dir, files_folder, select_folder)
    out_file = os.path.join(work_path, 'result.txt')

    # a nakonec zápis do souboru s context managerem

    with open(out_file, 'w') as open_file:
        open_file.write('xxxx')

    with open(out_file, 'r') as open_file:
        print(open_file.read())


    print('===========\n')

    work_path = os.path.join(script_dir, files_folder)
    o_file = os.path.join(work_path, 'multiline.txt')

    # soubory se také dost často musí číst postupně po řádcích
    with open(o_file, 'r') as open_file:
        for line in open_file:
            print(line)
