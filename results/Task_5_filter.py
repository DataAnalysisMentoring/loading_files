import os

# promenna files obsahuje seznam souboru ve slozce
folder = "C:/Users/hpavlasova/Desktop/PyMum/loading_files/loading_files/test_files"

files = os.listdir("C:/Users/hpavlasova/Desktop/PyMum/loading_files/loading_files/test_files") 

#nova promenna filtered_files pro neignorovane soubory
filtered_files=[]

for name in files:
	if not name.endswith('.ignore'):
		filtered_files.append(name)

obsah = 0

for file in filtered_files:
	os.chdir(folder)               # presune pozornost do pozadovane slozky
	file_1 = open(file, "r")		# otevre soubor
	obsah+=int((file_1.read()))      # pricte obsah souboru do promenne obsah
	file_1.close()                     # zavre soubor
	

print("Pocet vsech souboru ve slozce: ", len(files), "\nPocet neignorovanych souboru ve slozce: ", len(filtered_files), "\nSoucet obsahu neignorovanych souboru: ", str(obsah))

# zalozeni noveho souboru a zapsani vysledku z promenne obsah
new_file_filter = "C:/Users/hpavlasova/Desktop/PyMum/loading_files/loading_files/results/new_file_filter.txt"
 
file=open(new_file_filter,"w")

lines=["Pocet vsech souboru ve slozce: ", str(len(files)), "\n Pocet neignorovanych souboru ve slozce: ", str(len(filtered_files)), "\n Soucet obsahu neignorovanych souboru: ", str(obsah)]

file.writelines(lines)

#otevreni souboru pro cteni a vypsani 

file=open(new_file_filter, "r")

print('vysledek je zapsan v souboru: ',new_file_filter)
print('obsah noveho souboru je: \n',file.read())

file.close() 



