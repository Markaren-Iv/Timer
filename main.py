import os
import time
import tkinter as tk

window = tk.Tk()
window.title("Shutdown timer")
window.geometry("400x300")

frame1 = tk.Frame(window, relief="solid")#creating new frame on which you can create independent pack() or grid()
frame1.pack()
label = tk.Label(frame1, text="Shutdown timer")
label.pack()

current_time = time.localtime()
hour = str(current_time.tm_hour)
minutes = str(current_time.tm_min)
seconds = str(current_time.tm_sec)

frame2 = tk.Frame(window, relief="solid")
frame2.pack(pady=10)
hours_label = tk.Label(frame2, text = hour + " : ")
hours_label.grid(row=2, column=0, padx=0, pady=0)

minutes_label = tk.Label(frame2, text = minutes + " : ")
minutes_label.grid(row=2, column=1, padx=0, pady=0)

seconds_label = tk.Label(frame2, text = seconds)
seconds_label.grid(row=2, column=2, padx=0, pady=0)


window.mainloop()

