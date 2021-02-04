import os.path

file_1 = open("trainval.txt", "w+")

for i in range(1, 11181): # 파일 수량에 맞게 변경 !!
    xml_path = 'annotations/'+'%06d' %i+'.xml'
    if os.path.isfile(xml_path):
        file_1.write('%06d' %i)
        file_1.write('\n')

file_1.close()
