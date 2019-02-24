from tkinter import *
import keyboardlistener
import threading
import quickgrab

""" tutorial 2
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
"""
"""tutorial 3
one = Label(root, text="One", bg="red", fg="white")
one.pack()

two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)

three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)
"""
"""tutorial 4
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)
check_1 = Checkbutton(root, text="Keep me logged in")

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
check_1.grid(columnspan=2)
"""
"""tutorial5
def printName(event):
    print("Hello my name is Yann")

button_1 = Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()
"""
"""tutorial 7
def leftClick(event):
    print("Left")

def middleClick(event):
    print("Midlle")

def rightClick(event):
    print("Right")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()
"""
"""tutorial 8
class YannisButtons:

    def __init__(self, master):
        frame =  Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)


    def printMessage(self):
        print("Here is a message")


b = YannisButtons(root)
"""

class monApplication():
    def __init__(self, master):
        self.isStartClicked = False

        #widgets
        self.mainframe_top = Frame(master)
        self.mainframe_top.pack(side=TOP, fill=X)

        self.subframe_left = Frame(self.mainframe_top)
        self.subframe_left.pack(side=LEFT)

        self.button_start = Button(self.subframe_left, text="Start", state=NORMAL, command=self.button_start_clicked)
        self.button_stop = Button(self.subframe_left, text="Stop", state=DISABLED, command=self.button_stop_clicked)
        self.scale_timing = Scale(self.subframe_left, from_=0, to=20, orient=HORIZONTAL)
        self.button_start.pack(padx=50, pady=10)
        self.button_stop.pack(padx=50, pady=10)
        self.scale_timing.pack(padx=50, pady=10)

        self.subframe_right = Frame(self.mainframe_top)
        self.subframe_right.pack(side=RIGHT)
        self.button_record = Button(self.subframe_right, text="Record cursor information at next click",
                               command=self.button_record_clicked)
        self.button_record.pack(padx=20, pady=10)
        self.label_pos = Label(self.subframe_right)
        self.label_pos.pack(padx=20, pady=10)
        self.label_color = Label(self.subframe_right)
        self.label_color.pack(padx=20, pady=10)

        self.mainframe_bot = Frame(master)
        self.mainframe_bot.pack(side=BOTTOM, fill=X)

        self.label_status = Label(self.mainframe_bot, text="IDLE    tip: use the 'pause' key to toggle the start/stop button", bd=1, relief=SUNKEN, anchor=W)
        self.label_status.pack(fill=X)

        #le quickgrabder
        self.isThreadStarted = False
        self.quicky = quickgrab.quickgrab()
        self.quicky.isRunning = False
        self.thread_quickgrab = threading.Thread(target=self.quicky.startTheScript)
        self.thread_quickgrab.daemon = True

        #les calculs de pos
        self.isWaitingforCursorPos = False

    def button_start_clicked(self):
        self.isStartClicked = True
        self.button_stop["state"]=NORMAL
        self.button_start["state"] = DISABLED
        self.label_status["text"] = "RUNNING ...    tip: use the 'pause' key to toggle the start/stop button"

        #concerne le quickgrab
        self.quicky.timeBeforeConcede = self.scale_timing.get()
        if not self.isThreadStarted:
            try:
                self.thread_quickgrab.start()
                self.isThreadStarted = True
            except Exception as e:
                print("erreur : " + str(e))
        self.quicky.isRunning = True

    def button_stop_clicked(self):
        self.isStartClicked = False
        self.button_start["state"] = NORMAL
        self.button_stop["state"] = DISABLED
        self.label_status["text"] = "IDLE    tip: use the 'pause' key to toggle the start/stop button"

        #le quickgrabber
        self.quicky.isRunning = False

    def button_record_clicked(self):
        self.button_record["state"] = DISABLED
        self.isWaitingforCursorPos = True
        self.label_status["text"] = "Waiting to record cursor pos and color...  Use the 'space' key once your cursor is in position"

    def resolve_cursor_pos(self):
        self.label_pos["text"] = "Position : " + str(self.quicky.getPosNow())
        self.label_color["text"] = "Color : " + str(self.quicky.getColorNow())
        self.button_record["state"] = NORMAL
        self.isWaitingforCursorPos = False

#on instancie la frame
root = Tk()
root.geometry("500x250")
monAppli = monApplication(root)

#le keyboardListener
kbl = keyboardlistener.myKeyboardListener(monAppli)
keyboard_thread = threading.Thread(target=kbl.startTheListener)
keyboard_thread.daemon = True
keyboard_thread.start()

#lance le tout
root.mainloop()

