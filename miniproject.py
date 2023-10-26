from pathlib import Path

images_folder = Path("front/images")
files = sorted(images_folder.glob("*"))
for file in files:
    print(file.name)