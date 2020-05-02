from Application import *

#init window
root = Tk()
root.title = "Naval game"
root.geometry("800x500+100+100")

#init app
app = Application(master=root)
app.mainloop()
