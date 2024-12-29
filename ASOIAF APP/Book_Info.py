import tkinter as tk
from PIL import Image, ImageTk

class BookInfo_BookI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Game_of_Thrones.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config={
            "POV Characters": {"name": "POV Characters","command": self.show_pov_characters, "position": (0, 230), "width": 17, "height": 3},
            "Book Summary": {"name": "Book Summary","command": self.show_book_summary, "position": (282, 230), "width": 17, "height": 3},
            "Character Profiles": {"name": "Character Profiles","command": self.show_character_profiles, "position": (0, 350), "width": 17, "height": 3},
            "Map": {"name": "Map","command": self.show_map, "position": (282, 350), "width": 17, "height": 3},
            "Appendix": {"name": "Appendix","command": self.show_appendix, "position": (0, 472), "width": 34, "height": 4},
            
            
        }
        button_back= tk.Button(self.root, text="Back", command=self.getback, bg="WHITE", relief=tk.FLAT,)
        button_back.place(x=20, y=30)
        for  key, config in button_config.items():

            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
            button.place(x=config["position"][0], y=config["position"][1])
    def show_pov_characters(self):
        self.root.destroy()
        new_root = tk.Tk()
        from POV_Characters import POVCharactersBookI
        POVCharactersBookI(new_root)
        new_root.mainloop()

    def show_book_summary(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Summary import BookSummary_BookI
        BookSummary_BookI(new_root)
        new_root.mainloop()

    def show_character_profiles(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Character_profile_viewer import CharacterProfileBookI
        CharacterProfileBookI(new_root)
        new_root.mainloop()
    def show_map(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Map import MapsofASOIAF
        MapsofASOIAF(new_root)
        new_root.mainloop()
    def show_appendix(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Appendix import AppendixBookI
        AppendixBookI(new_root)
        new_root.mainloop()
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from ASOIAF_APP import MainMenuPage
        MainMenuPage(new_root)
        new_root.mainloop()

class BookInfo_BookII:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Clash_of_Kings.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config={
            "POV Characters": {"name": "POV Characters","command": self.show_pov_characters, "position": (0, 230), "width": 17, "height": 3},
            "Book Summary": {"name": "Book Summary","command": self.show_book_summary, "position": (282, 230), "width": 17, "height": 3},
            "Character Profiles": {"name": "Character Profiles","command": self.show_character_profiles, "position": (0, 350), "width": 17, "height": 3},
            "Map": {"name": "Map","command": self.show_map, "position": (282, 350), "width": 17, "height": 3},
            "Appendix": {"name": "Appendix","command": self.show_appendix, "position": (0, 472), "width": 34, "height": 4},
            
            
        }
        button_back= tk.Button(self.root, text="Back", command=self.getback, bg="WHITE", relief=tk.FLAT,)
        button_back.place(x=20, y=30)
        for  key, config in button_config.items():

            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
            button.place(x=config["position"][0], y=config["position"][1])
    def show_pov_characters(self):
        self.root.destroy()
        new_root = tk.Tk()
        from POV_Characters import POVCharactersBookII
        POVCharactersBookII(new_root)
        new_root.mainloop()

    def show_book_summary(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Summary import BookSummary_BookII
        BookSummary_BookII(new_root)
        new_root.mainloop()

    def show_character_profiles(self):
       pass
    def show_map(self):
        pass
    def show_appendix(self):
        pass
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from ASOIAF_APP import MainMenuPage
        MainMenuPage(new_root)
        new_root.mainloop()

class BookInfo_BookIII:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Storm_Of_Swords.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config={
            "POV Characters": {"name": "POV Characters","command": self.show_pov_characters, "position": (0, 230), "width": 17, "height": 3},
            "Book Summary": {"name": "Book Summary","command": self.show_book_summary, "position": (282, 230), "width": 17, "height": 3},
            "Character Profiles": {"name": "Character Profiles","command": self.show_character_profiles, "position": (0, 350), "width": 17, "height": 3},
            "Map": {"name": "Map","command": self.show_map, "position": (282, 350), "width": 17, "height": 3},
            "Appendix": {"name": "Appendix","command": self.show_appendix, "position": (0, 472), "width": 34, "height": 4},
            
            
        }
        button_back= tk.Button(self.root, text="Back", command=self.getback, bg="WHITE", relief=tk.FLAT,)
        button_back.place(x=20, y=30)
        for  key, config in button_config.items():

            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
            button.place(x=config["position"][0], y=config["position"][1])
    def show_pov_characters(self):
        self.root.destroy()
        new_root = tk.Tk()
        from POV_Characters import POVCharactersBookIII
        POVCharactersBookIII(new_root)
        new_root.mainloop()

    def show_book_summary(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Summary import BookSummary_BookIII
        BookSummary_BookIII(new_root)
        new_root.mainloop()

    def show_character_profiles(self):
       pass
    def show_map(self):
        pass
    def show_appendix(self):
        pass
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from ASOIAF_APP import MainMenuPage
        MainMenuPage(new_root)
        new_root.mainloop()
        
class BookInfo_BookIV:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Feast_for_Crows.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config={
            "POV Characters": {"name": "POV Characters","command": self.show_pov_characters, "position": (0, 230), "width": 17, "height": 3},
            "Book Summary": {"name": "Book Summary","command": self.show_book_summary, "position": (282, 230), "width": 17, "height": 3},
            "Character Profiles": {"name": "Character Profiles","command": self.show_character_profiles, "position": (0, 350), "width": 17, "height": 3},
            "Map": {"name": "Map","command": self.show_map, "position": (282, 350), "width": 17, "height": 3},
            "Appendix": {"name": "Appendix","command": self.show_appendix, "position": (0, 472), "width": 34, "height": 4},
            
            
        }
        button_back= tk.Button(self.root, text="Back", command=self.getback, bg="WHITE", relief=tk.FLAT,)
        button_back.place(x=20, y=30)
        for  key, config in button_config.items():

            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
            button.place(x=config["position"][0], y=config["position"][1])
    def show_pov_characters(self):
        pass

    def show_book_summary(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Summary import BookSummary_BookIV
        BookSummary_BookIV(new_root)
        new_root.mainloop()
    def show_character_profiles(self):
       pass
    def show_map(self):
        pass
    def show_appendix(self):
        pass
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from ASOIAF_APP import MainMenuPage
        MainMenuPage(new_root)
        new_root.mainloop()

class BookInfo_BookV:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.configure(bg="light blue")
        
        # Initialize GUI components
        self.image_label = tk.Label(root, bg="light blue")
        self.image_label.place(x=210, y=20)  # Adjust placement
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Dance_With_Dragons.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))  # Resize the image
        photo = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
        # Add buttons to the interface
        self.create_buttons()

    def create_buttons(self):
        button_config={
            "POV Characters": {"name": "POV Characters","command": self.show_pov_characters, "position": (0, 230), "width": 17, "height": 3},
            "Book Summary": {"name": "Book Summary","command": self.show_book_summary, "position": (282, 230), "width": 17, "height": 3},
            "Character Profiles": {"name": "Character Profiles","command": self.show_character_profiles, "position": (0, 350), "width": 17, "height": 3},
            "Map": {"name": "Map","command": self.show_map, "position": (282, 350), "width": 17, "height": 3},
            "Appendix": {"name": "Appendix","command": self.show_appendix, "position": (0, 472), "width": 34, "height": 4},
            
            
        }
        button_back= tk.Button(self.root, text="Back", command=self.getback, bg="WHITE", relief=tk.FLAT,)
        button_back.place(x=20, y=30)
        for  key, config in button_config.items():

            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
            button.place(x=config["position"][0], y=config["position"][1])
    def show_pov_characters(self):
        pass

    def show_book_summary(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Summary import BookSummary_BookV
        BookSummary_BookV(new_root)
        new_root.mainloop()

    def show_character_profiles(self):
       pass
    def show_map(self):
        pass
    def show_appendix(self):
        pass
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from ASOIAF_APP import MainMenuPage
        MainMenuPage(new_root)
        new_root.mainloop()