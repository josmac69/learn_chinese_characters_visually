import json
import random
import os

class FlashcardManager:
    def __init__(self, data_file='data/vocabulary.json'):
        self.data_file = data_file
        self.all_topics = {}
        self.active_topic = []
        self.current_index = 0
        self.load_data()

    def load_data(self):
        """Loads vocabulary dictionary from the JSON file."""
        if not os.path.exists(self.data_file):
            print(f"Warning: Data file {self.data_file} not found.")
            self.all_topics = {"Default": []}
            return

        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Handle old flat-list format gracefully if encountered
                if isinstance(data, list):
                    self.all_topics = {"Legacy Decrypt": data}
                else:
                    self.all_topics = data
        except json.JSONDecodeError:
            print(f"Error: {self.data_file} contains invalid JSON.")
            self.all_topics = {"Error": []}

    def get_available_topics(self):
        """Returns a list of all topic names available in the dataset."""
        return list(self.all_topics.keys())

    def load_topic(self, topic_name):
        """Sets the active topic and immediately shuffles the deck."""
        if topic_name in self.all_topics:
            self.active_topic = self.all_topics[topic_name].copy()
            self.shuffle_deck()
        else:
            print(f"Error: Topic '{topic_name}' not found.")
            self.active_topic = [{"chinese": "Error", "english": f"Topic {topic_name} missing"}]

    def get_current_card(self):
        """Returns the current flashcard from the active topic (Chinese + English)."""
        if not self.active_topic:
            return {"chinese": "Empty", "english": "No words in this topic"}
        return self.active_topic[self.current_index]

    def next_card(self):
        """Advances to the next card."""
        if self.active_topic:
            self.current_index = (self.current_index + 1) % len(self.active_topic)
        return self.get_current_card()

    def previous_card(self):
        """Goes back to the previous card."""
        if self.active_topic:
            self.current_index = (self.current_index - 1) % len(self.active_topic)
        return self.get_current_card()

    def shuffle_deck(self):
        """Shuffles the order of the active flashcards."""
        if self.active_topic:
            random.shuffle(self.active_topic)
            self.current_index = 0
