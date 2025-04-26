import customtkinter as ctk
from PIL import Image
from CTkScrollableDropdown import *
from Arya import AryaBookI, AryaBookII
from Bran import BranBookI, BranBookII
from Catelyn import CatelynBookI, CatelynBookII
from Eddard import EddardBookI
from Jon import JonBookI, JonBookII
from Book_Info import BookInfo_BookI, BookInfo_BookII
from Sansa import SansaBookI, SansaBookII
from Tyrion import TyrionBookI, TyrionBookI
from Daenerys import DaenerysBookI, DaenerysBookI
from Davos import DavosBookII
from Theon import TheonBookII

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
        
                # Add entry with autocomplete
        entry = ctk.CTkEntry(self, width=340)
        entry.pack(fill="x", padx=20, pady=20)
        entry.place(x=100, y=250)

        def insert_method(e):   
            entry.delete(0, 'end')
            entry.insert(0, e)
            
            if e == "Eddard":
                self.controller.show_frame(EddardBookI)
            elif e == "Catelyn":
                self.controller.show_frame(CatelynBookI)
            elif e == "Tyrion":
                self.controller.show_frame(TyrionBookI)
            elif e == "Jon":
                self.controller.show_frame(JonBookI)
            elif e == "Daenerys":
                self.controller.show_frame(DaenerysBookI)
            elif e == "Arya":
                self.controller.show_frame(AryaBookI)
            elif e == "Sansa":
                self.controller.show_frame(SansaBookI)
            elif e == "Bran":
                self.controller.show_frame(BranBookI)

        values = ["Eddard", "Catelyn", "Tyrion", "Jon", "Daenerys", "Arya", "Sansa", "Bran"]
        CTkScrollableDropdown(entry, values=values, command=lambda e: insert_method(e),autocomplete=True, width=340,)

        
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

        button_back = ctk.CTkButton(self, text="Back", 
            command=lambda: self.controller.show_frame(BookInfo_BookI),fg_color="transparent", bg_color="transparent",
            width=80, height=30, corner_radius=8)
        button_back.place(x=20, y=30)       

## book2

class POVCharactersBookII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.image_label = ctk.CTkLabel(self, bg_color="light blue")
        self.image_label.place(x=210, y=20)

        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_of_Kings.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))
        self.image_label.configure(image=photo)
        self.image_label.image = photo

        self.create_entry()
        self.create_buttons()

    def create_entry(self):
        entry = ctk.CTkEntry(self, width=340)
        entry.place(x=100, y=250)

        def insert_method(e):
            entry.delete(0, 'end')
            entry.insert(0, e)

            if e == "Davos":
                self.controller.show_frame(DavosBookII)
            elif e == "Theon":
                self.controller.show_frame(TheonBookII)
            elif e == "Arya":
                self.controller.show_frame(AryaBookII)
            elif e == "Bran":
                self.controller.show_frame(BranBookII)
            elif e == "Catelyn":
                self.controller.show_frame(CatelynBookII)
            elif e == "Sansa":
                self.controller.show_frame(SansaBookII)
            elif e == "Jon":
                self.controller.show_frame(JonBookII)
            elif e == "Daenerys":
                self.controller.show_frame(DaenerysBookII)
            elif e == "Tyrion":
                self.controller.show_frame(TyrionBookII)

        values = ["Davos", "Theon", "Arya", "Bran", "Catelyn", "Sansa", "Jon", "Daenerys", "Tyrion"]
        CTkScrollableDropdown(entry, values=values, command=lambda e: insert_method(e), autocomplete=True, width=340)

    def create_buttons(self):
        from ASOIAF_APP import MainMenuPage
        button_back = ctk.CTkButton(
            self, text="Back",
            command=lambda: self.controller.show_frame(MainMenuPage),
            width=80, height=30, corner_radius=8
        )
        button_back.place(x=20, y=30)
    
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

