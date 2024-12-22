import tkinter as tk
from PIL import Image, ImageTk

class CharacterProfileBookI:
    def __init__(self, root):
        """
        Initialize the Character Profile Viewer interface.

        Parameters
        ----------
        root : tkinter.Tk
            The root window of the application.

        Returns
        -------
        None
        """
        self.root = root
        self.root.title("Character Profile Viewer")
        self.root.geometry("600x600")
        self.root.configure(bg="light blue")
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=230, y=20)  # Adjust placement
        
        self.text_box = tk.Text(root, wrap=tk.WORD, width=65, height=10, state="disabled")
        self.text_box.place(x=15, y=200)
        
        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config = {
            "Tyrion Lannister": self.show_profile_tyrion,
            "Jon Snow": self.show_profile_jon,
            "Eddard Stark": self.show_profile_eddard,
            "Daenerys Targaryen": self.show_profile_daenerys,
            "Catelyn Stark": self.show_profile_catelyn,
            "Arya Stark": self.show_profile_arya,
            "Sansa Stark": self.show_profile_sansa,
            "Bran Stark": self.show_profile_bran,
            "Back": self.getback
        }
        
        # Define button positions
        positions = [
            (20, 400), (263, 400), (470, 400), (20, 450),
            (263, 450), (470, 450), (160, 500), (350, 500),(20,30)
        ]
        
        for (text, command), (x, y) in zip(button_config.items(), positions):
            button = tk.Button(self.root, text=text, command=command, bg="WHITE", relief=tk.FLAT)
            button.place(x=x, y=y)
##TO DO : UPDATE WITH THE ACTUAL CHARACTERS DESCRIPTIONS FOR A GAME OF THRONES BOOK I
    def get_character_profiles(self):
        """
        Returns a dictionary containing character profiles for various 
        characters from the 'Game of Thrones' series.

        Each character profile contains the following information:
        - Name: The full name of the character.
        - House: The noble house to which the character belongs.
        - Titles: A list of titles held by the character.
        - Bio: A brief biography of the character.
        - Image: The filename of the character's image.
        
        Returns:
            dict: A dictionary where keys are character names and values 
            are dictionaries containing profile information.
        """
        # Store profiles for all characters in a dictionary
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

    # Functions to display profiles
    def show_profile_eddard(self): self.display_profile("Eddard Stark")
    def show_profile_tyrion(self): self.display_profile("Tyrion Lannister")
    def show_profile_jon(self): self.display_profile("Jon Snow")
    def show_profile_catelyn(self): self.display_profile("Catelyn Stark")
    def show_profile_arya(self): self.display_profile("Arya Stark")
    def show_profile_sansa(self): self.display_profile("Sansa Stark")
    def show_profile_daenerys(self): self.display_profile("Daenerys Targaryen")
    def show_profile_bran(self): self.display_profile("Bran Stark")

    def display_profile(self, character_name):
        """
        Displays the profile of a given character.
        Args:
            character_name (str): The name of the character whose profile is to be displayed.
        Retrieves the character profiles, extracts the profile for the specified character,
        formats the profile information into a text string, and updates the text box and image
        with the character's profile information.
        """
        profiles = self.get_character_profiles()
        character_profile = profiles[character_name]
        profile_text = f"Name: {character_profile['Name']}\n" \
                       f"House: {character_profile['House']}\n" \
                       f"Titles: {', '.join(character_profile['Titles'])}\n" \
                       f"Biography: {character_profile['Bio']}"
        
        self.update_text_box(profile_text)
        self.update_image(character_profile['Image'])

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
            image_path=f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((150, 160))
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
        new_root.mainloop()

##class CharacterProfileBookII: