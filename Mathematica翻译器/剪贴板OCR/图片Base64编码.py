#import base64
#with open("P:\\Users\\a1535\\Desktop\\zo02.jpg",'rb') as f:
#    base64_data = base64.b64encode(f.read())
#    s = base64_data.decode()
#    print('%s'%s)
import base64
from PIL import Image, ImageGrab
body = base64.b64encode(open('P:/Users/a1535/Desktop/Mathematica翻译器/剪贴板OCR/OCR实验.png' ,'rb').read())
with open("P:\\Users\\a1535\\Desktop\\Mathematica翻译器\\剪贴板OCR\\OCR实验(图片Base编码).txt",'w') as f:
 f.write(str(body, encoding="utf-8"))