from PIL import Image
import os
from itertools import product

def resizeimg():
    image = Image.open(rf"screenshots/{screenshot}")
    image = image.resize((398, 398))
    out = os.path.join(output_dir, f"{name}.png")
    image.save(out)
    print("Resized original image")

def create_folder():
    os.mkdir(output_dir)
    
def tile(filename, dir_out, d=98):
    img = Image.open(filename)
    w, h = img.size
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    count = 16
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{count}.gif')
        count -= 1
        img.crop(box).save(out)
        print("Tiles created")

def remove_extra():
    for file in os.listdir(output_dir):
        if file == "0.gif" or file == "1.gif":
            os.remove(os.path.join(output_dir, file))
            print("Removed extra tiles")
            
def add_blank():
    for file in os.listdir("assets/img/mario"):
        if file == "blank.gif":
            file_loc = os.path.join("assets/img/mario", file)
            new_loc = os.path.join(output_dir, file)
            os.popen(f'cp {file_loc} {new_loc}') 
            print("Added Blank tile")

def create_thumbnail():
    image = Image.open(rf"{f}")
    image = image.resize((98, 98))
    out = os.path.join(output_dir, f"{name}_thumbnail.gif")
    image.save(out)
    os.remove(f)
    print("Created Thumbnail")
    
def create_puz_file():
    
            
    with open(puz_loc, 'w') as file:
        print("Creating Puz file")
        file.write(f"name: {name}\n")
        file.write(f"number: {size}\n")
        file.write("size: 98\n")
        file.write(f"thumbnail: assets/img/{name}/{name}_thumbnail.gif\n")
        
        x = [i for i in range(17)]
        x.reverse()
        
        c = 1    
        for i in x:
            if c == 16:
                file.write(f"{c}: {output_dir}/blank.gif\n")
                break
            file.write(f"{c}: {output_dir}/{i}.gif\n")
            c += 1
            
            
    print("Puz File Created")

def delete_screenshot():
    os.remove(f"screenshots/{screenshot}")

def start():
    create_folder()      
    resizeimg()
    tile(f, output_dir)
    remove_extra()
    add_blank()
    create_thumbnail()
    create_puz_file()
    delete_screenshot()
        
for screenshot in os.listdir("screenshots"):
    name = screenshot[:-4]
    output_dir = f"assets/img/{name}"
    f = output_dir + f"/{name}.png"
    puz_loc = f"assets/{name}.puz"
    size = 16
    start()
        