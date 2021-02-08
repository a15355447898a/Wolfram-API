import base64
with open("P:\\Users\\a1535\\Desktop\\zo02.jpg",'rb') as f:base64_data = base64.b64encode(f.read());s = base64_data.decode();print('%s'%s)