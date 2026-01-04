import os
import time
import tkinter as tk

def update_time():
    current_time = time.localtime()
    h = current_time.tm_hour
    m = current_time.tm_min
    s = current_time.tm_sec

    clock_hour_label.config(text = f"{h:02} :")
    clock_minute_label.config(text = f"{m:02} :")
    clock_second_label.config(text = f"{s:02}" ) 

    window.after(1000, update_time)

#def button_click():

def show_entry(i):
    labels[i].grid_remove()  # Hide label (keeps grid position)
    entries[i].grid(row=1, column=i*2)  # Show entry in same spot
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
timer_frame.pack()
###########
entries = []

timer_hours_entry = tk.Entry(timer_frame, textvariable=hours_var, width=3)
entries.append(timer_hours_entry)

timer_minutes_entry = tk.Entry(timer_frame, textvariable=minutes_var, width=3)
entries.append(timer_minutes_entry)

timer_seconds_entry = tk.Entry(timer_frame, textvariable=seconds_var, width=3)
entries.append(timer_seconds_entry)

#########
labels = []

timer_hours_label = tk.Label(timer_frame,textvariable=hours_var, text = "00")
timer_hours_label.grid(row=1, column=0)
labels.append(timer_hours_label)

colon_label_1 = tk.Label(timer_frame, text = ":")
colon_label_1.grid(row=1, column=1)

timer_minutes_label = tk.Label(timer_frame, textvariable=minutes_var, text = "00")
timer_minutes_label.grid(row=1, column=2)
labels.append(timer_minutes_label)

colon_label_2 = tk.Label(timer_frame, text = ":")
colon_label_2.grid(row=1, column=3)

timer_seconds_label = tk.Label(timer_frame, textvariable=seconds_var, text = "00")
timer_seconds_label.grid(row=1, column=4)
labels.append(timer_seconds_label)



#clock 
time_frame = tk.Frame(window, relief="solid")
time_frame.pack(side = "bottom", anchor="e")

clock_hour_label = tk.Label(time_frame, text = "")
clock_hour_label.grid(row=2, column=0)

clock_minute_label = tk.Label(time_frame, text = "")
clock_minute_label.grid(row=2, column=1)

clock_second_label = tk.Label(time_frame, text = "")
clock_second_label.grid(row=2, column=2)

update_time()

for i in range(len(labels)):
    labels[i].bind("<Button-1>", lambda event, i=i: show_entry(i))
    entries[i].bind("<Return>", lambda event, i=i: show_label(i))
    entries[i].bind("<FocusOut>", lambda event, i=i: show_label(i))

window.mainloop()

