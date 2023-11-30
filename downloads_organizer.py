import os
import shutil


def main():
    
    folders_map = {
        'Compressed': ['.7z', '.ace', '.afa', '.alz', '.apk', '.arc', '.arj', '.ark', '.b1', '.b6z', '.ba', '.bh', '.cab', '.car', '.cdx', '.cfs', '.cpt', '.dar', '.dd', '.dgc', '.dmg', '.ear', '.gca', '.genozip', '.ha', '.hki', '.ice', '.jar', '.kgb', '.lha', '.lzh', '.lzx', '.pak', '.paq6', '.paq7', '.paq8', '.partimg', '.pea', '.phar', '.pim', '.pit', '.qda', '.rar', '.rk', '.s7z', '.sda', '.sea', '.sen', '.sfx', '.shk', '.sit', '.sitx', '.sqx', '.tar', '.tbz2', '.tgz', '.tlz', '.txz', '.uc', '.uc0', '.uc2', '.uca', '.ucn', '.ue2', '.uha', '.ur2', '.war', '.wim', '.xar', '.xp3', '.yz1', '.zip', '.zipx', '.zoo', '.zpaq', '.zz'
],
        'Documents': ['.pdf', '.csv', '.doc', '.docx', '.xls', '.xlm', '.xlsx', '.xlsm', '.ppt', '.pptx', '.pps', '.pub'], 
        'Video': ['.3g2', '.3gp', '.amv', '.asf', '.avi', '.drc', '.f4a', '.f4b', '.f4v', '.flv', '.gifv', '.m2ts', '.m2v', '.m4p', '.m4v', '.mkv', '.mng', '.mov', '.mp2', '.mp4', '.mpe', '.mpeg', '.mpg', '.mpv', '.mts', '.mxf', '.nsv', '.ogg', '.ogv', '.qt', '.rm', '.rmvb', '.roq', '.svi', '.ts', '.viv', '.vob', '.webm', '.wmv', '.yuv'
], 
        'Images': ['.jpeg', '.jpg', '.png', '.webp', '.tiff', '.tif', '.bmp', '.img', '.svg', '.xps', '.gif', '.eps', '.raw'],
        'Music': ['.8svx', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.cda', '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.mmf', '.mogg', '.movpkg', '.mp3', '.mpc', '.msv', '.nmf', '.oga', '.opus', '.ra', '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', 
], 
        'Programs': ['.exe', '.bat']}

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