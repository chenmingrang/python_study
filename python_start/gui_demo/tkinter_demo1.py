"""
Python支持多种图形界面的第三方库，包括：
    TK、wxWdgets、QT、GTK
Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。
Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
"""

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        cnf = {}
        cnf["text"]='Hello world'
        cnf["background"]='red'
        # cnf["text"]='Hello world'
        # cnf["text"]='Hello world'
        # cnf["text"]='Hello world'
        self.helloLabel = tk.Label(self, cnf)
        self.helloLabel.pack()
        btn_cnf = {}
        btn_cnf["text"] = "Hello world\n(click me)"
        btn_cnf["command"] = self.say_hi
        self.hi_there = tk.Button(self, btn_cnf)
        self.hi_there.pack(side='top')

        self.QUIT = tk.Button(self, text='QUIT', fg='red', command=root.destroy)
        self.QUIT.pack(side='bottom', pady=100)

    def say_hi(self):
        print('hi there, everyone!')

root = tk.Tk()
app = Application(master=root)
app.master.minsize(700, 400)
app.mainloop()
