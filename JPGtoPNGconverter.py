import sys
import os
from PIL import Image

# grab first and second argument
origin_folder = sys.argv[1]
destination_folder = sys.argv[2]

# check if new folder exists, if not, create
if os.path.exists(destination_folder) != True:
  os.makedirs(destination_folder)

# loop through pokedex
# convert images to png
# save to new folder

for pokemon in os.listdir(origin_folder):
  name, old_format = os.path.splitext(pokemon)
  transformed = name + ".png"

  try:
    with Image.open(os.path.join(origin_folder,pokemon)) as im:
      im.save(f"{os.path.join(destination_folder,transformed)}", "PNG")
  except:
    print(f"Conversion error on {name}")