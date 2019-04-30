#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/4/20 17:09
# @Author   : 洪松
# @File     : pfaGUI2.py

from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter import messagebox


WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter':CRIT,
    'railroad crossing':WARN,
    'wrong way':CRIT,
    'merging traffic':WARN,
    'one way': REGU
}

critCB = lambda: messagebox.showerror('Error', 'Error Button Pressed!')
warnCB = lambda: messagebox.showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: messagebox.showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit,bg='red',fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white',fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod')
ReguButton = pto(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
    eval(cmd)

top.mainloop()