import tkinter as tk 

def draw(event):
    x1 = event.x - 5
    y1 = event.y - 5 
    x2 = event.x + 5
    y2 = event.y + 5
    canvas.create_oval(x1,y1,x2,y2, fill = "blue")

window = tk.Tk()
window.title("Draw")

canvas = tk.Canvas(width = 400 , height = 400 , bg = "white")
canvas.pack()
canvas.bind("<B1-Motion>",draw)

window.mainloop()
