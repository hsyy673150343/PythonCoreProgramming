#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/20 16:39
# @Author   : 洪松
# @File     : tkhello2.py

'''Button控件'''

import tkinter

top = tkinter.Tk()
quit = tkinter.Button(top, text='Hello World!', command=top.quit)
quit.pack()
tkinter.mainloop()