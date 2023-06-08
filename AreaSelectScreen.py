import tkinter as tk
from tkinter import messagebox


class AreaSelection:
    def __init__(self):
        self.selected_area = None
        self.drawing = False
        self.start_x, self.start_y = -1, -1
        self.end_x, self.end_y = -1, -1
        self.confirmed = False

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Area Selection")
        self.root.geometry("{0}x{1}+0+0".format(
            self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        ))

        self.root.attributes("-alpha", 0.5)

        # Create the canvas
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind the mouse events to the canvas
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.canvas.bind("<B1-Motion>", self.draw_rectangle)

        # Create confirmation buttons
        self.confirm_button = tk.Button(
            self.root, text="Confirm", command=self.confirm_selection
        )
        self.confirm_button.pack(side=tk.LEFT)

        self.cancel_button = tk.Button(
            self.root, text="Cancel", command=self.cancel_selection
        )
        self.cancel_button.pack(side=tk.LEFT)

        # Start the Tkinter event loop
        self.root.mainloop()

        # Check the confirmed flag after the main loop exits
        if not self.confirmed:
            # Clear the canvas or perform any necessary action
            print("Selected area canceled.")

    # Mouse callback functions
    def start_drawing(self, event):
        self.drawing = True
        self.start_x, self.start_y = event.x, event.y

    def stop_drawing(self, event):
        self.drawing = False
        self.end_x, self.end_y = event.x, event.y

    def draw_rectangle(self, event):
        if self.drawing:
            self.canvas.delete("rectangle")
            x, y = event.x, event.y
            self.canvas.create_rectangle(
                self.start_x, self.start_y, x, y, outline="red", tags="rectangle"
            )

    def confirm_selection(self):
        self.root.withdraw()  # Hide the root window
        response = messagebox.askquestion(
            "Confirmation", "Do you want to proceed with the selected area?"
        )
        if response == "yes":
            self.confirmed = True
            x = min(self.start_x, self.end_x)
            y = min(self.start_y, self.end_y)
            width = abs(self.end_x - self.start_x)
            height = abs(self.end_y - self.start_y)
            # Display the selected area in console
            print("Selected Area:")
            print(f"x: {x}")
            print(f"y: {y}")
            print(f"width: {width}")
            print(f"height: {height}")
            self.selected_area = (x, y, width, height)
        self.root.quit()
        self.root.update_idletasks()

    def cancel_selection(self):
        self.confirmed = False
        self.root.quit()
        self.root.update_idletasks()  # Update the window to ensure the message box is destroyed

    def get_selected_area(self):
        if self.confirmed:
            return self.selected_area
        else:
            return None
