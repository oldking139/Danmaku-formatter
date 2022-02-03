import os
input_file_path = str(input())
print(input_file_path)

#删除礼物，舰长以及sc信息
with open(input_file_path,'r',encoding='utf-8') as r:
    lines=r.readlines()
with open(input_file_path,'w',encoding='utf-8') as w:
    for contents in lines:
        if '<gift ts' not in contents:
          w.write(contents)

with open(input_file_path,'r',encoding='utf-8') as r:
    lines=r.readlines()
with open(input_file_path, 'w', encoding='utf-8') as w:
    for contents in lines:
        if '<guard ts' not in contents:
          w.write(contents)

with open(input_file_path,'r',encoding='utf-8') as r:
    lines=r.readlines()
with open(input_file_path, 'w', encoding='utf-8') as w:
    for contents in lines:
        if '<sc ts' not in contents:
          w.write(contents)

#去除行首空格
with open(input_file_path,'r',encoding='utf-8') as r:
    lines=r.readlines()
with open(input_file_path, 'w', encoding='utf-8') as w:
    for contents in lines:
        contents = contents.replace('  <','<')
        contents = contents.replace('\n', '')
        w.write(contents)
