import sys
import tkinter as tk
from flashcard_manager import FlashcardManager
from flashcard_app import FlashcardApp

def get_topic_selection(manager):
    """Presents a CLI menu for the user to select the active topic before GUI launch."""
    topics = manager.get_available_topics()
    
    if not topics:
        print("No vocabulary topics found. Exiting.")
        sys.exit(1)
        
    # If there is only one topic, just auto-select it.
    if len(topics) == 1:
        return topics[0]

    print("=========================================")
    print("Welcome to Visual Chinese Character Learning!")
    print("=========================================")
    print("Please select a topic to study:")
    
    for i, topic_name in enumerate(topics):
        print(f"  [{i + 1}] {topic_name}")
        
    print("=========================================")
    
    while True:
        choice = input("Enter the number of the topic (or 'q' to quit): ")
        if choice.lower() == 'q':
            sys.exit(0)
            
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(topics):
                print(f"Selected: {topics[choice_idx]}\n")
                return topics[choice_idx]
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Initialize the data manager
    manager = FlashcardManager(data_file='data/vocabulary.json')
    
    # Run the interactive CLI prompt to select a topic
    selected_topic = get_topic_selection(manager)
    
    # Set the active deck to the requested topic (this automatically shuffles it)
    manager.load_topic(selected_topic)
    
    # Initialize the Tkinter application with the filtered, active set
    root = tk.Tk()
    app = FlashcardApp(root, manager)
    
    # Start the event loop
    root.mainloop()

if __name__ == "__main__":
    main()
