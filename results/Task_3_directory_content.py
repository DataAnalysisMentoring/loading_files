import os

# promenna s adresou slozky, kterou zkoumam

folder = "C:/Users/hpavlasova/Desktop/PyMum/loading_files/loading_files/test_files"

# pocet souboru ve slozce, viz predchozi ukol
files = os.listdir(folder)

print("Pocet souboru ve slozce: ", len(files))

# suma obsahu souboru ve slozce pomoci cyklu, ktery pricita do promenne obsah jednotlive obsahy v souborech

obsah = 0

for file in files:
	os.chdir(folder)               # presune pozornost do pozadovane slozky
	file_1 = open(file, "r")		# otevre soubor
	obsah+=int((file_1.read()))      # pricte obsah souboru do promenne obsah
	file_1.close()                     # zavre soubor
	
print("Soucet obsahu: ", obsah)