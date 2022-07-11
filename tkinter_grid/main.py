from tkinter import *

def newLabelWithContent(root, name):
    frame = Frame(root)
    frame.grid_columnconfigure(tuple(range(18)), weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.pack(fill="both", side = TOP)
    
    Label(frame, text=name, borderwidth=2, relief="groove", width=10).grid(column=0, row=0, sticky="news", columnspan=6)
    Label(frame, text="Actual", borderwidth=2, relief="groove").grid(column=6, row=0, sticky="news", columnspan=6)
    Label(frame, text="Unit", borderwidth=2, relief="groove").grid(column=10, row=0, sticky="news", columnspan=1)
    Label(frame, text="Type", borderwidth=2, relief="groove").grid(column=11, row=0, sticky="news", columnspan=1)
    Label(frame, text="Set Value", borderwidth=2, relief="groove").grid(column=12, row=0, sticky="news", columnspan=4)
    Label(frame, text="Set-/Action-Button", borderwidth=2, relief="groove").grid(column=16, row=0, sticky="news", columnspan=2)
   
    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=2)

root = Tk()
root.title("BaseTopic")
root.geometry("500x200")

newLabelWithContent(root, "First Element")
newLabelWithContent(root, "Second Elemnt")
newLabelWithContent(root, "Short")
newLabelWithContent(root, "Looooooooooooooooooooong")

root.mainloop()