import tkinter as tk
from PIL import Image, ImageTk


class AppendixBookI:
    def __init__(self, root):
        self.root = root
        self.root.title("Appendix")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        self.create_buttons()
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=230, y=10)  # Adjust placement
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=69, height=15, state="disabled")
        self.text_box.place(x=0, y=200)
        
        # Add buttons to the interface
        self.create_buttons()
    def create_buttons(self):
            button_config = {
                "House Baratheon": {"command": self.show_house_baratheon, "position": (18, 446), "width": 18, "height": 2},
                "House Stark": {"command": self.show_house_stark, "position": (189, 446), "width": 19, "height": 2},
                "House Lannister": {"command": self.show_house_lannister, "position": (369, 446), "width": 18, "height": 2},
                "Houuse Arryn": {"command": self.show_house_arryn, "position": (18, 496), "width": 18, "height": 2},
                "House Tully": {"command": self.show_house_tully, "position": (189, 496), "width": 19, "height": 2},
                "House Tyrell": {"command": self.show_house_tyrell, "position": (369, 496), "width": 18, "height": 2},
                "House Greyjoy": {"command": self.show_house_greyjoy, "position": (18, 547), "width": 18, "height": 2},
                "House Martell": {"command": self.show_house_martell, "position": (189, 547), "width": 19, "height": 2},
                "The Old Dynasty:House Targaryen": {"command": self.show_house_targaryen, "position": (369, 547), "width": 18, "height": 2},
                "Back": {"command": self.getback, "position": (20, 30), "width": 10, "height": 1}
            }
            
            for text, config in button_config.items():
                button = tk.Button(self.root, text=text, command=config["command"], bg="WHITE",  font=("Arial", 13), width=config["width"], height=config["height"])
                button.place(x=config["position"][0], y=config["position"][1])
    def get_house_profiles(self):
        return {
            "House Baratheon":{
                "Name": "House Baratheon",
                "House description": "The youngest of the Great Houses, born during the Wars of Conquest. Its founder, OrysBaratheon, was rumored to be Aegon the Dragon  bastard brother. Orys rose through the ranks tobecome one of Aegons fiercest commanders. When he defeated and slew Argilac the Arrogant,the last Storm King, Aegon rewarded him with Argilac s castle, lands, and daughter. Orys took the girl to bride, and adopted the banner, honors, and words of her line. The Baratheon sigil is acrowned stag, black, on a golden field. Their words are Ours is the Fury",
                "House members": """
        KING ROBERT BARATHEON, the First of His Name,
                
                    - his wife, QUEEN CERSEI, of House Lannister, 
                    - their children:
                    - PRINCE JOFFREY, heir to the Iron Throne, twelve,
                    - PRINCESS MYRCELLA, a girl of eight,
                    - PRINCE TOMMEN, a boy of seven
                    - his brothers:
                    - STANNIS BARATHEON,Lord of Dragonstone,
                      - his wife, LADY SELYSE, of House Florent,
                      - their daughter, SHIREEN, a girl of nine,
                    - RENLY BARATHEON, Lord of Storms End,
                    - his small council:
                    —GRAND MAESTER PYCELLE,
                    —LORD PETYR BAELISH, called LITTLEFINGER, master of coin,
                    —LORD STANNIS BARATHEON, master of ships,
                    —LORD RENLY BARATHEON, master of laws,
                    —SER BARRISTAN SELMY, Lord Commander of the Kingsguard,
                    —VARYS, a eunuch, called the Spider, master of whisperers,
                """,
                "image": "house_baratheon.png"
            },
            "House Stark":{
                "Name": "House Stark",
                "House description":"""The Starks trace their descent from Brandon the Builder and the ancient Kings of Winter. For thousands of years they ruled from Winterfell as Kings in the North, until Torrhen Stark, the King Who Knelt, chose to swear fealty to Aegon the Dragon rather than give battle. Their blazon is a grey direwolf on an ice-white field. The Stark words are Winter Is Coming.
                """,
                "House members": """
                EDDARD STARK, Lord of Winterfell, Warden of the North,
                
                    —his wife, LADY CATELYN, of House Tully,
                    —their children:
                    —ROBB, the heir to Winterfell, fourteen years of age,
                    —SANSA, the eldest daughter, eleven,
                    —ARYA, the younger daughter, a girl of nine,
                    —BRANDON, called Bran, seven,
                    —RICKON, a boy of three,
                    —his bastard son, JON SNOW, a boy of fourteen,
                    —his ward, THEON GREYJOY, heir to the Iron Islands,
                    —his siblings:
                    —BRANDON, his elder brother, murdered by the command of Aerys II Targaryen,
                    —LYANNA, his younger sister, died in the mountains of Dorne,
                    —BENJEN, his younger brother, a man of the Night Watch,
                    —his household:
                    —MAESTER LUWIN, counsellor, healer, and tutor,
                    —VAYON POOLE, steward of Winterfell,
                    —JEYNE, his daughter, Sansa closest friend,
                    —JORY CASSEL, captain of the guard,
                    —HALLIS MOLLEN, DESMOND, JACKS, PORTHER, QUENT, ALYN,
                    TOMARD, VARLY, HEWARD, CAYN, WYL, guardsmen,
                    —SER RODRIK CASSEL, master-at-arms, Jory uncle,
                    —BETH, his young daughter,
                    —SEPTA MORDANE, tutor to Lord Eddard daughters,
                """,
            "image": "house_stark.png"
            },
            "House Lannister":{
                "Name": "House Lannister",
                "House description": """Fair-haired, tall, and handsome, the Lannisters are the blood of Andal adventurers who carved out a mighty kingdom in the western hills and valleys. Through the female line they claim descent from Lann the Clever, the legendary trickster of the Age of Heroes. The gold of Casterly Rock and the Golden Tooth has made them the wealthiest of the Great Houses. Their sigil is a golden lion upon a crimson field. The Lannister words are Hear Me Roar!
                    """,
                "House members": """
                 TYWIN LANNISTER, Lord of Casterly Rock, Warden of the West, Shield of Lannisport,
                    —his wife, {LADY JOANNA}, a cousin, died in childbed,
                    —their children:
                    —SER JAIME, called the Kingslayer, heir to Casterly Rock, a twin to Cersei,
                    —QUEEN CERSEI, wife of King Robert I Baratheon, a twin to Jaime,
                    —TYRION, called the Imp, a dwarf,

                    """,
                "image": "house_lannister.png"
            },
            "House Arryn":{
                "Name": "House Arryn",
                "House description": """
                    The Arryns are the blood of the Kings of the North, the heroes of the Age of Heroes.
                    """ ,
                "House members": """
                """,
                "image": "house_arryn.png"
            },
            "House Tully":{
                "Name": "House Tully",
                "House description": """
                    The Tullys are the blood of the Kings of the Vale, the heroes of the Age of Heroes.
                    """ ,
                "House members": """
                """,
                "image": "house_tully.png"
                
            },
            "House Tyrell":{
                "Name": "House Tyrell",
                "House description": """
                    The Tyrells are the blood of the Kings of the Reach, the heroes of the Age of Heroes.
                    """ ,
                "House members": """
                """,
                "image": "house_tyrell.png"
            },
            "House Greyjoy":{
                "Name": "House Greyjoy",
                "House description": """
                    The Greyjoys are the blood of the Kings of the Iron Islands, the heroes of the Age of Heroes.
                    """ ,
                "House members": """
                """,
                "image": "house_greyjoy.png"
                
            },
            "House Martell":{
                "Name": "House Martell",
                "House description": """
                    The Martells are the blood of the Kings of the Vale, the heroes of the Age of Heroes.
                    """ ,
                "House members": """
                """,
                "image": "house_martell.png"
            },
            "House Targaryen":{
                "Name": "House Targaryen",
                "House description": """
                    The Targaryens are the blood of the Kings of the Seven Kingdoms, the heroes of the Age of Heroes.
                    """ ,
                "House members": """
                """,
                "image": "house_targaryen.png"
            }  
        }
    def show_house_baratheon(self):self.show_house_profile("House Baratheon")
    def show_house_stark(self):self.show_house_profile("House Stark")
    def show_house_lannister(self):self.show_house_profile("House Lannister")
    def show_house_arryn(self):self.show_house_profile("House Arryn")
    def show_house_tully(self):self.show_house_profile("House Tully")
    def show_house_tyrell(self):self.show_house_profile("House Tyrell") 
    def show_house_greyjoy(self):self.show_house_profile("House Greyjoy")
    def show_house_martell(self):self.show_house_profile("House Martell")
    def show_house_targaryen(self):self.show_house_profile("House Targaryen")
    def show_house_profile(self, house_name):
        houses = self.get_house_profiles()
        house_profile =houses[house_name]
        house_text= f"House Name: {house_profile['Name']}\n" \
                    f"House Description: {house_profile['House description']}\n" \
                    f"House Members: {house_profile['House members']}"
        self.update_text_box(house_text)
        self.update_image(house_profile['image'])
    
    def update_text_box(self, text):
        """
        Update the text box with the provided text.

        Parameters
        ----------
        text : str
            The text to be displayed in the text box.

        Returns
        -------
        None
        """
        self.text_box.config(state="normal")
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, text)
        self.text_box.config(state="disabled")
    def update_image(self, image_name):
        """
        Updates the image displayed in the character profile.

        Args:
            image_name (str): The name of the image file to be loaded.

        Raises:
            Exception: If there is an error loading the image, it prints an error message and updates the text box with a failure message.
        """
        try:
            ##image_path = f"/Users/santomukiza/Desktop/test/character_profile/Png Files/{image_name}"
            image_path=f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/House Sigiles/{image_name}"
            pil_image = Image.open(image_path).resize((150, 190))
            tk_image = ImageTk.PhotoImage(pil_image)
            self.image_label.config(image=tk_image)
            self.image_label.image = tk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")
    def getback(self):
        self.root.destroy() 
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        
 