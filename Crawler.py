# -*- coding: utf-8 -*-
# coding: utf-8

import argparse
import calendar
import gettext
import io
import json
import logging
import math
import os
import random
import re
import sys
import time
from tkinter import constants
import xml.dom.minidom
import urllib.request
import urllib
import requests
import tkinter
import tkinter.messagebox #这个是消息框，对话框的关键

from tkinter.filedialog import (askopenfilename, 
                                    askopenfilenames, 
                                    askdirectory, 
                                    asksaveasfilename)

text = ""  
def crawl():
    urls = text.get("0.0", "end").split("\n")
    urls = filter(lambda x: x!="",urls)
    index = 0
    for url in urls:
        index += 1
        # 2、创建request请求对象
        r = requests.get(url)
        
        print(r.encoding)
        # print(r.apparent_encoding)
        # print('将对象编码转换成UTF-8编码并打印出来')
        r.encoding = 'utf-8'
        # print(r.text)
        
        # # 3、发送请求获取结果
        # response = urllib.request.urlopen(request)
        # htmldata = response.read()
        
        # # 4、设置编码方式
        # htmldata = htmldata.decode('gb18030')
        # fileOb = open(url.split("/")[-1].replace("?","")+".html",'w',encoding='utf-8')     #打开一个文件，没有就新建一个
        fileOb = open(str(index)+".xml",'w',encoding='utf-8')     #打开一个文件，没有就新建一个
        fileOb.write(r.text)
        fileOb.close()
        print("Done with ", url)
    tkinter.messagebox.showinfo("Hint","Crawl finished!")

def main():
    global text
    win = tkinter.Tk()
    win.title("Crwaler")
    win.geometry("400x400")
    label = tkinter.Label(win, text = '',anchor=constants.W)
    label.pack(side=tkinter.TOP)
    text = tkinter.Text(win, height=20, width=50)
    text.pack()
    label = tkinter.Label(win, text = '')
    label.pack(side=tkinter.TOP)
    # label.grid(column = 10, row = 16)
    # 进入消息循环
    # B = tkinter.Button(win, width=15,height=3, text ="Select Folder", command = crawl)
    # B.pack(side=tkinter.TOP)
    label = tkinter.Label(win, text = '')
    label.pack(side=tkinter.TOP)
    # B.grid(column = 10, row = 1)
    B2 = tkinter.Button(win, width=15,height=3, text ="Crawl!", command = crawl)
    B2.pack(side=tkinter.TOP)
    # B2.grid(column = 10, row = 8)
    win.mainloop()




if __name__ == '__main__':
    main()
