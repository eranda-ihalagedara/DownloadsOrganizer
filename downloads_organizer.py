import os
import shutil
import json

def main():

    # Load folders map
    script_path = os.path.dirname(__file__)
    with open(os.path.join(script_path,'folders_map.json')) as mfile:
        folders_map = json.load(mfile)

    # Create extension map
    extension_map = {}

    for folder, extensions in folders_map.items():
        for ext in extensions:

            # If extensions are duplicated
            if ext in extension_map.keys():
                print(f"'{ext}' extension is duplicated in folders map.\nPlease assign extensions exclusively to one folder")
                return
                
            extension_map[ext] = folder
            
    # Take folder path as input
    base_folder = input('Enter folder path:')

    if not os.path.exists(base_folder):
        print(f'Path:"{base_folder}" does not exits')
        
    # Move files based on extension
    duplicate_files = {}
    other_extensions = []
    for fname in os.listdir(base_folder):
        fpath = os.path.join(base_folder, fname)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1].lower()
            match_folder = extension_map.get(ext)
    
            if match_folder is not None:
                target_path = os.path.join(base_folder,match_folder)
                if not os.path.exists(target_path):
                    os.mkdir(target_path)
                    
                # If a file with same name exists in target folder
                if os.path.exists(os.path.join(target_path,fname)):
                    duplicate_files[fname] = target_path
                else:
                    shutil.move(os.path.join(base_folder,fname), os.path.join(target_path,fname))
                    print(f"File '{fname}' moved to '{match_folder}'")
            else:
                other_extensions.append(fname)

    if (len(duplicate_files)+len(other_extensions))>0:
        print('Following files were NOT moved:')
        
        for fname, target_path in duplicate_files.items():
            print(f"File name '{fname}' already exits in '{target_path}'.")

        for fname in other_extensions:
            print(f"'{fname}' file's type not assigned to any folder.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)