import json
import requests
import base64
import urllib.parse
from PIL import Image, ImageGrab
import re

APP_ID = '19166123'
API_KEY ='Nw6CPD3exncAAVZ3UF4Hfpz6'
SECRECT_KEY = 'WSAVSETPg0GOAiNyq70kRTF996XSVxix'

# 获取token
url = 'https://aip.baidubce.com/oauth/2.0/token'
body = {'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRECT_KEY
        }

req = requests.post(url=url, data=body)
token = json.loads(req.content)['access_token']

# 获取百度api识别结果
ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s'%token
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# 读取图片并进行base64加密
im = ImageGrab.grabclipboard()
im.save('P:\\Users\\a1535\\Desktop\\剪贴板OCR\\OCR实验.png')
body = base64.b64encode(open('P:\\Users\\a1535\\Desktop\\剪贴板OCR\\OCR实验.png' ,'rb').read())

# 进行urlencode
data = urllib.parse.urlencode({'image': body})

# post请求
r = requests.post(url=ocr_url, headers=headers, data=data)

# 输出请求结果
res_words = json.loads(r.content)['words_result']
sentence=""
for word in res_words:
    sentence += word['words']+"\n"
print('%s' % sentence)