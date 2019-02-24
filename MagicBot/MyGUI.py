from tkinter import *
import quickgrab
import threading

class Application(Frame):

    def __init__(self, master, quickgrab1):
        #initialize the frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

        #on instancie le quickgrab
        self.quicky = qb
        self.quicky.isRunning = False
        self.thread = threading.Thread(target=self.quicky.startTheScript)

    def create_widgets(self):
        #create the 3 buttons
        self.button_start = Button(self, text = "Lancer le Script", command=self.start)
        self.button_start.grid()

        self.button_stop = Button(self, text = "Stoper le Script", command=self.stop)
        self.button_stop.grid()

        self.button_pos = Button(self, text = "Recup Position", command=self.pos)
        self.button_pos.grid(row=0, column=40)

        self.button_color = Button(self, text = "Recup Color", command=self.color)
        self.button_color.grid(row=1, column=40)

        self.label_pos = Label(self, text="position du pointer : ")
        self.label_pos.grid()

        self.label_color = Label(self, text="couleur du pointer : ")
        self.label_color.grid()

    def start(self):
        try:
            self.thread.start()
        except:
            print("seulement un start please")

    def stop(self):
        self.quicky.isRunning = False

    def pos(self):
        self.label_pos["text"] = "position du pointer : " + str(self.quicky.getPosIn3Secs())
        self.label_color["text"] = "couleur du pointer : " + str(self.quicky.getColorIn3Secs())

    def color(self):
        self.label_pos["text"] = "position du pointer : " + str(self.quicky.getPosIn3Secs())
        self.label_color["text"] = "couleur du pointer : " + str(self.quicky.getColorIn3Secs())



root = Tk()
root.title = "MyGUI"
root.geometry("400x200")

#on instancie le quickgrab
qb = quickgrab.quickgrab()

app = Application(root, qb)

root.mainloop()

#permet d'arreter le thread une fois la fenetre fermée
qb.isRunning = False