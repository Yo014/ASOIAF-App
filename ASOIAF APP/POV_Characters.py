import customtkinter as ctk
from PIL import Image
from CTkScrollableDropdown import *
from Arya import AryaBookI, AryaBookII, AryaBookIII 
from Bran import BranBookI, BranBookII, BranBookIII
from Catelyn import CatelynBookI, CatelynBookII, CatelynBookIII
from Eddard import EddardBookI
from Jon import JonBookI, JonBookII, JonBookIII
from Book_Info import BookInfo_BookI, BookInfo_BookII, BookInfo_BookIII
from Sansa import SansaBookI, SansaBookII, SansaBookIII
from Tyrion import TyrionBookI, TyrionBookII, TyrionBookIII
from Daenerys import DaenerysBookI, DaenerysBookII, DaenerysBookIII
from Davos import DavosBookII, DavosBookIII
from Jaime import JaimeBookIII
from Theon import TheonBookII
from Samwell import SamwellBookIII

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
            command=lambda: self.controller.show_frame(BookInfo_BookII),
            width=80, height=30, corner_radius=8
        )
        button_back.place(x=20, y=30)
    
class POVCharactersBookIII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.image_label = ctk.CTkLabel(self, bg_color="light blue")
        self.image_label.place(x=210, y=20)

        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_Of_Swords.png"
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

            if e == "Arya":
                self.controller.show_frame(AryaBookIII)
            elif e == "Bran":
                self.controller.show_frame(BranBookIII)
            elif e == "Catelyn":
                self.controller.show_frame(CatelynBookIII)
            elif e == "Davos":
                self.controller.show_frame(DavosBookIII)
            elif e == "Jaime":
                self.controller.show_frame(JaimeBookIII)
            elif e == "Jon":
                self.controller.show_frame(JonBookIII)
            elif e == "Sansa":
                self.controller.show_frame(SansaBookIII)
            elif e == "Samwell":
                self.controller.show_frame(SamwellBookIII)
            elif e == "Tyrion":
                self.controller.show_frame(TyrionBookIII)
            elif e == "Daenerys":
                self.controller.show_frame(DaenerysBookIII)

        values = ["Arya", "Bran", "Catelyn", "Davos", "Jaime", "Jon", "Sansa", "Samwell", "Tyrion", "Daenerys"]
        CTkScrollableDropdown(entry, values=values, command=lambda e: insert_method(e), autocomplete=True, width=340)

    def create_buttons(self):
        from ASOIAF_APP import MainMenuPage
        button_back = ctk.CTkButton(
            self, text="Back",
            command=lambda: self.controller.show_frame(BookInfo_BookIII),
            width=80, height=30, corner_radius=8
        )
        button_back.place(x=20, y=30)
