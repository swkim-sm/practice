import os.path
import shutil

# 파일명을 숫자로 변경 후 1.jpg ~ 11181.jpg 파일에 대해 사용
for i in range(1, 11181): # 이미지 수량에 맞게 변경!!!
    # 기존 경로
    img_path = 'images_before/' + '%06d' %i + '.jpg' # 자신의 이미지 경로로 변경!!!
    xml_path = 'annotations_before/' + '%06d' %i + '.xml' # 자신의 어노테이션 경로로 변경!!!
    # training dataset 
    new_img_train = 'images/train/'+'%06d' %i+'.jpg'
    new_xml_train = 'annotations/'+'%06d' %i+'.xml'
    # test dataset
    new_img_test = 'images/test/'+'%06d' %i+'.jpg'
    new_xml_test = 'annotations/'+'%06d' %i+'.xml'
    if os.path.isfile(xml_path):
        if i % 4 == 0 :
            shutil.copy(img_path, new_img_test)
            shutil.copy(xml_path, new_xml_test)
        else:
            shutil.copy(img_path, new_img_train)
            shutil.copy(xml_path, new_xml_train)
