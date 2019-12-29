import tkinter as tk
from tkinter import filedialog,Text
import os

root = tk.Tk()
# Array to keep the selected files
apps = []

print(apps)

# read from save log to restore last session
if os.path.isfile('save.txt'):
    with open('save.txt','r') as r:
        tempApps=r.read()
        tempApps=tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]
        



# TO create a file directory pop up on clicking open file button
def addApp():

    # Each time I add new files selected they are added in the array but when diplaying in the label its repeated
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes = (("executables","*.exe"),("all files","*.*")))
    apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def delApps():
    del apps[::]
    os.remove("save.txt")

    for widget in frame.winfo_children():
        widget.destroy()

# To create a canvas and have colors/font etc.,

canvas = tk.Canvas(root, height = 600, width = 600,bg = "#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1,rely=0.1)

# add buttons

openFile = tk.Button(root,text='Open File',padx=10,pady=5,fg ="white",bg="#263D42",command=addApp)
openFile.pack()

runApps = tk.Button(root,text='Run Apps',padx=10,pady=5,fg ="white",bg="#263D42",command=runApps)
runApps.pack()

delApps = tk.Button(root,text='Delete Apps',padx=10,pady=5,fg ="white",bg="#263D42",command=delApps)
delApps.pack()


# When opening the app we are supposed to get the list of already existing apps
for app in apps:
    label=tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# But each time we close the file the workflow is lost so add in a save log

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')
