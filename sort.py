import sys, os, shutil

pictures = ['.JPEG', '.PNG', '.JPG', '.SVG']
videos =['.AVI', '.MP4', '.MOV', '.MKV']
documents = ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
audio = ['.MP3', '.OGG', '.WAV', '.AMR']
archives = ['.ZIP', '.GZ', '.TAR']

transliteration_table = {
    "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "ZH",
    "З": "Z", "И": "I", "Й": "Y", "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O",
    "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "KH", "Ц": "TS",
    "Ч": "CH", "Ш": "SH", "Щ": "SHCH", "Ъ": "", "Ы": "Y", "Ь": "", "Э": "E", "Ю": "YU",
    "Я": "YA", "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
    "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh",
    "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", "ъ": "", "ы": "y", "ь": "", "э": "e",
    "ю": "yu", "я": "ya", "!": "_", "@": "_", "#": "_", "$": "_", "%": "_", "^": "_", "&": "_",
    "*": "_", "(": "_", ")": "_", "+": "_", "=": "_", "{": "_", "}": "_", "[": "_", "]": "_", ";": "_",
    ":": "_", ",": "_", "<": "_", ">": "_", "?": "_", "/": "_", "\\": "_", "|": "_", "№": "_", " ": "_",
}
path = sys.argv[1]


#Creating all directories with their paths
path_for_sorting = os.path.join(path,'Sorted/')
os.makedirs(path_for_sorting)
dir_path_pics = os.path.join(path_for_sorting + 'Pictures')
os.makedirs(dir_path_pics)
dir_path_vid = os.path.join(path_for_sorting + 'Video')
os.makedirs(dir_path_vid)
dir_path_docs = os.path.join(path_for_sorting + 'Documents')
os.makedirs(dir_path_docs)
dir_path_aud = os.path.join(path_for_sorting + 'Audio')
os.makedirs(dir_path_aud)
dir_path_arch = os.path.join(path_for_sorting + 'Archives')
os.makedirs(dir_path_arch)
dir_path_other = os.path.join(path_for_sorting + 'Other')
os.makedirs(dir_path_other)
      
#Function to normalize name of file
def normalize(name,format):
    english_name = ""
    for char in name:
        if char in transliteration_table:
            english_name += transliteration_table[char]
        else:
            english_name += char
    new_name = english_name + format
    return new_name
      
#Function to raname files
def renaming(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)) and item == 'Sorted/':
            continue
        elif os.path.isdir(os.path.join(path, item)):
            renaming(os.path.join(path, item))
        elif os.path.isfile(os.path.join(path, item)) and item =='.DS_Store':
            continue
        elif os.path.isfile(os.path.join(path, item)):
            name, format = os.path.splitext(item)
            if any(ord(char) > 127 for char in name):
                old_file_path = os.path.join(path, item)
                file_path = os.path.join(path, normalize(name,format))
                os.rename(old_file_path, file_path)    
            else:
                file_path = os.path.join(path, item)
    return "Renaming was done"            

#Function to sort files                
def sorting(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)) and item == 'Sorted/':
            continue
        elif os.path.isdir(os.path.join(path, item)):
            sorting(os.path.join(path, item))
        elif os.path.isfile(os.path.join(path, item)) and item =='.DS_Store':
            continue
        elif os.path.isfile(os.path.join(path, item)):
            name, format = os.path.splitext(item)   
            file_path = os.path.join(path, item)            
            if format.upper() in pictures:
                shutil.move(file_path, dir_path_pics)
            elif format.upper() in videos:
                shutil.move(file_path, dir_path_vid)
            elif format.upper() in documents:
                shutil.move(file_path, dir_path_docs)
            elif format.upper() in audio:
                shutil.move(file_path, dir_path_aud)
            elif format.upper() in archives:
                shutil.unpack_archive(file_path, dir_path_arch + '/' + name)
                os.remove(file_path)
            elif format == '.DS_Store': #Need to ignore my system dir 
                continue
            else:
                shutil.move(file_path, dir_path_other)
    return "Sorting was done"

# Function to delete empty dirs
def delete_empty_directories(path):
    
    sorted_dir = path_for_sorting
    
    for dir_name in os.listdir(path):
        dir_path = os.path.join(path, dir_name)
        
        if dir_path == sorted_dir:
            continue
        
        if os.path.isdir(dir_path):
            delete_empty_directories(dir_path)
        
        if not os.listdir(dir_path) or os.listdir(dir) == ['.DS_Store']:
            os.rmdir(dir_path)
    
#Full working script
def full_sort(path):
    renaming(path)
    sorting(path)
    delete_empty_directories(path)
    return 'Everything was done'
      
                    
print(full_sort(path))