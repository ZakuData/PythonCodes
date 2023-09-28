
import os, shutil


path = r"C:/Users/zakv/Downloads/"


file_name = os.listdir(path)

folder_names = ['csv files', 'images files', 'text files', 'pdf files']

for loop in range (0,4):
    if not os.path.exists(path+folder_names[loop]):
        os.makedirs(path+folder_names[loop])
        
for file in file_name:
    if ".csv" in file and not os.path.exists(path+"csv files/"+file):
        shutil.move(path + file,path + "csv files/"+file)
    elif ".png" in file and not os.path.exists(path+"images files/"+file):
        shutil.move(path + file,path + "images files/"+file)
    elif ".txt" in file and not os.path.exists(path+"text files/"+file):
        shutil.move(path + file,path + "text files/"+file)
    elif ".pdf" in file and not os.path.exists(path+"pdf files/"+file):
        shutil.move(path + file,path + "pdf files/"+file)



