import tkinter as tk
from flashcard_manager import FlashcardManager

class FlashcardApp:
    def __init__(self, root, manager: FlashcardManager):
        self.root = root
        self.manager = manager
        
        # Configure AR glasses optimized full-screen window
        self.root.title("Visual Chinese Learning")
        
        # Ensure pure black background for transparency on AR glasses
        self.bg_color = "black"
        self.fg_color = "white"
        self.root.configure(bg=self.bg_color)
        
        # Hide standard window decorations (title bar, borders)
        self.root.attributes("-fullscreen", True)
        self.root.config(cursor="none") # Hide the mouse cursor

        # Key Bindings
        self.root.bind("<Escape>", self.quit_app)
        self.root.bind("<space>", self.next_card)
        self.root.bind("<Right>", self.next_card)
        self.root.bind("<Left>", self.previous_card)

        # Setup UI
        self.setup_ui()
        self.update_display()

    def setup_ui(self):
        # Configure a main frame to center content vertically
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Huge Chinese Character Label
        # Using a very large font size (e.g. 200+) helps readability on AR
        self.chinese_label = tk.Label(
            self.main_frame, 
            text="", 
            font=("Arial", 250, "bold"), 
            bg=self.bg_color, 
            fg=self.fg_color
        )
        self.chinese_label.pack(pady=(0, 50)) # Add some padding under the char

        # Smaller English Translation Label
        self.english_label = tk.Label(
            self.main_frame, 
            text="", 
            font=("Arial", 60), 
            bg=self.bg_color, 
            fg="lightgray" # Slightly dimmer than the Chinese char to maintain hierarchy
        )
        self.english_label.pack()

    def update_display(self):
        \"\"\"Updates the UI with the content of the current card.\"\"\"
        card = self.manager.get_current_card()
        self.chinese_label.config(text=card.get("chinese", ""))
        self.english_label.config(text=card.get("english", ""))

    def next_card(self, event=None):
        self.manager.next_card()
        self.update_display()

    def previous_card(self, event=None):
        self.manager.previous_card()
        self.update_display()

    def quit_app(self, event=None):
        self.root.destroy()
