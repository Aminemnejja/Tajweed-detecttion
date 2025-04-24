import cv2
import numpy as np
from utils import color_rule_map

def analyze_tajweed_image(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    results = {rule: 0 for rule in color_rule_map['rule_name']}

    for idx, row in color_rule_map.iterrows():
        rule = row['rule_name']
        lower = np.array(row['hsv_lower'])
        upper = np.array(row['hsv_upper'])
        mask = cv2.inRange(hsv, lower, upper)
        count = cv2.countNonZero(mask)
        occurrences = count // row['pixel_threshold']
        results[rule] = occurrences

    return results
