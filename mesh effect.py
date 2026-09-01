import turtle
import traceback

def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Mesh Effect")
    screen.setup(width=800, height=800)
    return screen

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()
    return t

def draw_mesh_effect(t):
    colors = ["red", "purple", "blue", "cyan", "green", "yellow", "orange"]
    
    for i in range(150):
        t.pencolor(colors[i % 7])
        t.circle(i, 100)
        t.left(90)
        t.forward(i)
        t.left(45)

def main():
    screen = setup_screen()
    t = setup_turtle()
    
    try:
        draw_mesh_effect(t)
        print("Drawing complete! Click anywhere on the graphics window to close it cleanly.")
    except Exception as e:
        print("\n--- ERROR CAUSING THE CRASH ---")
        traceback.print_exc()
    
    # This prevents the window from closing until you click it,
    # ensuring the background process shuts down safely.
    screen.exitonclick()

if __name__ == "__main__":
    main()