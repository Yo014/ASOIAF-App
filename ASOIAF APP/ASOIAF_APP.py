import tkinter as tk
from PIL import Image, ImageTk


class MainMenuPage:
    """
    The main menu page of the application. This class creates a window with
    buttons that can be used to navigate to different parts of the application.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        self.create_buttons()

    def create_buttons(self):
        """
        Creates buttons dynamically for different books in the ASOIAF series.
        This method reads the button configuration from a predefined dictionary,
        loads the corresponding images, resizes them, and creates buttons with
        the specified commands and positions. The buttons are then placed on the
        root window.
        """
        button_config = {
            "A Game of Thrones": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Game_of_Thrones.png",
                "command": self.open_book_infoBookI,
                "position": (10, 50)
            }, 
            "A Clash of Kings": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_of_Kings.png",
                "command": self.open_book_infoBookII,
                "position": (200, 50)
            }
        }
        
        # Create buttons dynamically
        for key, config in button_config.items():

            image = Image.open(config["image_path"])
            resized_image = image.resize((150, 190))  # Resize the image
            photo = ImageTk.PhotoImage(resized_image)
            
            button = tk.Button(self.root, image=photo, command=config["command"], borderwidth=0)
            button.image = photo  # Keep a reference
            button.place(x=config["position"][0], y=config["position"][1])



    def open_book_infoBookI(self):
        """
        Opens the book information page when a book button is clicked.
        """
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        new_root.mainloop()
    def open_book_infoBookII(self):
        """
        Opens the book information page when a book button is clicked.
        """
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookII
        BookInfo_BookII(new_root)
        new_root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuPage(root)
    root.mainloop()
