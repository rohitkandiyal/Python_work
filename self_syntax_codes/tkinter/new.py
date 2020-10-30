import Tkinter as tk
import ttk

window=tk.Tk()
window.title("Mphasis Automation App")
window.geometry("300x350")

nb1=ttk.Notebook(window)
frame1=ttk.Frame(nb1)
frame2=ttk.Frame(nb1)
nb1.add(frame1,text="ORACLE")
nb1.add(frame2,text="SQL")
nb1.pack(expand=1, fill="both")
#tk.Label(frame1,text="\n").pack()
frame3=tk.LabelFrame(frame1,cursor="top_left_corner",text="Choose an option",padx=20,pady=20,bd=5)
frame3.pack()

frame4=tk.LabelFrame(frame2,cursor="top_left_corner",text="Choose an option",padx=20,pady=20,bd=5)
frame4.pack()

b = tk.Button(frame3, activeforeground="#000fff000", bg="lightgrey", text="Installation  ", padx=40, pady=5)
b.pack()
b1 = tk.Button(frame3, activeforeground="#000fff000", bg="lightgrey", text="DB Patching", padx=40, pady=5)
b1.pack()
tk.Button(frame3, activeforeground="#000fff000", bg="lightgrey", text="DB Creation", padx=40, pady=5).pack()

tk.Button(frame4, activeforeground="#000fff000", bg="lightgrey", text="DB Creation", padx=40, pady=5).pack(fill="both")

window.mainloop()