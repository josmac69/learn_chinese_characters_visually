import json
import random
import os

class FlashcardManager:
    def __init__(self, data_file='data/vocabulary.json'):
        self.data_file = data_file
        self.vocabulary = []
        self.current_index = 0
        self.load_data()

    def load_data(self):
        \"\"\"Loads vocabulary from the JSON file.\"\"\"
        if not os.path.exists(self.data_file):
            print(f"Warning: Data file {self.data_file} not found. Starting with an empty dictionary.")
            self.vocabulary = []
            return

        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.vocabulary = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {self.data_file} contains invalid JSON.")
            self.vocabulary = []

    def get_current_card(self):
        \"\"\"Returns the current flashcard (Chinese + English).\"\"\"
        if not self.vocabulary:
            return {"chinese": "No Data", "english": "Please add words to vocabulary.json"}
        return self.vocabulary[self.current_index]

    def next_card(self):
        \"\"\"Advances to the next card.\"\"\"
        if self.vocabulary:
            self.current_index = (self.current_index + 1) % len(self.vocabulary)
        return self.get_current_card()

    def previous_card(self):
        \"\"\"Goes back to the previous card.\"\"\"
        if self.vocabulary:
            self.current_index = (self.current_index - 1) % len(self.vocabulary)
        return self.get_current_card()

    def shuffle_deck(self):
        \"\"\"Shuffles the order of the flashcards.\"\"\"
        random.shuffle(self.vocabulary)
        self.current_index = 0
