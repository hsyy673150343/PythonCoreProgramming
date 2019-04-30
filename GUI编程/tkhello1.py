#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/20 16:33
# @Author   : 洪松
# @File     : tkhello1.py

'''Label控件'''

import tkinter

# 创建一个顶层窗口
top = tkinter.Tk()

label = tkinter.Label(top, text='Hello World!')

# 让Packer来管理和显示控件
label.pack()

# 调用mainloop()运行这个GUI应用
tkinter.mainloop()