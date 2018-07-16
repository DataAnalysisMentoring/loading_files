# vyvolani souboru s ukolem cislo 3, ktery vypocita soucet obsahu vsech souboru

import os

task_3= "C:/Users/hpavlasova/Desktop/PyMum/loading_files/loading_files/results/Task_3_directory_content.py"

with open(os.path.expanduser(task_3)) as t3:
    exec(t3.read())

# zalozeni noveho souboru a zapsani vysledku z promenne obsah
new_file = "C:/Users/hpavlasova/Desktop/PyMum/loading_files/loading_files/results/new_file.txt"
 
file=open(new_file,"w")

lines=['Pocet souboru ve slozce test_files je: ',str(len(files)),'.\n Soucet obsahu vsech souboru ve slozce je: ',str(obsah),'.' ]
file.writelines(lines)

#otevreni souboru pro cteni a vypsani 

file=open(new_file, "r")

print('vysledek je zapsan v souboru: ',new_file)
print('obsah noveho souboru je: \n',file.read())

file.close() 
