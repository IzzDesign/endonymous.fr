from os import listdir
from os.path import isfile, join, getsize
import subprocess

PATH = './assets/roman-graphique'
folders = [f for f in listdir(PATH) if not isfile(join(PATH, f))]

for folder in folders:
    folder_path = join(PATH, folder)
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and '.png' in f]

    png_size = 0
    webp_size = 0
    for file in files:
        file_path = join(folder_path, file)
        webp_path = file_path.replace('.png', '.webp')

        # Below command line only works for lossless.
        # https://www.smashingmagazine.com/2018/07/converting-images-to-webp/
        # add  "-q", "100" for longer and better results
        subprocess.run(["cwebp", "-m", "6", "-z", "9", "-lossless", file_path, "-o", webp_path])

        png_size += getsize(file_path)
        webp_size += getsize(webp_path)

    print("Finished %s, png=%sKB, webp=%sKB" % (folder, png_size // 1024, webp_size // 1024))
