import tkinter as tk
from tkinter import ttk
import math
from datetime import datetime, timedelta

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("400x200")
        self.root.configure(bg='black')
        self.root.resizable(True, True)  # Allow window resizing

        # Variables
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.is_running = False
        self.after_id = None

        # Create main frame
        self.main_frame = tk.Frame(root, bg='black')
        self.main_frame.pack(expand=True, fill='both')

        # Create canvas for circular progress
        self.canvas = tk.Canvas(self.main_frame, width=400, height=200,
                              bg='black', highlightthickness=0)
        self.canvas.pack(expand=True, fill='both')

        # Create buttons
        self.play_button = tk.Button(self.canvas, text="▶", command=self.toggle_timer,
                                   bg='#FFA500', fg='white', bd=0, width=2, height=1)
        self.close_button = tk.Button(self.canvas, text="×", command=self.root.destroy,
                                    bg='#444444', fg='white', bd=0, width=2, height=1)
        
        # Create time label
        self.time_label = tk.Label(self.canvas, text="00:00", fg='white', bg='black',
                                 font=('Arial', 48))
        
        # Place widgets
        self.play_button.place(x=20, y=20)
        self.close_button.place(x=70, y=20)
        self.time_label.place(relx=0.5, rely=0.5, anchor='center')

        # Bind keyboard events
        self.root.bind('<Key>', self.handle_key_press)
        self.input_buffer = ""

        self.draw_progress(1.0)

    def draw_progress(self, percentage):
        self.canvas.delete("progress")
        
        # Get current window dimensions
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # Calculate padding and arc dimensions
        padding = 20
        arc_width = width - (padding * 2)
        arc_height = height - (padding * 2)
        
        # Draw background arc (gray)
        self.canvas.create_arc(padding, padding, arc_width, arc_height,
                              start=90, extent=-360,
                              fill='#222222', tags="progress")
        
        # Draw progress arc (yellow)
        if percentage > 0:
            self.canvas.create_arc(padding, padding, arc_width, arc_height,
                                 start=90, extent=-360 * percentage,
                                 fill='#FFA500', tags="progress")

        # Update widget positions based on new dimensions
        self.play_button.place(x=padding + 10, y=padding + 10)
        self.close_button.place(x=padding + 60, y=padding + 10)
        self.time_label.place(relx=0.5, rely=0.5, anchor='center')

    def toggle_timer(self):
        if not self.is_running and self.remaining_seconds > 0:
            self.is_running = True
            self.play_button.config(text="⏸")
            self.update_timer()
        else:
            self.is_running = False
            self.play_button.config(text="▶")
            if self.after_id:
                self.root.after_cancel(self.after_id)

    def update_timer(self):
        if self.is_running and self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            minutes = self.remaining_seconds // 60
            seconds = self.remaining_seconds % 60
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
            
            progress = self.remaining_seconds / self.total_seconds if self.total_seconds > 0 else 0
            self.draw_progress(progress)
            
            self.after_id = self.root.after(1000, self.update_timer)
        elif self.remaining_seconds <= 0:
            self.is_running = False
            self.play_button.config(text="▶")
            self.time_label.config(text="00:00")
            self.draw_progress(1.0)

    def handle_key_press(self, event):
        if event.char.isdigit():
            self.input_buffer += event.char
            if len(self.input_buffer) >= 2:
                minutes = int(self.input_buffer)
                self.total_seconds = minutes * 60
                self.remaining_seconds = self.total_seconds
                minutes = self.remaining_seconds // 60
                seconds = self.remaining_seconds % 60
                self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.input_buffer = ""
                self.draw_progress(1.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()