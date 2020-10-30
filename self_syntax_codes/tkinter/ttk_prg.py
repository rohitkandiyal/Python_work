import Tkinter as tk
import ttk

window=tk.Tk()
window.title("Mphasis Automation App")
window.geometry("300x400")

frame1=ttk.Frame(window,borderwidth=4,padding='0.1i')
frame1.grid()

label=ttk.Label(frame1,text="Press Proceed to go on next screen")
label.grid()
button=ttk.Button(frame1,text="Proceed")
button.grid()

window.mainloop()