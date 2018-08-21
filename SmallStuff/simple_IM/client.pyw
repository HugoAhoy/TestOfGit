from tkinter import *
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
        self.LoadButton = Button(self, text='Load', command = send_Loading_msg)
        self.LoadButton.pack()

    def send_Loading_msg(self):
        if (self.PWDEntry.get() == '' or self.AccountEntry.get() == ''):
            pass
        else:
            content = b'acc:' + self.AccountEntry.get() + 'pwd:' + self.PWDEntry.get()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('127.0.0.1',6666))
            s.send(content)


app = Application('200x150')
app.title('IM_Client')
app.mainloop()