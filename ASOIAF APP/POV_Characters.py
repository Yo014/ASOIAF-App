import customtkinter as ctk
from PIL import Image


class POVCharactersBookI(ctk.CTkFrame):
    """
    This class creates a GUI for showing the point of view characters
    in the first book of the A Song of Ice and Fire series.
    """
    def __init__(self, parent,controller):

        super().__init__(parent)
        self.controller = controller
   
        # Initialize GUI components


        
        self.image_paths = [
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/eddard_stark.png",
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Arya_Stark.png",
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Bran_Stark.png",
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Catelyn_Stark.png",
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Jon_Snow.png",
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Sansa_Stark.png",
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Tyrion_Lannister.png",
            "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/Daenerys_Targaryen.png"
        ]
        self.image_index = 0
        
        self.image_label = ctk.CTkLabel(self, bg_color="light blue", text="")
        self.image_label.place(x=0, y=0)  # Adjust placement

        self.update_image()
        self.cycle_images()  # Start cycling through images

        
        # Add buttons to the interface
        self.create_buttons()
    
    def update_image(self):
        """Updates the displayed image."""
        image_path = self.image_paths[self.image_index]
        image = Image.open(image_path)
        resized_image = image.resize((555, 600))  # Resize image
        photo = ctk.CTkImage(resized_image, size=(555, 600))

        # Configure the label with the new image
        self.image_label.configure(image=photo)
        self.image_label.image = photo
    
    def cycle_images(self):
        """Cycles through images periodically."""
        # Increment index and loop back if necessary
        self.image_index = (self.image_index + 1) % len(self.image_paths)
        self.update_image()

        # Schedule the next update in 3000 milliseconds (3 seconds)
        self.after(9000, self.cycle_images)
        
    def create_buttons(self):
        """
        Creates buttons dynamically for different characters in the first book.
        """
        from Arya import AryaBookI, AryaBookII
        from Bran import BranBookI
        from Catelyn import CatelynBookI
        from Eddard import EddardBookI
        from Jon import JonBookI
        from Book_Info import BookInfo_BookI
        from Sansa import SansaBookI
        from Tyrion import TyrionBookI
        from Daenerys import DaenerysBookI
        
        button_config = {
            "Eddard": {"name": "Eddard", "command": lambda: self.controller.show_frame(EddardBookI), "position": (80, 250)},
            "Catelyn": {"name": "Catelyn", "command": lambda: self.controller.show_frame(CatelynBookI), "position": (322, 250)},
            "Tyrion": {"name": "Tyrion", "command": lambda: self.controller.show_frame(TyrionBookI), "position": (80, 337)},
            "Jon": {"name": "Jon", "command": lambda: self.controller.show_frame(JonBookI), "position": (322, 337)},
            "Daenerys": {"name": "Daenerys", "command": lambda: self.controller.show_frame(DaenerysBookI), "position": (80, 425)},
            "Arya": {"name": "Arya", "command": lambda: self.controller.show_frame(AryaBookI), "position": (322, 425)},
            "Sansa": {"name": "Sansa", "command": lambda: self.controller.show_frame(SansaBookI), "position": (80, 513)},
            "Bran": {"name": "Bran", "command": lambda: self.controller.show_frame(BranBookI), "position": (322, 513)},
        }
        button_back = ctk.CTkButton(self, fg_color="transparent", text="Back", command=lambda: self.controller.show_frame(BookInfo_BookI), width=80, height=30, corner_radius=8)
        button_back.place(x=20, y=30)       

        for key, config in button_config.items():
            button = ctk.CTkButton(
                self,
                text=config["name"],
                corner_radius=8,
                command=config["command"],
                fg_color="transparent",
                text_color="white",
                hover_color="lightgray",
                font=("Arial", 20),
                width=150,
                height=80,
            )
            button.place(x=config["position"][0], y=config["position"][1])


