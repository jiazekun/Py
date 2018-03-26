import os

from pillow import Image

import pytesseract

import webbrowser

def get_image(): #获得截屏

    os.system(&#39;adb shell screencap -p /sdcard/image.png&#39;) 
    

    os.system(&#39;adb pull 
    /sdcard/image.png .&#39;)

xigua_size = (150,530,1800,800) #百万英雄的题干位置，其它的可以任意修改

while True:

    if raw_input("please input ."+&#39;\n&#39;) == &#39;.&#39;: #触发条件

        get_image()

img=Image.open(&#39;image.png&#39;)

img_que = img.crop(xigua_size)

question=pytesseract.image_to_string(img_que,lang=&#39;chi_sim&#39;)#识别文字

question=question.replace(&#39; &#39;,&#39;&#39;).replace(&#39;\n&#39;,&#39;&#39;)

que = question[question.find(&#39;.&#39;)+1: question.find(&#39;?&#39;)]#选取题干的切片

url = "https://www.baidu.com/s?wd=" +que

webbrowser.open(url)
