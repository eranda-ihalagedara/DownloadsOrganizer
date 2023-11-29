import os
import shutil


def main():
    # Take folder path as input
    base_folder = input('Enter folder path:')

    if not os.path.exists(base_folder):
        print(f'Path:"{base_folder}" does not exits')

    folders_map = {
        'Compressed': ['.7z', '.ace', '.afa', '.alz', '.apk', '.arc', '.arj', '.ark', '.b1', '.b6z', '.ba', '.bh', '.cab', '.car', '.cdx', '.cfs', '.cpt', '.dar', '.dd', '.dgc', '.dmg', '.ear', '.gca', '.genozip', '.ha', '.hki', '.ice', '.jar', '.kgb', '.lha', '.lzh', '.lzx', '.pak', '.paq6', '.paq7', '.paq8', '.partimg', '.pea', '.phar', '.pim', '.pit', '.qda', '.rar', '.rk', '.s7z', '.sda', '.sea', '.sen', '.sfx', '.shk', '.sit', '.sitx', '.sqx', '.tar', '.tbz2', '.tgz', '.tlz', '.txz', '.uc', '.uc0', '.uc2', '.uca', '.ucn', '.ue2', '.uha', '.ur2', '.war', '.wim', '.xar', '.xp3', '.yz1', '.zip', '.zipx', '.zoo', '.zpaq', '.zz'
],
        'Documents': ['.pdf', '.csv', '.doc', '.docx', '.xls', '.xlm', '.xlsx', '.xlsm', '.ppt', '.pptx', '.pps', '.pub'], 
        'Video': ['.3g2', '.3gp', '.amv', '.asf', '.avi', '.drc', '.f4a', '.f4b', '.f4v', '.flv', '.gifv', '.m2ts', '.m2v', '.m4p', '.m4v', '.mkv', '.mng', '.mov', '.mp2', '.mp4', '.mpe', '.mpeg', '.mpg', '.mpv', '.mts', '.mxf', '.nsv', '.ogg', '.ogv', '.qt', '.rm', '.rmvb', '.roq', '.svi', '.ts', '.viv', '.vob', '.webm', '.wmv', '.yuv'
], 
        'Images': ['.jpeg', '.jpg', '.png', '.webp', '.tiff', '.tif', '.bmp', '.img', '.svg', '.xps', '.gif', '.eps', '.raw'],
        'Music': ['.8svx', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.cda', '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.mmf', '.mogg', '.movpkg', '.mp3', '.mpc', '.msv', '.nmf', '.oga', '.opus', '.ra', '.raw', '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', 
], 
        'Programs': ['.exe', '.bat']}

    # Create extension map
    extension_map = {}

    for folder, extensions in folders_map.items():
        for ext in extensions:
            extension_map[ext] = folder

    # Move files based on extention
    for fname in os.listdir(base_folder):
        fpath = os.path.join(base_folder, fname)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1]
            match_folder = extension_map.get(ext)
    
            if match_folder is not None:
                target_path = os.path.join(base_folder,match_folder)
                if not os.path.exists(target_path):
                    os.mkdir(target_path)
                    
                shutil.move(os.path.join(base_folder,fname), os.path.join(target_path,fname))
                print(f'{fname} moved to {match_folder}')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)