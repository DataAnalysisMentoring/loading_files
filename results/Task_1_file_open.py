
''' Cílem je otevřít soubor ve složce test_files/file_1.txt a vypsat jeho obsah'''


file_1 = open("C:/Users/hpavlasova/Desktop/PyMum/loading_files/loading_files/test_files/file_1.txt","r" )

print("Otevren soubor : test_files/file_1.txt ")

print ("Obsah je:")

print(file_1.read())   # vypise obsah souboru

file_1.close()    #zavre soubor

print("Zavren soubor : test_files/file_1.txt ")