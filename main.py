import tkinter as tk
from flashcard_manager import FlashcardManager
from flashcard_app import FlashcardApp

def main():
    # Initialize the data manager
    manager = FlashcardManager(data_file='data/vocabulary.json')
    
    # Shuffle the deck initially (optional but helpful for learning)
    manager.shuffle_deck()
    
    # Initialize the Tkinter application
    root = tk.Tk()
    app = FlashcardApp(root, manager)
    
    # Start the event loop
    root.mainloop()

if __name__ == "__main__":
    main()
