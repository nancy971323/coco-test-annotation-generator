import json
import os
import cv2

if __name__ == '__main__':
    # modify here
    path = "./test/"
    files = [f for f in os.listdir(path)]

    images = []
    for i in range(len(files)):
        img = cv2.imread(path + files[i])
        height = img.shape[0]
        width = img.shape[1]
        tmp = {'file_name': files[i], 'height': height, 'width' : width, 'id' : i}
        images.append(tmp)

    annotation = {
        'images': images,
        # modify here
        'categories': [{'supercategory': 'cat', 'id': 1, 'name': 'cat'},
                       {'supercategory': 'dog', 'id': 2, 'name': 'dog'}]
    }

    with open('annotation.json', 'w') as fp:
        json.dump(annotation, fp)