class POVCharactersBookII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, bg_color="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_of_Kings.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ctk.CTkImage(resized_image, size=(150, 190))
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        
        # Add buttons to the interface
        self.create_buttons()
        
    def create_buttons(self):
        from Arya import AryaBookI, AryaBookII
        from ASOIAF_APP import MainMenuPage
        # Add buttons to the interface
        button_config = {
            "Davos":{ "name": "Davos", "command": self.show_davos_Chapters, "position": (0, 250)},
            "Catelyn":{ "name": "Catelyn", "command": self.show_catelyn_Chapters, "position": (282, 250)},
            "Tyrion":{ "name": "Tyrion", "command": self.show_tyrion_Chapters, "position": (0, 337)},
            "Jon":{ "name": "Jon", "command": self.show_Characters, "position": (282, 337)},
            "Daenerys":{ "name": "Daenerys", "command": self.show_daenerys_Chapters, "position": (0, 425)},
            "Arya":{ "name": "Arya", "command": lambda: self.controller.show_frame(AryaBookII), "position": (282, 425)},
            "Sansa":{ "name": "Sansa", "command": self.show_sansa_Chapters, "position": (0, 513)},
            "Bran":{ "name": "Bran", "command": self.show_bran_Chapters, "position": (187, 513)},
            "Theon":{ "name": "Theon", "command": self.show_theon_Chapters, "position": (374, 513)},
        }
        button_back = ctk.CTkButton(self, text="Back", command=lambda: self.controller.show_frame(MainMenuPage), width=80, height=30, corner_radius=8)
        button_back.place(x=20, y=30)

        for key, config in button_config.items():
            button = ctk.CTkButton(
                self,
                text=config["name"],
                command=config["command"],
                corner_radius=8,
                fg_color="white",
                text_color="black",
                hover_color="lightgray",
                font=("Arial", 20)
            )
            button.place(x=config["position"][0], y=config["position"][1])

    def show_davos_Chapters(self):
        pass    
    def show_catelyn_Chapters(self):
        pass           
    def show_tyrion_Chapters(self):
        pass
    def show_Characters(self):
        pass
    def show_daenerys_Chapters(self):
        pass
    def show_sansa_Chapters(self):
        pass
    def show_bran_Chapters(self):
        pass
    def show_theon_Chapters(self):
        pass
    
class POVCharactersBookIII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        
        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, bg_color="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_Of_Swords.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ctk.CTkImage(resized_image, size=(150, 190))
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        
        # Add buttons to the interface
        self.create_buttons()
        
    def create_buttons(self):
        from ASOIAF_APP import MainMenuPage
        # Add buttons to the interface
        button_config = {
            "Davos":{ "name": "Davos", "command": self.show_davos_Chapters, "position": (0, 250)},
            "Catelyn":{ "name": "Catelyn", "command": self.show_catelyn_Chapters, "position": (187, 250)},
            "Jaime":{ "name": "Jaime", "command": self.show_jaime_Chapters, "position": (374, 250)},
            "Tyrion":{ "name": "Tyrion", "command": self.show_tyrion_Chapters, "position": (374, 337)},
            "Jon":{ "name": "Jon", "command": self.show_Characters, "position": (0, 337)},
            "Bran":{ "name": "Bran", "command": self.show_bran_Chapters, "position": (187, 337)},
            "Daenerys":{ "name": "Daenerys", "command": self.show_daenerys_Chapters, "position": (0, 425)},
            "Arya":{ "name": "Arya", "command": self.show_arya_Chapters, "position": (282, 425)},
            "Sansa":{ "name": "Sansa", "command": self.show_sansa_Chapters, "position": (0, 513)},
            "Samwell":{ "name": "Samwell", "command": self.show_samwell_Chapters, "position": (282, 513)},
        }
        button_back = ctk.CTkButton(self, text="Back", command=lambda: self.controller.show_frame(MainMenuPage), width=80, height=30, corner_radius=8)
        button_back.place(x=20, y=30)        

        for key, config in button_config.items():
            button = ctk.CTkButton(
                self,
                text=config["name"],
                command=config["command"],
                corner_radius=8,
                fg_color="white",
                text_color="black",
                hover_color="lightgray",
                font=("Arial", 20)
            )
            button.place(x=config["position"][0], y=config["position"][1])

    def show_davos_Chapters(self):
        pass    
    def show_catelyn_Chapters(self):
        pass           
    def show_tyrion_Chapters(self):
        pass
    def show_Characters(self):
        pass
    def show_daenerys_Chapters(self):
        pass
    def show_arya_Chapters(self):
        pass
    def show_sansa_Chapters(self):
        pass
    def show_bran_Chapters(self):
        pass
    def show_jaime_Chapters(self):
        pass
    def show_samwell_Chapters(self):
        pass

