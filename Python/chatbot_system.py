"""
Student: Sameer Ahadi
Course: CSC-101
Date: 12/13/2025
Description: Chatbot
"""

from __future__ import annotations

import random
import string
from typing import Dict


class Chatbot:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.memory: Dict[str, str] = {}
        self.active: bool = True

        self.responses = {
            "greetings": [
                "Hi there!",
                "Hello!",
                "Hey!",
                "Howdy!",
                "Hi!! Nice to chat with you.",
            ],
            "status": [
                "I'm doing great thanks for asking!",
                "All systems running smoothly",
                "I am feeling helpful today!",
                "Doing well! How about you?",
            ],
            "farewell": [
                "Goodbye!",
                "See you later!",
                "Bye! Come back anytime.",
                "Take care!",
            ],
            "fallback": [
                "I'm not sure how to respond to that. Try 'hi', 'how are you', 'name', 'color', 'favorite', or 'exit'.",
                "Hmm—I didn't catch that. Can you rephrase?",
                "I don't know that one yet, but I am learning! Try a different command.",
            ],
        }

    def _normalize(self, user_input: str) -> str:
        """
        Normalize user input:
        - strip surrounding whitespace
        - lowercase
        - ignore trailing punctuation (e.g., "hi!!!" -> "hi")
        """
        text = user_input.strip().lower()

        while text and text[-1] in string.punctuation:
            text = text[:-1]

        text = " ".join(text.split())
        return text

    def greet_user(self) -> None:
        print(f"{self.name}: Hello! I'm {self.name}, your chatbot.")
        user_name = input(f"{self.name}: What's your name? ").strip()

        if not user_name:
            user_name = "friend"

        self.memory["name"] = user_name
        print(f"{self.name}: Nice to meet you, {user_name}!")

    def get_response(self, user_input: str) -> str:
        """Return a response string based on the normalized user input."""
        text = self._normalize(user_input)

        if text == "exit":
            self.active = False
            return "Thanks for chatting. Goodbye!"

        greetings = {"hi", "hello", "hey", "howdy"}
        if text in greetings or text.startswith(("hi ", "hello ", "hey ", "howdy ")):
            return random.choice(self.responses["greetings"])

        if text in {"how are you", "how are you doing?", "how r u", "hru"}:
            return random.choice(self.responses["status"])

        if text in {"bye", "goodbye", "see you"}:
            return random.choice(self.responses["farewell"])

        if "name" in text:
            saved = self.memory.get("name")
            if saved:
                return f"Your name is {saved}."
            return "I don't know your name yet."

        if "color" in text:
            color = input(f"{self.name}: What's your favorite color? ").strip()
            if not color:
                return "No worries—tell me your favorite color anytime by typing 'color'."
            self.memory["favorite_color"] = color
            return f"Got it! I'll remember that your favorite color is {color}."

        if "favorite" in text:
            fav = self.memory.get("favorite_color")
            if fav:
                return f"Your favorite color is {fav}."
            return "You haven't told me your favorite color yet. Type 'color' to set it."

        return random.choice(self.responses["fallback"])

    def chat(self) -> None:
        """Run the main interactive chat loop until the user types 'exit'."""
        self.greet_user()

        while self.active:
            user_text = input("You: ")
            response = self.get_response(user_text)
            print(f"{self.name}: {response}")


def main() -> None:
    bot = Chatbot(name="Bayes")
    bot.chat()


if __name__ == "__main__":
    main()
