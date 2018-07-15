import os, os.path, sys
files = os.listdir("C:/Users/Hesham/Desktop/git_tutorial/loading_files/test_files")

print ("Počet všech souborů ve složce: ", len(files))


obsah = 0
for file in files:
	os.chdir("C:/Users/Hesham/Desktop/git_tutorial/loading_files/test_files")
	file_1 = open(file, "r")
	obsah+=int((file_1.read()))
	file_1.close()

print("Součet ze souborů:  ", obsah) 

