import tkinter as tk
from PIL import Image, ImageTk
class POVCharactersBookI:
    """
    This class creates a GUI for showing the point of view characters
    in the first book of the A Song of Ice and Fire series.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Point of View Characters")
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
        # Add buttons to the interface
        """
        Creates buttons dynamically for different characters in the first book of.
        This method reads the button configuration from a predefined dictionary,
        loads the corresponding images, resizes them, and creates buttons with
        the specified commands and positions. The buttons are then placed on the
        root window.
        """
        button_config = {
            "Eddard":{ "name": "Eddard", "command": self.show_eddard_Chapters, "position": (0, 250), "width": 17, "height": 2},
            "Catelyn":{ "name": "Catelyn", "command": self.show_catelyn_Chapters, "position": (282, 250), "width": 17, "height": 2},
            "Tyrion":{ "name": "Tyrion", "command": self.show_tyrion_Chapters, "position": (0, 337), "width": 17, "height": 2},
            "Jon":{ "name": "Jon", "command": self.show_Characters, "position": (282, 337), "width": 17, "height": 2},
            "Daenerys":{ "name": "Daenerys", "command": self.show_daenerys_Chapters, "position": (0, 425), "width": 17, "height": 2},
            "Arya":{ "name": "Arya", "command": self.show_arya_Chapters, "position": (282, 425), "width": 17, "height": 2},
            "Sansa":{ "name": "Sansa", "command": self.show_sansa_Chapters, "position": (0, 513), "width": 17, "height": 2},
            "Bran":{ "name": "Bran", "command": self.show_bran_Chapters, "position": (282, 513), "width": 17, "height": 2},
            "Back":{ "name": "Back", "command": self.getback, "position": (20, 30), "width": 0, "height": 0}
            
        }
        for key, config in button_config.items():
            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
            button.place(x=config["position"][0], y=config["position"][1])

    def show_eddard_Chapters(self):
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
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookI
        BookInfo_BookI(new_root)
        new_root.mainloop()


class POVCharactersBookII:
    def __init__(self, root):
        self.root = root
        self.root.title("Point of View Characters")
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
        # Add buttons to the interface
        button_config = {
            "Davos":{ "name": "Davos", "command": self.show_davos_Chapters, "position": (0, 250), "width": 17, "height": 2},
            "Catelyn":{ "name": "Catelyn", "command": self.show_catelyn_Chapters, "position": (282, 250), "width": 17, "height": 2},
            "Tyrion":{ "name": "Tyrion", "command": self.show_tyrion_Chapters, "position": (0, 337), "width": 17, "height": 2},
            "Jon":{ "name": "Jon", "command": self.show_Characters, "position": (282, 337), "width": 17, "height": 2},
            "Daenerys":{ "name": "Daenerys", "command": self.show_daenerys_Chapters, "position": (0, 425), "width": 17, "height": 2},
            "Arya":{ "name": "Arya", "command": self.show_arya_Chapters, "position": (282, 425), "width": 17, "height": 2},
            "Sansa":{ "name": "Sansa", "command": self.show_sansa_Chapters, "position": (0, 513), "width": 11, "height": 2},
            "Bran":{ "name": "Bran", "command": self.show_bran_Chapters, "position": (187, 513), "width": 11, "height": 2},
            "Theon":{ "name": "Theon", "command": self.show_theon_Chapters, "position": (374, 513), "width": 11, "height": 2},
            "Back":{ "name": "Back", "command": self.getback, "position": (20, 30), "width": 0, "height": 0}
            
        }
        for key, config in button_config.items():
            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
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
    def show_theon_Chapters(self):
        pass
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookII
        BookInfo_BookII(new_root)
        new_root.mainloop()

class POVCharactersBookIII:
    def __init__(self, root):
        self.root = root
        self.root.title("Point of View Characters")
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
        # Add buttons to the interface
        button_config = {
            "Davos":{ "name": "Davos", "command": self.show_davos_Chapters, "position": (0, 250), "width": 11, "height": 2},
            "Catelyn":{ "name": "Catelyn", "command": self.show_catelyn_Chapters, "position": (187, 250), "width": 11, "height": 2},
            "Jaime":{ "name": "Jaime", "command": self.show_jaime_Chapters, "position": (374, 250), "width": 11, "height": 2},
            "Tyrion":{ "name": "Tyrion", "command": self.show_tyrion_Chapters, "position": (374, 337), "width": 11, "height": 2},
            "Jon":{ "name": "Jon", "command": self.show_Characters, "position": (0, 337), "width": 11, "height": 2},
            "Bran":{ "name": "Bran", "command": self.show_bran_Chapters, "position": (187, 337), "width": 11, "height": 2},
            "Daenerys":{ "name": "Daenerys", "command": self.show_daenerys_Chapters, "position": (0, 425), "width": 17, "height": 2},
            "Arya":{ "name": "Arya", "command": self.show_arya_Chapters, "position": (282, 425), "width": 17, "height": 2},
            "Sansa":{ "name": "Sansa", "command": self.show_sansa_Chapters, "position": (0, 513), "width": 17, "height": 2},
            "Samwell":{ "name": "Samwell", "command": self.show_samwell_Chapters, "position": (282, 513), "width": 17, "height": 2},
            "Back":{ "name": "Back", "command": self.getback, "position": (20, 30), "width": 0, "height": 0}
            
        }
        for key, config in button_config.items():
            button = tk.Button(self.root, text=config["name"], command=config["command"], bg="WHITE", width=config["width"], height= config["height"], font=("Arial", 20))
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
    def getback(self):
        self.root.destroy()
        new_root = tk.Tk()
        from Book_Info import BookInfo_BookII
        BookInfo_BookII(new_root)
        new_root.mainloop()