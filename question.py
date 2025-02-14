import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk, ImageSequence

def show_large_window(message, gif_path):
    large_window = Toplevel(root)
    large_window.title("Answer")
    large_window.geometry("600x400")

    message_label = tk.Label(large_window, text=message, font=("Arial", 20), bg="pink")
    message_label.pack(pady=20)

    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

    def update(frame=0):
        label.config(image=frames[frame])
        large_window.after(100, update, (frame + 1) % len(frames))

    label = tk.Label(large_window)
    label.pack()
    update()

def on_yes():
    show_large_window("I LOVE YOU ❤️", "yes.gif")

def on_no():
    show_large_window("WRONG!", "no.gif")

root = tk.Tk()
root.title("Important Question")
root.geometry("800x600")
root.configure(bg='pink')

canvas = tk.Canvas(root, width=500, height=500, bg="pink", bd=0, highlightthickness=0)
canvas.pack()

gif = Image.open("asking.gif")
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

def update_canvas(frame=0):
    canvas.create_image(250, 250, image=frames[frame])
    root.after(100, update_canvas, (frame + 1) % len(frames))

update_canvas()

text = tk.Label(root, text="Will you be my Valentine?", font=("Arial", 20), bg="pink")
text.place(x=250, y=150)

yes_button = tk.Button(root, text="Yes!", font=("Arial", 15), cursor="hand2", padx=20, pady=15, activebackground="pink", bd=3, bg="red", command=on_yes)
yes_button.place(x=250, y=380)

no_button = tk.Button(root, text="No", font=("Arial", 15), cursor="hand2", padx=20, pady=15, activebackground="pink", bd=3, bg="red", command=on_no)
no_button.place(x=480, y=380)

root.mainloop()