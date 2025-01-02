import customtkinter as ctk
from PIL import Image
from ASOIAF_APP import MainMenuPage
from Book_Info import BookInfo_BookI

class CharacterProfileBookI(ctk.CTkFrame):
    def __init__(self,controller, parent):
        super().__init__(parent)
        """
        Initialize the Character Profile Viewer interface.

        Parameters
        ----------
        root : ctk.CTk
            The root window of the application.

        Returns
        -------
        None
        """
        self.controller = controller



        
        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="", fg_color="light blue")
        self.image_label.place(x=230, y=10)  # Adjust placement
        
        self.text_box = ctk.CTkTextbox(self, wrap="word", width=500, height=230, state="disabled")
        self.text_box.place(x=15, y=200)
        
        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config = {
            "Tyrion Lannister": {"command": self.show_profile_tyrion, "position": (18, 446)},
            "Jon Snow": {"command": self.show_profile_jon, "position": (189, 446)},
            "Eddard Stark": {"command": self.show_profile_eddard, "position": (369, 446)},
            "Daenerys Targaryen": {"command": self.show_profile_daenerys, "position": (18, 496)},
            "Catelyn Stark": {"command": self.show_profile_catelyn, "position": (189, 496)},
            "Arya Stark": {"command": self.show_profile_arya, "position": (369, 496)},
            "Sansa Stark": {"command": self.show_profile_sansa, "position": (18, 547)},
            "Bran Stark": {"command": self.show_profile_bran, "position": (279, 547)},
        }
        button_back = ctk.CTkButton(self, text="Back", command=lambda: self.controller.show_frame(BookInfo_BookI), width=80, height=30, corner_radius=8)
        button_back.place(x=20, y=30)


        for text, config in button_config.items():
            button = ctk.CTkButton(self, text=text, command=config["command"], width=120, height=40)
            button.place(x=config["position"][0], y=config["position"][1])

    def get_character_profiles(self):
        return {
            "Eddard Stark": {
                "Name": "Eddard Stark",
                "House": "Stark of Winterfell",
                "Titles": ["Lord of Winterfell", "Warden of the North", "Hand of the King"],
                "Bio": "Eddard 'Ned' Stark was the Lord of Winterfell and head of House Stark. "
                       "He was known for his honor and loyalty, which ultimately led to his tragic fate.",
                "Image": "eddard_stark.png"
            },
            "Tyrion Lannister": {
                "Name": "Tyrion Lannister",
                "House": "House Lannister of Casterly Rock",
                "Titles": ["Hand of the King", "The Imp", "Little Demon"],
                "Bio": "Tyrion 'Tywin' Lannister was the King in the North and head of House Lannister.",
                "Image": "Tyrion_lannister.png"
            },
            "Jon Snow": {
                "Name": "Jon Snow",
                "House": "House Stark of Winterfell",
                "Titles": ["Bastard of Winterfell", "Lord Snow"],
                "Bio": "Jon Snow is the bastard son of Eddard Stark.",
                "Image": "Jon_Snow.png"
            },
            "Catelyn Stark": {
                "Name": "Catelyn Stark",
                "House": "House Stark of Winterfell, House Tully",
                "Titles": ["Lady of Winterfell"],
                "Bio": "Catelyn Stark is the Lady of Winterfell.",
                "Image": "Catelyn_Stark.png"
            },
            "Arya Stark": {
                "Name": "Arya Stark",
                "House": "House Stark of Winterfell",
                "Titles": [""],
                "Bio": "Arya Stark is a fiercely independent and courageous young Stark.",
                "Image": "Arya_Stark.png"
            },
            "Sansa Stark": {
                "Name": "Sansa Stark",
                "House": "House Stark of Winterfell",
                "Titles": [""],
                "Bio": "Sansa Stark is a lady of grace and perseverance.",
                "Image": "Sansa_Stark.png"
            },
            "Daenerys Targaryen": {
                "Name": "Daenerys Targaryen",
                "House": "House Targaryen of Dragonstone",
                "Titles": [""],
                "Bio": "Daenerys Targaryen, the Mother of Dragons.",
                "Image": "Daenerys_Targaryen.png"
            },
            "Bran Stark": {
                "Name": "Bran Stark",
                "House": "House Stark of Winterfell",
                "Titles": [""],
                "Bio": "Bran Stark is the youngest son of House Stark.",
                "Image": "Bran_Stark.png"
            }
        }

    def show_profile_eddard(self): self.display_profile("Eddard Stark")
    def show_profile_tyrion(self): self.display_profile("Tyrion Lannister")
    def show_profile_jon(self): self.display_profile("Jon Snow")
    def show_profile_catelyn(self): self.display_profile("Catelyn Stark")
    def show_profile_arya(self): self.display_profile("Arya Stark")
    def show_profile_sansa(self): self.display_profile("Sansa Stark")
    def show_profile_daenerys(self): self.display_profile("Daenerys Targaryen")
    def show_profile_bran(self): self.display_profile("Bran Stark")

    def display_profile(self, character_name):
        profiles = self.get_character_profiles()
        character_profile = profiles[character_name]
        profile_text = f"Name: {character_profile['Name']}\n" \
                       f"House: {character_profile['House']}\n" \
                       f"Titles: {', '.join(character_profile['Titles'])}\n" \
                       f"Biography: {character_profile['Bio']}"
        
        self.update_text_box(profile_text)
        self.update_image(character_profile['Image'])

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", text)
        self.text_box.configure(state="disabled")

    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            image = Image.open(image_path).resize((150, 190))
            photo = ctk.CTkImage(image, size=(150, 190))
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")



##class CharacterProfileBookII: