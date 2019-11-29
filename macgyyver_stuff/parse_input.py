
import pyperclip
INPUT_PATH = 'input.txt'

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:  # can throw FileNotFoundError
        result = tuple(l.rstrip() for l in text_file.readlines())
        return result
    
    
    
raw_in = read_text_file(INPUT_PATH)
print(raw_in)


in_str = ''
for line in raw_in:
    in_str += line
print(in_str)

s_raw_in = in_str.split('"')
print(s_raw_in)


e_l = []

for elm_num, elm in enumerate(s_raw_in):
    if elm_num % 2 != 0:
        e_l.append(elm)
        
print(e_l)
    

pyperclip.copy(str(e_l))
spam = pyperclip.paste()







