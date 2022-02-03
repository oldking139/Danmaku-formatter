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
def delspace(input_file_path):
    txt=open(input_file_path,'r')
    newtxt=open(input_file_path,'w')
    lines=txt.readlines()
    for line in lines:
        newline=line[2:]
        newtxt.write(newline)
    txt.close()
    newtxt.close()


#多行合一
with open(input_file_path,'r',encoding='utf-8') as r:
    lines=r.readlines()
with open(input_file_path, 'w', encoding='utf-8') as w:
    a = ''  # 空字符（中间不加空格）
    for line in lines:
        a += line.strip('\n')  # strip()是去掉每行末尾的换行符\n 1
    c = a.split()  # 将a分割成每个字符串 2
    b = ' '.join(c)  # 将c的每个字符不以任何符号直接连接 3
    # print(a)
    # print(b)
    for line in lines:
         w.write(b)

#去除每个element之间的空格
with open(input_file_path,'r',encoding='utf-8') as r:
    lines=r.readlines()
with open(input_file_path, 'w', encoding='utf-8') as w:
    for contents in lines:
        contents = contents.replace('> <','><')
        w.write(contents)