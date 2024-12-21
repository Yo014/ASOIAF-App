import tkinter as tk
from PIL import Image, ImageTk

class MainMenuPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("600x600")
        self.root.configure(bg="light blue")
        self.create_buttons()

    def create_buttons(self):
        button_bg = "white"

        # Button to load the profile
        button_eddard = tk.Button(self.root, text="Eddard Stark", command=self.show_profile1,bg=button_bg, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuPage(root)
    root.mainloop()
    