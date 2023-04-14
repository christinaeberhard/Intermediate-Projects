from tkinter import *
import math

# CREATING VARIABLES
pink = "#E7AB9A"
red = "#DF7857"
green = "#617143"
yellow = "#EDE9D5"
font_name = "Courier"
work_min = 25
short_break_min = 5
long_break_min = 20
reps = 0
timer = None

# TIMER RESET
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1

    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=red)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg =pink)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg =green)


# COUNTDOWN MECHANISM
def count_down(count):
    """ adjust the sec into min:sec, using the math module (floor is giving the last whole number,
    e.g. for 4.8 min, it would write 4 min """
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    """ with every count/sec, the text of timer_text should change """
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    """ after function waits the given amount of msec and then call the function,
     so the timer will count backwards every second (1000 msec), ending at 0 to not count negative """
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=yellow)

timer_label = Label(text="Timer", fg=green, bg=yellow, font=(font_name, 40))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=yellow, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(font_name, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(bg=yellow, fg=green)
check_marks.grid(column=1, row=3)

window.mainloop()