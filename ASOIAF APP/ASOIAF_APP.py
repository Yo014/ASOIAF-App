
import customtkinter as ctk
from PIL import Image

# Disable animations and scaling
ctk.deactivate_automatic_dpi_awareness()
ctk.set_appearance_mode("dark")
ctk.set_widget_scaling(1.0)
ctk.deactivate_automatic_dpi_awareness()

class MainMenuPage(ctk.CTkFrame):
    """
    The main menu page of the application. This class creates a window with
    buttons that can be used to navigate to different parts of the application.
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.controller.geometry("555x600")
        self.controller.title("A Song of Ice and Fire App")
    
        self.create_buttons()

    def create_buttons(self):
        """
        Creates buttons dynamically for different books in the ASOIAF series.
        This method reads the button configuration from a predefined dictionary,
        loads the corresponding images, resizes them, and creates buttons with
        the specified commands and positions. The buttons are then placed on the
        root window.
        """
        from Book_Info import BookInfo_BookI, BookInfo_BookII, BookInfo_BookIII, BookInfo_BookIV, BookInfo_BookV
        from ASOIAF_APP import MainMenuPage
        self.image=[]
        button_config = {
            "A Game of Thrones": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Game_of_Thrones.png",
                "command": lambda: self.controller.show_frame(BookInfo_BookI),
                "position": (10, 50)
            }, 
            "A Clash of Kings": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_of_Kings.png",
                "command": lambda: self.controller.show_frame(BookInfo_BookII),
                "position": (200, 50)
            },
            "A Storm of Swords": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_Of_Swords.png",
                "command": lambda: self.controller.show_frame(BookInfo_BookIII),
                "position": (380, 50)
            },
            "A Feast for Crows": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Feast_for_Crows.png",
                "command": lambda: self.controller.show_frame(BookInfo_BookIV),
                "position": (100, 280)
            },
            "A Dance with Dragons": {
                "image_path": "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Dance_with_Dragons.png",
                "command": lambda: self.controller.show_frame(BookInfo_BookV),
                "position": (300, 280)
                }
        }

        # Create buttons dynamically
        for key, config in button_config.items():

            image = Image.open(config["image_path"])
            resized_image = image.resize((150, 190))  # Resize the image
            ctk_image = ctk.CTkImage(resized_image, size=(150, 190))  # Convert to CTkImage
            
            button = ctk.CTkButton(self, image=ctk_image, command=config["command"], text="",fg_color="transparent",bg_color="transparent")
            button.place(x=config["position"][0], y=config["position"][1])



