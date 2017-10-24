import tkinter as tk
import  tkinter.messagebox as msg_box

class Application(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWiggets()

    def createWiggets(self):
        self.input = tk.Entry(self)
        self.input.pack()

        self.alertBtn = tk.Button(self, text="Hello", command=self.say_hi)
        self.alertBtn.pack()

    def say_hi(self):
        name = self.input.get() or 'world'
        msg_box.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title("Hello world")
app.mainloop()