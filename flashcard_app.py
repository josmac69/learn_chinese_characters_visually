import tkinter as tk
import json
import os
from flashcard_manager import FlashcardManager

class FlashcardApp:
    def __init__(self, root, manager: FlashcardManager):
        self.root = root
        self.manager = manager
        self.config_file = 'data/config.json'
        
        # Performance/Visual Configuration State
        self.themes = [
            ("black", "white", "gray80"),       # Default AR Standard
            ("black", "yellow", "khaki"),      # High Contrast
            ("black", "#00ff00", "#00aa00"),   # Green/Retro Display
            ("white", "black", "gray30")       # Inverted
        ]
        
        # Default configuration
        self.current_theme_idx = 0
        self.chinese_font_size = 250
        self.english_font_size = 60
        
        # Load user settings if they exist
        self.load_config()
        self.bg_color, self.chinese_color, self.english_color = self.themes[self.current_theme_idx]
        
        # Configure AR glasses optimized full-screen window
        self.root.title("Visual Chinese Learning")
        self.root.configure(bg=self.bg_color)
        
        # Hide standard window decorations (title bar, borders)
        self.root.attributes("-fullscreen", True)
        self.root.config(cursor="none") # Hide the mouse cursor

        # Key Bindings
        self.root.bind("<Escape>", self.quit_app)
        self.root.bind("<space>", self.next_card)
        self.root.bind("<Right>", self.next_card)
        self.root.bind("<Left>", self.previous_card)
        
        # Configuration Bindings
        self.root.bind("c", self.cycle_theme)
        self.root.bind("C", self.cycle_theme)
        self.root.bind("<plus>", self.increase_size)
        self.root.bind("<equal>", self.increase_size) # In case they skip shift
        self.root.bind("<minus>", self.decrease_size)

        # Setup UI
        self.setup_ui()
        self.update_display()

    def load_config(self):
        """Loads user preferences from the config file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                    # Apply loaded config, falling back to existing defaults if key is missing/invalid
                    self.current_theme_idx = config.get("theme_idx", self.current_theme_idx)
                    self.chinese_font_size = config.get("chinese_font_size", self.chinese_font_size)
                    self.english_font_size = config.get("english_font_size", self.english_font_size)
                    
                    # Prevent out-of-bounds theme index
                    self.current_theme_idx = self.current_theme_idx % len(self.themes)
            except Exception as e:
                print(f"Warning: Failed to load config. {e}")

    def save_config(self):
        """Saves current user preferences to the config file."""
        config = {
            "theme_idx": self.current_theme_idx,
            "chinese_font_size": self.chinese_font_size,
            "english_font_size": self.english_font_size
        }
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
        except Exception as e:
            print(f"Warning: Failed to save config. {e}")

    def setup_ui(self):
        # Configure a main frame to center content vertically
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Huge Chinese Character Label
        self.chinese_label = tk.Label(
            self.main_frame, 
            text="", 
            font=("Arial", self.chinese_font_size, "bold"), 
            bg=self.bg_color, 
            fg=self.chinese_color
        )
        self.chinese_label.pack(pady=(0, 50))

        # Smaller English Translation Label
        self.english_label = tk.Label(
            self.main_frame, 
            text="", 
            font=("Arial", self.english_font_size), 
            bg=self.bg_color, 
            fg=self.english_color
        )
        self.english_label.pack()

    def update_styles(self):
        """Immediately applies font and color changes to the UI."""
        self.root.configure(bg=self.bg_color)
        self.main_frame.configure(bg=self.bg_color)
        
        self.chinese_label.config(
            bg=self.bg_color, fg=self.chinese_color,
            font=("Arial", self.chinese_font_size, "bold")
        )
        self.english_label.config(
            bg=self.bg_color, fg=self.english_color,
            font=("Arial", self.english_font_size)
        )

    def cycle_theme(self, event=None):
        self.current_theme_idx = (self.current_theme_idx + 1) % len(self.themes)
        self.bg_color, self.chinese_color, self.english_color = self.themes[self.current_theme_idx]
        self.update_styles()
        self.save_config()

    def increase_size(self, event=None):
        self.chinese_font_size += 20
        self.english_font_size += 5
        self.update_styles()
        self.save_config()

    def decrease_size(self, event=None):
        if self.chinese_font_size > 50:
            self.chinese_font_size -= 20
            self.english_font_size -= 5
            self.update_styles()
            self.save_config()

    def update_display(self):
        """Updates the UI with the content of the current card."""
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
