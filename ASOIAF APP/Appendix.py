import customtkinter as ctk
from PIL import Image
from Book_Info import BookInfo_BookI
class AppendixBookI(ctk.CTkFrame):
    def __init__(self,controller, parent):
        super().__init__(parent)
        self.controller = controller
        ctk.set_appearance_mode("dark")
        
        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=230, y=10)
        
        self.text_box = ctk.CTkTextbox(self, wrap="word", width=500, height=200, state="disabled")
        self.text_box.place(x=20, y=200)

        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config = {
            "House Baratheon": {"command": self.show_house_baratheon, "position": (18, 446)},
            "House Stark": {"command": self.show_house_stark, "position": (189, 446)},
            "House Lannister": {"command": self.show_house_lannister, "position": (369, 446)},
            "House Arryn": {"command": self.show_house_arryn, "position": (18, 496)},
            "House Tully": {"command": self.show_house_tully, "position": (189, 496)},
            "House Tyrell": {"command": self.show_house_tyrell, "position": (369, 496)},
            "House Greyjoy": {"command": self.show_house_greyjoy, "position": (18, 547)},
            "House Martell": {"command": self.show_house_martell, "position": (189, 547)},
            "House Targaryen": {"command": self.show_house_targaryen, "position": (369, 547)},
        }
        button_back = ctk.CTkButton(self, text="Back", command=lambda: self.controller.show_frame(BookInfo_BookI), width=80, height=30, corner_radius=8)
        button_back.place(x=20, y=30)
        for text, config in button_config.items():
            button = ctk.CTkButton(self, text=text, command=config["command"], width=150)
            button.place(x=config["position"][0], y=config["position"][1])

    def get_house_profiles(self):
        return {
            "House Baratheon": {
                "Name": "House Baratheon",
                "House description": "The youngest of the Great Houses...",
                "House members": "KING ROBERT BARATHEON, the First of His Name...",
                "image": "house_baratheon.png"
            },
            "House Stark": {
                "Name": "House Stark",
                "House description": "The Starks trace their descent from Brandon the Builder...",
                "House members": "EDDARD STARK, Lord of Winterfell...",
                "image": "house_stark.png"
            },
            "House Lannister": {
                "Name": "House Lannister",
                "House description": "Fair-haired, tall, and handsome...",
                "House members": "TYWIN LANNISTER, Lord of Casterly Rock...",
                "image": "house_lannister.png"
            },
            "House Arryn": {
                "Name": "House Arryn",
                "House description": "The Arryns are a noble family of the Westerlands...",
                "House members": "ROBB STARK, Lord of Casterly Rock...",
                "image": "house_arryn.png"
            },
            "House Tully": {
                "Name": "House Tully",
                "House description": "The Tullys are an ancient royal house...",
                "House members": "RICKON STARK, Lord of Casterly Rock...",
                "image": "house_tully.png"
            },
            "House Tyrell": {
                "Name": "House Tyrell",
                "House description": "The Tyrells are a noble family of the Reach...",
                "House members": "ROBB STARK, Lord of Casterly Rock...",
                "image": "house_tyrell.png"
            },
            "House Greyjoy": {
                "Name": "House Greyjoy",
                "House description": "The Greyjoys are a noble family of the Iron Islands...",
                "House members": "ROBB STARK, Lord of Casterly Rock...",
                "image": "house_greyjoy.png"
            },
            "House Martell": {
                "Name": "House Martell",
                "House description": "The Martells are a noble family of the Westerlands...",
                "House members": "ROBB STARK, Lord of Casterly Rock...",
                "image": "house_martell.png"
            },
            "House Targaryen": {
                "Name": "House Targaryen",
                "House description": "The Targaryens are a noble family of the Dragonstone...",
                "House members": "ROBB STARK, Lord of Casterly Rock...",
                "image": "house_targaryen.png"    
            },
        }

    def show_house_baratheon(self): self.show_house_profile("House Baratheon")
    def show_house_stark(self): self.show_house_profile("House Stark")
    def show_house_lannister(self): self.show_house_profile("House Lannister")
    def show_house_arryn(self): self.show_house_profile("House Arryn")
    def show_house_tully(self): self.show_house_profile("House Tully")
    def show_house_tyrell(self): self.show_house_profile("House Tyrell")
    def show_house_greyjoy(self): self.show_house_profile("House Greyjoy")
    def show_house_martell(self): self.show_house_profile("House Martell")
    def show_house_targaryen(self): self.show_house_profile("House Targaryen")

    def show_house_profile(self, house_name):
        houses = self.get_house_profiles()
        house_profile = houses[house_name]
        house_text = f"House Name: {house_profile['Name']}\n" \
                     f"House Description: {house_profile['House description']}\n" \
                     f"House Members: {house_profile['House members']}"
        self.update_text_box(house_text)
        self.update_image(house_profile['image'])

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", text)
        self.text_box.configure(state="disabled")

    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/House Sigiles /{image_name}"
            image = Image.open(image_path).resize((150, 190))
            photo = ctk.CTkImage(image, size=(150, 190))
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")


        
 