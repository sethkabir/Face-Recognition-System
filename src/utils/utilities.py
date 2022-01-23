import cv2
from datetime import datetime

def facial_extraction(image, bbox, padding, size=(256, 256)):
    x, y, _, _ = bbox
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x, y, w, h = round(x), round(y), round(w), round(h)

    start_y, end_y = y - padding, y + h + padding
    start_x, end_x = x - padding, x + w + padding
    if start_y < 0:
        start_y = 0
    if end_y > image.shape[0]:
        end_y = image.shape[0]
    if start_x < 0:
        start_x = 0
    if end_x > image.shape[1]:
        end_x = image.shape[1]

    ratio = image.shape[1] // image.shape[0]
    try:
        face = cv2.resize(
            image[start_y:end_y, start_x:end_x], (size[0], ratio * size[0])
        )
    except:
        face = cv2.resize(image, (size[0], ratio * size[0]))

    return face, (size[0], ratio * size[0])

def record(name):
    with open('data/records/detection_records.csv.csv','r+') as f:
        lines = f.readlines()
        records = [line.split(',')[0] for line in lines]
        if name not in records:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'n{name},{time},{date}')