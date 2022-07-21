from os import listdir
from os.path import isfile, join
import subprocess

PATH = './assets/roman-graphique'
folders = [f for f in listdir(PATH) if not isfile(join(PATH, f))]

for folder in folders[0:1]:
    folder_path = join(PATH, folder)
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and '.png' in f]
    for file in files:
        file_path = join(folder_path, file)
        subprocess.run(["convert", file_path, "-quality", "85", file_path.replace('.png', '.webp')])
