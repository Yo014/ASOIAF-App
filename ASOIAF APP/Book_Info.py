import customtkinter as ctk
from PIL import Image


class BookInfo_BookI(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_image()
        self.create_buttons()

    def create_image(self):
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Game_of_Thrones.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))
        self.image_label = ctk.CTkLabel(self, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        from Book_Summary import BookSummary_BookI
        from Character_profile_viewer import CharacterProfileBookI
        from Map import MapsofASOIAF
        from Appendix import AppendixBookI
        from ASOIAF_APP import MainMenuPage
        button_config = {
            "POV Characters": {"command": lambda: self.controller.show_frame(POVCharactersBookI), "position": (20,230), "width": 180, "height": 50},
            "Book Summary": {"command": lambda: self.controller.show_frame(BookSummary_BookI), "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": lambda: self.controller.show_frame(CharacterProfileBookI), "position": (20, 350), "width": 180, "height": 50},
            "Map": {"command": lambda: self.controller.show_frame(MapsofASOIAF), "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": lambda: self.controller.show_frame(AppendixBookI), "position": (140, 472), "width": 250, "height": 50},
        }

        button_back = ctk.CTkButton(self, text="Back", command=lambda: self.controller.show_frame(MainMenuPage), width=80, height=30, corner_radius=8)
        button_back.place(x=20, y=30)

        for key, config in button_config.items():
            ctk.CTkButton(self, text=key, command=config["command"], width=config["width"], height=config["height"], corner_radius=10, hover_color="#d1e7f0").place(x=config["position"][0], y=config["position"][1])

class BookInfo_BookII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Initialize Main Window
        self.controller = controller

        # GUI Components
        self.create_image()
        self.create_buttons()

    def create_image(self):
        """Display Book Cover Image."""
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_of_Kings.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))

        # Display Image
        self.image_label = ctk.CTkLabel(self, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        from POV_Characters import POVCharactersBookI, POVCharactersBookII, POVCharactersBookIII
        from Book_Summary import BookSummary_BookI, BookSummary_BookII, BookSummary_BookIII, BookSummary_BookIV, BookSummary_BookV
        from Character_profile_viewer import CharacterProfileBookI
        from Map import MapsofASOIAF
        from Appendix import AppendixBookI
        from ASOIAF_APP import MainMenuPage
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command":lambda: self.controller.show_frame(POVCharactersBookII), "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": lambda: self.controller.show_frame(BookSummary_BookII), "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": lambda: self.controller.show_frame(CharacterProfileBookI), "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": lambda: self.controller.show_frame(MapsofASOIAF), "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command":lambda: self.controller.show_frame(AppendixBookI), "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self, text="Back", command= lambda: self.controller.show_frame(MainMenuPage),
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

class BookInfo_BookIII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Initialize Main Window
        self.controller = controller


        # GUI Components
        self.create_image()
        self.create_buttons()

    def create_image(self):
        """Display Book Cover Image."""
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_Of_Swords.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))

        # Display Image
        self.image_label = ctk.CTkLabel(self, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        from POV_Characters import POVCharactersBookI, POVCharactersBookII, POVCharactersBookIII
        from Book_Summary import BookSummary_BookI, BookSummary_BookII, BookSummary_BookIII, BookSummary_BookIV, BookSummary_BookV
        from Character_profile_viewer import CharacterProfileBookI
        from Map import MapsofASOIAF
        from Appendix import AppendixBookI
        from ASOIAF_APP import MainMenuPage
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command":lambda: self.controller.show_frame(POVCharactersBookIII), "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": lambda: self.controller.show_frame(BookSummary_BookIII),  "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": lambda: self.controller.show_frame(CharacterProfileBookI), "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": lambda: self.controller.show_frame(MapsofASOIAF), "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": lambda: self.controller.show_frame(AppendixBookI), "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self, text="Back", command= lambda: self.controller.show_frame(MainMenuPage),
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

class BookInfo_BookIV(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Initialize Main Window
        self.controller = controller


        # GUI Components
        self.create_image()
        self.create_buttons()

    def create_image(self):
        """Display Book Cover Image."""
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Feast_for_Crows.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))

        # Display Image
        self.image_label = ctk.CTkLabel(self, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        from POV_Characters import POVCharactersBookI, POVCharactersBookII, POVCharactersBookIII
        from Book_Summary import BookSummary_BookI, BookSummary_BookII, BookSummary_BookIII, BookSummary_BookIV, BookSummary_BookV
        from Character_profile_viewer import CharacterProfileBookI
        from Map import MapsofASOIAF
        from Appendix import AppendixBookI
        from ASOIAF_APP import MainMenuPage
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command":lambda: self.controller.show_frame(POVCharactersBookI), "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": lambda: self.controller.show_frame(BookSummary_BookIV), "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": lambda: self.controller.show_frame(CharacterProfileBookI), "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": lambda: self.controller.show_frame(MapsofASOIAF), "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": lambda: self.controller.show_frame(AppendixBookI), "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self, text="Back", command= lambda: self.controller.show_frame(MainMenuPage),
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

class BookInfo_BookV(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Initialize Main Window
        self.controller = controller


        # Initialize GUI components
        self.create_image()
        self.create_buttons()

    def create_image(self):
        """Display Book Cover Image."""
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Dance_With_Dragons.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))

        # Display Image
        self.image_label = ctk.CTkLabel(self, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        from POV_Characters import POVCharactersBookI, POVCharactersBookII, POVCharactersBookIII
        from Book_Summary import BookSummary_BookI, BookSummary_BookII, BookSummary_BookIII, BookSummary_BookIV, BookSummary_BookV
        from Character_profile_viewer import CharacterProfileBookI
        from Map import MapsofASOIAF
        from Appendix import AppendixBookI
        from ASOIAF_APP import MainMenuPage
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command":lambda: self.controller.show_frame(POVCharactersBookI), "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": lambda: self.controller.show_frame(BookSummary_BookV), "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": lambda: self.controller.show_frame(CharacterProfileBookI), "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command":lambda: self.controller.show_frame(MapsofASOIAF), "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": lambda: self.controller.show_frame(AppendixBookI), "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self, text="Back", command= lambda: self.controller.show_frame(MainMenuPage),
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])