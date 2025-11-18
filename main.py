import os
import time
import tkinter as tk

def update_time():
    current_time = time.localtime()
    hour = str(current_time.tm_hour)
    minute = str(current_time.tm_min)
    second = str(current_time.tm_sec)

    hour_label.config(text = hour + " : ")
    minute_label.config(text = minute + " : ")
    second_label.config(text = second) 

    window.after(1000, update_time)

#def button_click():

def show_entry(i):
    labels[i].grid_remove()  # Hide label (keeps grid position)
    entries[i].grid(row=1, column=i)  # Show entry in same spot
    entries[i].focus()
    entries[i].select_range(0, tk.END)

def show_label(i):
    entries[i].grid_remove()  # Hide entry
    labels[i].grid()  # Show label again


window = tk.Tk()
window.title("Shutdown timer")
window.geometry("400x300")


#the header
frame1 = tk.Frame(window, relief="solid")#creating new frame on which you can create independent pack() or grid()
frame1.pack()#just places it on window
header_label = tk.Label(frame1, text="Shutdown timer",font=("Arial",16))#label on which you can write and change info
header_label.pack()

#the timer

hours_var = tk.StringVar()
hours_var.set("00")

minutes_var = tk.StringVar()
minutes_var.set("00")

seconds_var = tk.StringVar()
seconds_var.set("00")


timer_frame = tk.Frame(window, relief="solid")
timer_frame.pack(pady=10)
###########
entries = []

hours_entry = tk.Entry(timer_frame, textvariable=hours_var, width=20)
entries.append(hours_entry)

minutes_entry = tk.Entry(timer_frame, textvariable=minutes_var, width=20)
entries.append(minutes_entry)

seconds_entry = tk.Entry(timer_frame, textvariable=seconds_var, width=20)
entries.append(seconds_entry)

#########
labels = []

hours_label = tk.Label(timer_frame,textvariable=hours_var, text = "00:")
hours_label.grid(row=1, column=0)
labels.append(hours_label)

minutes_label = tk.Label(timer_frame, textvariable=minutes_var, text = "00:")
minutes_label.grid(row=1, column=1)
labels.append(minutes_label)

seconds_label = tk.Label(timer_frame, textvariable=seconds_var, text = "00")
seconds_label.grid(row=1, column=2)
labels.append(seconds_label)




button = tk.Button(timer_frame, text="Start")
button.grid(row=2, column=1)

#clock 
time_frame = tk.Frame(window, relief="solid")
time_frame.pack(anchor="e", pady=80)

hour_label = tk.Label(time_frame, text = "")
hour_label.grid(row=2, column=0)

minute_label = tk.Label(time_frame, text = "")
minute_label.grid(row=2, column=1)

second_label = tk.Label(time_frame, text = "")
second_label.grid(row=2, column=2)

update_time()

for i in range(len(labels)):
    labels[i].bind("<Button-1>", lambda event, i=i: show_entry(i))
    entries[i].bind("<Return>", lambda event, i=i: show_label(i))
    entries[i].bind("<FocusOut>", lambda event, i=i: show_label(i))

window.mainloop()

