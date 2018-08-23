from tkinter import *
from tkinter.messagebox import *
import socket
class Application(Tk):
    def __init__(self, size = '100x100'):
        Tk.__init__(self)
        self.geometry(size)
        self.createWidgets()

    def createWidgets(self):
        self.AccountLabel = Label(self, text='Account:')
        self.AccountLabel.pack()
        self.AccountEntry = Entry(self)
        self.AccountEntry.pack()
        self.PWDLabel = Label(self, text='Password:')
        self.PWDLabel.pack()
        self.PWDEntry = Entry(self, show = '*')
        self.PWDEntry.pack()
        self.LoadButton = Button(self, text='Load', command = self.send_Loading_msg)
        self.LoadButton.pack()

    def send_Loading_msg(self):
        if (self.PWDEntry.get() == '' or self.AccountEntry.get() == ''):
            showinfo(title="tips", message="Please fill the blank")
        else:
            content = 'acc:' + self.AccountEntry.get() + 'pwd:' + self.PWDEntry.get()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.1.102',6666))
            s.send(content.encode())


app = Application('239x125')
app.title('HUGO\'s IM')
app.mainloop()