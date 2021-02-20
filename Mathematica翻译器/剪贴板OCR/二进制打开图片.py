import base64
from PIL import Image, ImageGrab
#body = base64.b64encode(open('P:/Users/a1535/Desktop/OCR实验.png' ,'rb').read())
body = open('P:/Users/a1535/Desktop/Mathematica翻译器/剪贴板OCR/OCR实验.png' ,'rb').read()
with open("P:\\Users\\a1535\\Desktop\\Mathematica翻译器\\剪贴板OCR\\OCR实验(图片二进制编码).txt",'w') as f:
 #f.write(str(body, encoding="utf-8"))
 f.write(str(body))