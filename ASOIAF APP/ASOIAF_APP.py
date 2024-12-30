import tkinter as tk
import customtkinter as ctk
from PIL import Image

# Disable animations and scaling
ctk.deactivate_automatic_dpi_awareness()
ctk.set_appearance_mode("dark")
ctk.set_widget_scaling(1.0)
ctk.deactivate_automatic_dpi_awareness()

class MainMenuPage:
    """
    The main menu page of the application. This class creates a window with
    buttons that can be used to navigate to different parts of the application.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        ctk.set_default_color_theme("dark-blue")
        self.root.geometry("555x600")
        ctk.deactivate_automatic_dpi_awareness()

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
            },
            "A Storm of Swords": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_Of_Swords.png",
                "command": self.open_book_infoBookIII,
                "position": (380, 50)
            },
            "A Feast for Crows": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Feast_for_Crows.png",
                "command": self.open_book_infoBookIV,
                "position": (100, 280)
            },
            "A Dance with Dragons": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Dance_with_Dragons.png",
                "command": self.open_book_infoBookV,
                "position": (300, 280)
                }
        }
        
        # Create buttons dynamically
        for key, config in button_config.items():

            image = Image.open(config["image_path"])
            resized_image = image.resize((150, 190))  # Resize the image
            ctk_image = ctk.CTkImage(resized_image, size=(150, 190))  # Convert to CTkImage
            
            button = ctk.CTkButton(self.root, image=ctk_image, command=config["command"], text="",fg_color="transparent",bg_color="transparent")
            button.place(x=config["position"][0], y=config["position"][1])

    def cancel_pending_callbacks(self):
        try:
            for widget in self.root.winfo_children():
                widget.after_cancel('all')  # Cancel animations for each widget
        except Exception as e:
            print(f"Error while canceling callbacks: {e}")

    def open_book_infoBookI(self):
        """
        Opens the book information page when a book button is clicked.
        """
        self.cancel_pending_callbacks()
        self.root.destroy()
        self.root.update()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        new_root.mainloop()

    def open_book_infoBookII(self):
        """
        Opens the book information page when a book button is clicked.
        """
        self.cancel_pending_callbacks()
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookII
        BookInfo_BookII(new_root)
        new_root.mainloop()

    def open_book_infoBookIII(self):
        """
        Opens the book information page when a book button is clicked.
        """
        self.cancel_pending_callbacks()
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookIII
        BookInfo_BookIII(new_root)
        new_root.mainloop()

    def open_book_infoBookIV(self):
        """
        Opens the book information page when a book button is clicked.
        """
        self.cancel_pending_callbacks()
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookIV
        BookInfo_BookIV(new_root)
        new_root.mainloop()

    def open_book_infoBookV(self):
        """
        Opens the book information page when a book button is clicked.
        """
        self.cancel_pending_callbacks()
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Info import BookInfo_BookV
        BookInfo_BookV(new_root)
        new_root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainMenuPage(root)
    root.mainloop()
