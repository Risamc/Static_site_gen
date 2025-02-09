import os
import shutil

def copy_dir(src, dest):
    if not os.path.exists(src):
        print(f"The dir: {src} does not exist.")
        return
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    os.mkdir(dest)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            os.mkdir(dest_path)
            print(f"Created directory: {dest_path}")
            copy_dir(src_path, dest_path)

#copy_dir("static", "public")