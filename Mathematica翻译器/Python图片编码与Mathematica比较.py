import base64
import urllib.parse
from PIL import Image, ImageGrab
import re

# 读取图片并进行base64加密
body = base64.b64encode(open('P:\\Users\\a1535\\Desktop\\Mathematica翻译器\\剪贴板OCR\\OCR实验.png' ,'rb').read())

# 进行urlencode
data = urllib.parse.urlencode({'image': body})

with open("P:\\Users\\a1535\\Desktop\\Mathematica翻译器\\剪贴板OCR\\OCR实验(图片urlencode编码).txt",'w') as f:
 f.write(data)