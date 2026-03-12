from tkinter import Label, Tk  
import time  

app = Tk()  
app.title("🕒 Digital Clock")  
app.geometry("400x100")  
app.resizable(True, True)  
app.configure(bg="black")  

clock_label = Label(app, bg="black", fg="cyan", font=("Helvetica", 20), relief='flat')  
clock_label.pack(expand=True)

def update_time():
    current_time = time.strftime("%I:%M:%S %p\n %A %d %B %y")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

update_time()  
app.mainloop()