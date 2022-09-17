import psutil
from tkinter import *
from threading import Timer
from tkinter.ttk import *
import os
import time

oldSpeed = 0
currentSpeed = 0
speed = 0
t = 1200
count = 0
timeformat = ""

root = Tk()
root.title("ShutDowner")
root.geometry("500x200")
# root.resizable(0, 0)
root.configure(bg='black')


def netSpeed():
    global oldSpeed
    global speed
    global t
    global count
    global timeformat

    Timer(1, netSpeed).start()
    newSpeed = psutil.net_io_counters(pernic=False, nowrap=True)[1]
    speed = (newSpeed - oldSpeed) / 1000000
    lblSpeed.config(text=f"{str(round(speed, 2))} Mb/s")
    oldSpeed = newSpeed

    if float(str(round(speed, 2))) < 0.3:
        count = 0
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        lblCountDown.config(text=f"Shutdown in {timeformat}")
        t -= 1
        if t <= 0:
            lblCountDown.config(text="SHUTDOWN")
            time.sleep(5)
            os.system('shutdown -s')

    elif float(str(round(speed, 2))) > 0.2:
        count += 1
        if count < 11:
            lblCountDown.config(text=f"Paused {timeformat}")

        elif count > 10:
            lblCountDown.config(text=f"Network Traffic")
            t = 1200
            nodatacount = 0


lbltext = Label(root, font=('calibri', 15, 'bold'), background="black", foreground="orange", text="Speed below 0.2Mb/s will start the countdown")
lblSpeed = Label(root, font=('calibri', 59, 'bold'), background="black", foreground="orange")
lblCountDown = Label(root, font=('calibri', 30, 'bold'), background="black", foreground="orange")

netSpeed()
# lbltext.config(text="Speed below 0.2Mb will start the countdown")
lbltext.pack()
lblSpeed.pack()
lblCountDown.pack()


mainloop()
