import xml.etree.ElementTree as ET
import os
from os import getcwd
from os.path import join
import glob

sets = ['train', 'val']  # 分别保存训练集和测试集的文件夹名称

# 需要修改的地方1
# 将里面的内容换成自己的标签
classes = [ "asiatic_rice_borer", "rice_water_weevil","rice_leaf_roller", "rice_gall_midge", "brown_plant_hopper", "rice_leaf_hopper","small_brown_plant_hopper", "yellow_rice_borer", "paddy_stem_maggot","rice_leaf_caterpillar"]  # 标注时的标签

'''
xml中框的左上角坐标和右下角坐标(x1,y1,x2,y2)
》》txt中的中心点坐标和宽和高(x,y,w,h)，并且归一化
'''


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(data_dir, imageset, image_id):
    in_file = open(data_dir + '/%s_annotations/%s.xml' % (imageset, image_id))  # 读取xml
    out_file = open(data_dir + '/%s_labels/%s.txt' % (imageset, image_id), 'w')  # 保存txt

    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)  # 获取类别索引
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str('%.6f' % a) for a in bb]) + '\n')


wd = getcwd()
print(wd)  # 当前路径

# 需要修改的地方2
# 复制文件夹的相对路径到这里来
data_dir = 'data/train'


for image_set in sets:
    image_ids = []
    for x in glob.glob(data_dir + '/%s_annotations' % image_set + '/*.xml'):
        print(x)
        image_ids.append(os.path.basename(x)[:-4])
    print('\n%s数量:' % image_set, len(image_ids))  # 确认数量
    i = 0
    for image_id in image_ids:
        i = i + 1
        convert_annotation(data_dir, image_set, image_id)
        print("%s 数据:%s/%s文件完成！" % (image_set, i, len(image_ids)))

print("Done!!!")

