"""
Hangman game
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import os
import random

path = os.path.dirname(__file__)
filepath = os.path.join(path, "resources", "words.txt")
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()
allwords = text.splitlines()
words = [[], [], []]
for word in allwords:
    length = len(word)
    if length <= 4:
        words[0].append(word)
    elif length <= 8:
        words[1].append(word)
    elif length <= 14:
        words[2].append(word)


class Hangman(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=(50,50)))

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        #self.main_window.stack_trace_dialog("text", "the text in the file", str(words))
        
        self.selections = ['Easy (1-4)','Medium (5-8)','Hard (9-14)']

        self.difficulty_label = toga.Label('Choose a difficulty',style=Pack(text_align='center', padding=(50,50)))
        self.main_box.add(self.difficulty_label)

        self.difficulty_select = toga.Selection(items=self.selections)
        self.main_box.add(self.difficulty_select)

        self.difficulty_ok_button = toga.Button('Ok',on_press=self.difficulty_ok,style=Pack(text_align='center', padding=(50,50)))
        self.main_box.add(self.difficulty_ok_button)
        
        self.main_window.show()
    
    def difficulty_ok(self,widget):
        self.level = self.selections.index(self.difficulty_select.value)
        self.words=words[self.level]
        self.word = random.choice(self.words)
        self.main_box.remove(*self.main_box.children)
        self.game()
    
    def game(self):
        self.main_window.info_dialog("word", self.word)
        



def main():
    return Hangman()
