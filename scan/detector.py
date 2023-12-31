# How to detect two different colors using `cv2.inRange` in Python-OpenCV?
# https://stackoverflow.com/questions/48109650/how-to-detect-two-different-colors-using-cv2-inrange-in-python-opencv

# inRange:
# https://www.tutorialspoint.com/how-to-find-the-hsv-values-of-a-color-using-opencv-python

# pick your color online
# https://imagecolorpicker.com/
############################################################

# (x,y)

import cv2
import numpy as np

def ColorDetection(img_output):

    c1_value = c2_value = c3_value = c4_value = 0
    c5_value = c6_value = c7_value = c8_value = 0
    c9_value = c10_value = c11_value = c12_value = 0
    c13_value = c14_value = c15_value = c16_value = 0

    ############################

    c1_name = "Magnesium"
    c1_data = img_output[27, 180]

    r, g, b = c1_data[2], c1_data[1], c1_data[0]
    c1_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c1_hsv = cv2.cvtColor(np.uint8([[c1_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c1_20 = cv2.inRange(c1_hsv, (3, 110, 232), (4, 112, 242))
    c1_40 = cv2.inRange(c1_hsv, (36, 40, 0), (70, 10, 255))
    c1_60 = cv2.inRange(c1_hsv, (3, 100, 100), (23, 255, 255))
    c1_80 = cv2.inRange(c1_hsv, (36, 80, 0), (70, 60, 255))
    c1_100 = cv2.inRange(c1_hsv, (36, 90, 0), (70, 70, 255))

    if c1_20[0] > 0:
        c1_value = 20
    elif c1_40[0] > 0:
        c1_value = 40
    elif c1_60[0] > 0:
        c1_value = 60
    elif c1_80[0] > 0:
        c1_value = 80
    elif c1_100[0] > 0:
        c1_value = 100

    c1_full = {c1_name:(c1_value, c1_hex)}

    ############################

    c2_name = "Zinc"
    c2_data =  img_output[27, 263]

    r, g, b = c2_data[2], c2_data[1], c2_data[0]
    c2_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c2_hsv = cv2.cvtColor(np.uint8([[c2_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c2_20 = cv2.inRange(c2_hsv, (20, 0, 0), (70, 255, 255))
    c2_40 = cv2.inRange(c2_hsv, (36, 0, 0), (80, 255, 255))
    c2_60 = cv2.inRange(c2_hsv, (36, 10, 0), (90, 60, 255))
    c2_80 = cv2.inRange(c2_hsv, (36, 0, 0), (100, 255, 255))
    c2_100 = cv2.inRange(c2_hsv, (20, 100, 100), (120, 255, 255))

    if c2_20[0] > 0:
        c2_value = 20
    elif c2_40[0] > 0:
        c2_value = 40
    elif c2_60[0] > 0:
        c2_value = 60
    elif c2_80[0] > 0:
        c2_value = 80
    elif c2_100[0] > 0:
        c2_value = 100

    c2_full = {c2_name:(c2_value, c2_hex)}

    ############################

    c3_name = "Potassium"
    c3_data =  img_output[27, 336]

    r, g, b = c3_data[2], c3_data[1], c3_data[0]
    c3_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c3_hsv = cv2.cvtColor(np.uint8([[c3_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c3_20 = cv2.inRange(c3_hsv, (3, 110, 232), (4, 112, 242))
    c3_40 = cv2.inRange(c3_hsv, (36, 0, 0), (70, 255, 255))
    c3_60 = cv2.inRange(c3_hsv, (36, 0, 0), (70, 255, 255))
    c3_80 = cv2.inRange(c3_hsv, (166, 100, 100), (186, 255, 255))
    c3_100 = cv2.inRange(c3_hsv, (36, 0, 0), (70, 255, 255))

    if c3_20[0] > 0:
        c3_value = 20
    elif c3_40[0] > 0:
        c3_value = 40
    elif c3_60[0] > 0:
        c3_value = 60
    elif c3_80[0] > 0:
        c3_value = 80
    elif c3_100[0] > 0:
        c3_value = 100

    c3_full = {c3_name:(c3_value, c3_hex)}

    ############################

    c4_name = "Iron"
    c4_data =  img_output[108, 180]

    r, g, b = c4_data[2], c4_data[1], c4_data[0]
    c4_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c4_hsv = cv2.cvtColor(np.uint8([[c4_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c4_20 = cv2.inRange(c4_hsv, (3, 110, 232), (4, 112, 242))
    c4_40 = cv2.inRange(c4_hsv, (151, 100, 100), (171, 255, 255))
    c4_60 = cv2.inRange(c4_hsv, (36, 0, 0), (70, 255, 255))
    c4_80 = cv2.inRange(c4_hsv, (36, 0, 0), (70, 255, 255))
    c4_100 = cv2.inRange(c4_hsv, (36, 0, 0), (70, 255, 255))

    if c4_20[0] > 0:
        c4_value = 20
    elif c4_40[0] > 0:
        c4_value = 40
    elif c4_60[0] > 0:
        c4_value = 60
    elif c4_80[0] > 0:
        c4_value = 80
    elif c4_100[0] > 0:
        c4_value = 100

    c4_full = {c4_name:(c4_value, c4_hex)}

    ############################

    c5_name = "Copper"
    c5_data =  img_output[108, 263]

    r, g, b = c5_data[2], c5_data[1], c5_data[0]
    c5_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c5_hsv = cv2.cvtColor(np.uint8([[c5_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c5_20 = cv2.inRange(c5_hsv, (95, 100, 100), (115, 255, 255))
    c5_40 = cv2.inRange(c5_hsv, (36, 0, 0), (70, 255, 255))
    c5_60 = cv2.inRange(c5_hsv, (36, 0, 0), (70, 255, 255))
    c5_80 = cv2.inRange(c5_hsv, (36, 0, 0), (70, 255, 255))
    c5_100 = cv2.inRange(c5_hsv, (36, 0, 0), (70, 255, 255))

    if c5_20[0] > 0:
        c5_value = 20
    elif c5_40[0] > 0:
        c5_value = 40
    elif c5_60[0] > 0:
        c5_value = 60
    elif c5_80[0] > 0:
        c5_value = 80
    elif c5_100[0] > 0:
        c5_value = 100

    c5_full = {c5_name:(c5_value, c5_hex)}

    ############################

    c6_name = "Calcium"
    c6_data =  img_output[108, 336]

    r, g, b = c6_data[2], c6_data[1], c6_data[0]
    c6_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c6_hsv = cv2.cvtColor(np.uint8([[c6_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c6_20 = cv2.inRange(c6_hsv, (3, 110, 232), (4, 112, 242))
    c6_40 = cv2.inRange(c6_hsv, (36, 10, 0), (90, 60, 255))
    c6_60 = cv2.inRange(c6_hsv, (36, 0, 0), (70, 255, 255))
    c6_80 = cv2.inRange(c6_hsv, (36, 0, 0), (70, 255, 255))
    c6_100 = cv2.inRange(c6_hsv, (3, 100, 100), (23, 255, 255))

    if c6_20[0] > 0:
        c6_value = 20
    elif c6_40[0] > 0:
        c6_value = 40
    elif c6_60[0] > 0:
        c6_value = 60
    elif c6_80[0] > 0:
        c6_value = 80
    elif c6_100[0] > 0:
        c6_value = 100

    c6_full = {c6_name:(c6_value, c6_hex)}

    ############################

    c7_name = "Sulfur"
    c7_data =  img_output[180, 27]

    r, g, b = c7_data[2], c7_data[1], c7_data[0]
    c7_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c7_hsv = cv2.cvtColor(np.uint8([[c7_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c7_20 = cv2.inRange(c7_hsv, (95, 100, 100), (140,139,133))
    c7_40 = cv2.inRange(c7_hsv, (16, 100, 100), (36, 255, 255))
    c7_60 = cv2.inRange(c7_hsv, (36, 0, 0), (70, 255, 255))
    c7_80 = cv2.inRange(c7_hsv, (36, 0, 0), (70, 255, 255))
    c7_100 = cv2.inRange(c7_hsv, (36, 0, 0), (70, 255, 255))

    if c7_20[0] > 0:
        c7_value = 20
    elif c7_40[0] > 0:
        c7_value = 40
    elif c7_60[0] > 0:
        c7_value = 60
    elif c7_80[0] > 0:
        c7_value = 80
    elif c7_100[0] > 0:
        c7_value = 100

    c7_full = {c7_name:(c7_value, c7_hex)}

    ############################

    c8_name = "Urea"
    c8_data =  img_output[180, 108]

    r, g, b = c8_data[2], c8_data[1], c8_data[0]
    c8_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c8_hsv = cv2.cvtColor(np.uint8([[c8_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c8_20 = cv2.inRange(c8_hsv, (3, 110, 232), (4, 112, 242))
    c8_40 = cv2.inRange(c8_hsv, (36, 0, 0), (70, 255, 255))
    c8_60 = cv2.inRange(c8_hsv, (95, 100, 100), (115, 255, 255))
    c8_80 = cv2.inRange(c8_hsv, (36, 0, 0), (70, 255, 255))
    c8_100 = cv2.inRange(c8_hsv, (36, 0, 0), (70, 255, 255))

    if c8_20[0] > 0:
        c8_value = 20
    elif c8_40[0] > 0:
        c8_value = 40
    elif c8_60[0] > 0:
        c8_value = 60
    elif c8_80[0] > 0:
        c8_value = 80
    elif c8_100[0] > 0:
        c8_value = 100

    c8_full = {c8_name:(c8_value, c8_hex)}

    ############################

    c9_name = "Sodium"
    c9_data =  img_output[180, 180]

    r, g, b = c9_data[2], c9_data[1], c9_data[0]
    c9_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c9_hsv = cv2.cvtColor(np.uint8([[c9_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c9_20 = cv2.inRange(c9_hsv, (166, 100, 100), (186, 255, 255))
    c9_40 = cv2.inRange(c9_hsv, (36, 0, 0), (70, 255, 255))
    c9_60 = cv2.inRange(c9_hsv, (36, 0, 0), (70, 255, 255))
    c9_80 = cv2.inRange(c9_hsv, (36, 0, 0), (70, 255, 255))
    c9_100 = cv2.inRange(c9_hsv, (36, 0, 0), (70, 255, 255))

    if c9_20[0] > 0:
        c9_value = 20
    elif c9_40[0] > 0:
        c9_value = 40
    elif c9_60[0] > 0:
        c9_value = 60
    elif c9_80[0] > 0:
        c9_value = 80
    elif c9_100[0] > 0:
        c9_value = 100

    c9_full = {c9_name:(c9_value, c9_hex)}

    ############################

    c10_name = "Phosphorus"
    c10_data =  img_output[180, 263]

    r, g, b = c10_data[2], c10_data[1], c10_data[0]
    c10_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c10_hsv = cv2.cvtColor(np.uint8([[c10_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c10_20 = cv2.inRange(c10_hsv, (3, 110, 232), (4, 112, 242))
    c10_40 = cv2.inRange(c10_hsv, (3, 100, 100), (23, 255, 255))
    c10_60 = cv2.inRange(c10_hsv, (36, 0, 0), (70, 255, 255))
    c10_80 = cv2.inRange(c10_hsv, (36, 0, 0), (70, 255, 255))
    c10_100 = cv2.inRange(c10_hsv, (36, 0, 0), (70, 255, 255))

    if c10_20[0] > 0:
        c10_value = 20
    elif c10_40[0] > 0:
        c10_value = 40
    elif c10_60[0] > 0:
        c10_value = 60
    elif c10_80[0] > 0:
        c10_value = 80
    elif c10_100[0] > 0:
        c10_value = 100

    c10_full = {c10_name:(c1_value, c10_hex)}

    ############################

    c11_name = "Clorine"
    c11_data =  img_output[180, 336]

    r, g, b = c11_data[2], c11_data[1], c11_data[0]
    c11_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c11_hsv = cv2.cvtColor(np.uint8([[c11_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c11_20 = cv2.inRange(c11_hsv, (50, 100, 100), (70, 255, 255))
    c11_40 = cv2.inRange(c11_hsv, (36, 0, 0), (70, 255, 255))
    c11_60 = cv2.inRange(c11_hsv, (36, 0, 0), (70, 255, 255))
    c11_80 = cv2.inRange(c11_hsv, (36, 0, 0), (70, 255, 255))
    c11_100 = cv2.inRange(c11_hsv, (36, 0, 0), (80, 255, 255))

    if c11_20[0] > 0:
        c11_value = 20
    elif c11_40[0] > 0:
        c11_value = 40
    elif c11_60[0] > 0:
        c11_value = 60
    elif c11_80[0] > 0:
        c11_value = 80
    elif c11_100[0] > 0:
        c11_value = 100

    c11_full = {c11_name:(c11_value, c11_hex)}

    ############################

    c12_name = "Glucose"
    c12_data =  img_output[263, 27]

    r, g, b = c12_data[2], c12_data[1], c12_data[0]
    c12_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c12_hsv = cv2.cvtColor(np.uint8([[c12_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c12_20 = cv2.inRange(c12_hsv, (3, 110, 232), (4, 112, 242))
    c12_40 = cv2.inRange(c12_hsv, (36, 0, 0), (70, 255, 255))
    c12_60 = cv2.inRange(c12_hsv, (36, 0, 0), (70, 255, 255))
    c12_80 = cv2.inRange(c12_hsv, (151, 100, 100), (171, 255, 255))
    c12_100 = cv2.inRange(c12_hsv, (36, 0, 0), (70, 255, 255))

    if c12_20[0] > 0:
        c12_value = 20
    elif c12_40[0] > 0:
        c12_value = 40
    elif c12_60[0] > 0:
        c12_value = 60
    elif c12_80[0] > 0:
        c12_value = 80
    elif c12_100[0] > 0:
        c12_value = 100

    c12_full = {c12_name:(c12_value, c12_hex)}

    ############################

    c13_name = "Lactate"
    c13_data =  img_output[263, 108]

    r, g, b = c13_data[2], c13_data[1], c13_data[0]
    c13_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c13_hsv = cv2.cvtColor(np.uint8([[c13_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c13_20 = cv2.inRange(c13_hsv, (3, 110, 232), (4, 112, 242))
    c13_40 = cv2.inRange(c13_hsv, (3, 100, 100), (23, 255, 255))
    c13_60 = cv2.inRange(c13_hsv, (36, 0, 0), (70, 255, 255))
    c13_80 = cv2.inRange(c13_hsv, (36, 0, 0), (70, 255, 255))
    c13_100 = cv2.inRange(c13_hsv, (36, 0, 0), (70, 255, 255))

    if c13_20[0] > 0:
        c13_value = 20
    elif c13_40[0] > 0:
        c13_value = 40
    elif c13_60[0] > 0:
        c13_value = 60
    elif c13_80[0] > 0:
        c13_value = 80
    elif c13_100[0] > 0:
        c13_value = 100

    c13_full = {c13_name:(c13_value, c13_hex)}

    ############################

    c14_name = "Iodine"
    c14_data =  img_output[263, 180]

    r, g, b = c14_data[2], c14_data[1], c14_data[0]
    c14_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c14_hsv = cv2.cvtColor(np.uint8([[c14_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c14_20 = cv2.inRange(c14_hsv, (3, 110, 232), (4, 112, 242))
    c14_40 = cv2.inRange(c14_hsv, (36, 0, 0), (70, 255, 255))
    c14_60 = cv2.inRange(c14_hsv, (36, 0, 0), (70, 255, 255))
    c14_80 = cv2.inRange(c14_hsv, (16, 100, 100), (36, 255, 255))
    c14_100 = cv2.inRange(c14_hsv, (36, 0, 0), (70, 255, 255))

    if c14_20[0] > 0:
        c14_value = 20
    elif c14_40[0] > 0:
        c14_value = 40
    elif c14_60[0] > 0:
        c14_value = 60
    elif c14_80[0] > 0:
        c14_value = 80
    elif c14_100[0] > 0:
        c14_value = 100

    c14_full = {c14_name:(c14_value, c14_hex)}

    ############################

    c15_name = "Ascorbic Acid"
    c15_data =  img_output[263, 263]

    r, g, b = c15_data[2], c15_data[1], c15_data[0]
    c15_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c15_hsv = cv2.cvtColor(np.uint8([[c15_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c15_20 = cv2.inRange(c15_hsv, (3, 110, 232), (4, 112, 242))
    c15_40 = cv2.inRange(c15_hsv, (36, 0, 0), (70, 255, 255))
    c15_60 = cv2.inRange(c15_hsv, (166, 100, 100), (186, 255, 255))
    c15_80 = cv2.inRange(c15_hsv, (36, 0, 0), (70, 255, 255))
    c15_100 = cv2.inRange(c15_hsv, (36, 0, 0), (70, 255, 255))

    if c15_20[0] > 0:
        c15_value = 20
    elif c15_40[0] > 0:
        c15_value = 40
    elif c15_60[0] > 0:
        c15_value = 60
    elif c15_80[0] > 0:
        c15_value = 80
    elif c15_100[0] > 0:
        c15_value = 100

    c15_full = {c15_name:(c15_value, c15_hex)}

    ############################

    c16_name = "Floride"
    c16_data = img_output[263, 336]

    r, g, b = c16_data[2], c16_data[1], c16_data[0]
    c16_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    c16_hsv = cv2.cvtColor(np.uint8([[c16_data.tolist()]]),cv2.COLOR_BGR2HSV)
    c16_20 = cv2.inRange(c16_hsv, (3, 100, 100), (23, 255, 255))
    c16_40 = cv2.inRange(c16_hsv, (36, 0, 0), (70, 255, 255))
    c16_60 = cv2.inRange(c16_hsv, (36, 0, 0), (70, 255, 255))
    c16_80 = cv2.inRange(c16_hsv, (36, 0, 0), (70, 255, 255))
    c16_100 = cv2.inRange(c16_hsv, (36, 0, 0), (70, 255, 255))

    if c16_20[0] > 0:
        c16_value = 20
    elif c16_40[0] > 0:
        c16_value = 40
    elif c16_60[0] > 0:
        c16_value = 60
    elif c16_80[0] > 0:
        c16_value = 80
    elif c16_100[0] > 0:
        c16_value = 100

    c16_full = {c16_name:(c16_value, c16_hex)}


    return c1_full, c2_full, c3_full, c4_full, c5_full, c6_full, c7_full, c8_full, c9_full, c10_full, c11_full, c12_full, c13_full, c14_full, c15_full, c16_full
