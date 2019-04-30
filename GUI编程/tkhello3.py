#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/20 16:43
# @Author   : 洪松
# @File     : tkhello3.py

import tkinter

top = tkinter.Tk()

hello = tkinter.Label(top, text='Hello World!')
hello.pack()

quit = tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack()

tkinter.mainloop()