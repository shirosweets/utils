import os

from PIL import Image  # python3 -m pip install Pillow

downloadFolder = ""  # Insert your download folder

if __name__ == "__main__":
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splittext(downloadFolder + filename)

        if (extension in [".jpng", ".jpeg", ".png"]):
            picture = Image.open(downloadFolder + filename)
            picture.save(downloadFolder + "compressed_" + filename, optimize=True, quality=60)
