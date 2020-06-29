import numpy as np
import pyautogui
import imutils
import pytesseract
import cv2
import time
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while(1):
    image = pyautogui.screenshot(region=(142,925, 100, 20))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    kernel = np.ones((2, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    out_below = pytesseract.image_to_string(image, config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789-+*/')
    print(out_below)
    try:
        exec('a = {0}'.format(out_below))
        print(a)
        pyautogui.typewrite('t')
        pyautogui.typewrite(str(a) + '\n')

    except:
        print("err")

    time.sleep(1)