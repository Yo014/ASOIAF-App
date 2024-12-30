import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk

class BookInfo_BookI:
    def __init__(self, root):
        # Initialize Main Window
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.resizable(width=False, height=False)
        
        # GUI Components
        self.create_image()
        self.create_buttons()

    def create_image(self):
        """Display Book Cover Image."""
        image_path = "C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/A_Game_of_Thrones.png"
        image = Image.open(image_path)
        resized_image = image.resize((150, 190))
        photo = ctk.CTkImage(resized_image, size=(150, 190))

        # Display Image
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command": self.show_pov_characters, "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": self.show_book_summary, "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": self.show_character_profiles, "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": self.show_map, "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": self.show_appendix, "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback,
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self.root, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

    # Navigation Methods
    def show_pov_characters(self):
        """Navigate to POV Characters."""
        self.switch_window("POV_Characters", "POVCharactersBookI")

    def show_book_summary(self):
        """Navigate to Book Summary."""
        self.switch_window("Book_Summary", "BookSummary_BookI", customtkinter=True)

    def show_character_profiles(self):
        """Navigate to Character Profiles."""
        self.switch_window("Character_profile_viewer", "CharacterProfileBookI")

    def show_map(self):
        """Navigate to Maps."""
        self.switch_window("Map", "MapsofASOIAF")

    def show_appendix(self):
        """Navigate to Appendix."""
        self.switch_window("Appendix", "AppendixBookI")

    def getback(self):
        """Navigate Back to Main Menu."""
        self.switch_window("ASOIAF_APP", "MainMenuPage")
    
    def cancel_pending_callbacks(self):
        try:
            for widget in self.root.winfo_children():
                widget.after_cancel('all')  # Cancel animations for each widget
        except Exception as e:
            print(f"Error while canceling callbacks: {e}")

    # Window Management Helper
    def switch_window(self, module_name, class_name, customtkinter=False):
        """Destroy current window and open a new one."""
        self.cancel_pending_callbacks()
        self.root.destroy()
        new_root = ctk.CTk()
        module = __import__(module_name)
        getattr(module, class_name)(new_root)
        new_root.mainloop()



class BookInfo_BookII:
    def __init__(self, root):
        # Initialize Main Window
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.resizable(width=False, height=False)

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
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command": self.show_pov_characters, "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": self.show_book_summary, "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": self.show_character_profiles, "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": self.show_map, "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": self.show_appendix, "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback,
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self.root, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

    # Navigation Methods
    def show_pov_characters(self):
        """Navigate to POV Characters."""
        self.switch_window("POV_Characters", "POVCharactersBookII")

    def show_book_summary(self):
        """Navigate to Book Summary."""
        self.switch_window("Book_Summary", "BookSummary_BookII", customtkinter=True)

    def show_character_profiles(self):
        """Navigate to Character Profiles."""
        self.switch_window("Character_profile_viewer", "CharacterProfileBookII")

    def show_map(self):
        """Navigate to Maps."""
        self.switch_window("Map", "MapsofASOIAF")

    def show_appendix(self):
        """Navigate to Appendix."""
        self.switch_window("Appendix", "AppendixBookII")

    def getback(self):
        """Navigate Back to Main Menu."""
        self.switch_window("ASOIAF_APP", "MainMenuPage")

    def cancel_pending_callbacks(self):
        try:
            for widget in self.root.winfo_children():
                widget.after_cancel('all')  # Cancel animations for each widget
        except Exception as e:
            print(f"Error while canceling callbacks: {e}")

    # Window Management Helper
    def switch_window(self, module_name, class_name, customtkinter=False):
        """Destroy current window and open a new one."""
        self.cancel_pending_callbacks()
        self.root.destroy()
        if customtkinter:
            new_root = ctk.CTk()
        else:
            new_root = tk.Tk()
        module = __import__(module_name)
        getattr(module, class_name)(new_root)
        new_root.mainloop()


class BookInfo_BookIII:
    def __init__(self, root):
        # Initialize Main Window
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.resizable(width=False, height=False)

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
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command": self.show_pov_characters, "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": self.show_book_summary, "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": self.show_character_profiles, "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": self.show_map, "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": self.show_appendix, "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback,
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self.root, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

    # Navigation Methods
    def show_pov_characters(self):
        """Navigate to POV Characters."""
        self.switch_window("POV_Characters", "POVCharactersBookIII")

    def show_book_summary(self):
        """Navigate to Book Summary."""
        self.switch_window("Book_Summary", "BookSummary_BookIII")

    def show_character_profiles(self):
        """Navigate to Character Profiles."""
        self.switch_window("Character_profile_viewer", "CharacterProfileBookIII")

    def show_map(self):
        """Navigate to Maps."""
        self.switch_window("Map", "MapsofASOIAF")

    def show_appendix(self):
        """Navigate to Appendix."""
        self.switch_window("Appendix", "AppendixBookIII")

    def getback(self):
        """Navigate Back to Main Menu."""
        self.switch_window("ASOIAF_APP", "MainMenuPage")

    def cancel_pending_callbacks(self):
        try:
            for widget in self.root.winfo_children():
                widget.after_cancel('all')  # Cancel animations for each widget
        except Exception as e:
            print(f"Error while canceling callbacks: {e}")

    # Window Management Helper
    def switch_window(self, module_name, class_name, customtkinter=False):
        """Destroy current window and open a new one."""
        self.cancel_pending_callbacks()
        self.root.destroy()
        if customtkinter:
            new_root = ctk.CTk()
        else:
            new_root = tk.Tk()
        module = __import__(module_name)
        getattr(module, class_name)(new_root)
        new_root.mainloop()


class BookInfo_BookIV:
    def __init__(self, root):
        # Initialize Main Window
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.resizable(width=False, height=False)

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
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command": self.show_pov_characters, "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": self.show_book_summary, "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": self.show_character_profiles, "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": self.show_map, "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": self.show_appendix, "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback,
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self.root, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

    # Navigation Methods
    def show_pov_characters(self):
        """Navigate to POV Characters."""
        self.switch_window("POV_Characters", "POVCharactersBookIV")

    def show_book_summary(self):
        """Navigate to Book Summary."""
        self.switch_window("Book_Summary", "BookSummary_BookIV")

    def show_character_profiles(self):
        """Navigate to Character Profiles."""
        self.switch_window("Character_profile_viewer", "CharacterProfileBookIV")

    def show_map(self):
        """Navigate to Maps."""
        self.switch_window("Map", "MapsofASOIAF")

    def show_appendix(self):
        """Navigate to Appendix."""
        self.switch_window("Appendix", "AppendixBookIV")

    def getback(self):
        """Navigate Back to Main Menu."""
        self.switch_window("ASOIAF_APP", "MainMenuPage")

    def cancel_pending_callbacks(self):
        try:
            for widget in self.root.winfo_children():
                widget.after_cancel('all')  # Cancel animations for each widget
        except Exception as e:
            print(f"Error while canceling callbacks: {e}")

    # Window Management Helper
    def switch_window(self, module_name, class_name, customtkinter=False):
        """Destroy current window and open a new one."""
        self.cancel_pending_callbacks()
        self.root.destroy()
        if customtkinter:
            new_root = ctk.CTk()
        else:
            new_root = tk.Tk()
        module = __import__(module_name)
        getattr(module, class_name)(new_root)
        new_root.mainloop()

class BookInfo_BookV:
    def __init__(self, root):
        # Initialize Main Window
        self.root = root
        self.root.title("Book Information")
        self.root.geometry("555x600")
        self.root.resizable(width=False, height=False)
        ctk.set_theme("dark")

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
        self.image_label = ctk.CTkLabel(self.root, image=photo, text="")
        self.image_label.place(x=210, y=20)
        self.image_label.image = photo

    def create_buttons(self):
        """Create Buttons for Navigation."""
        button_config = {
            "POV Characters": {"command": self.show_pov_characters, "position": (0, 230), "width": 180, "height": 50},
            "Book Summary": {"command": self.show_book_summary, "position": (282, 230), "width": 180, "height": 50},
            "Character Profiles": {"command": self.show_character_profiles, "position": (0, 350), "width": 180, "height": 50},
            "Map": {"command": self.show_map, "position": (282, 350), "width": 180, "height": 50},
            "Appendix": {"command": self.show_appendix, "position": (140, 472), "width": 250, "height": 50},
        }

        # Create Back Button
        button_back = ctk.CTkButton(
            self.root, text="Back", command=self.getback,
            width=80, height=30, fg_color="white", text_color="black", corner_radius=8
        )
        button_back.place(x=20, y=30)

        # Create Main Buttons
        for key, config in button_config.items():
            ctk.CTkButton(
                self.root, text=key, command=config["command"],
                width=config["width"], height=config["height"],
                corner_radius=10, fg_color="white", text_color="black", hover_color="#d1e7f0"
            ).place(x=config["position"][0], y=config["position"][1])

    # Navigation Methods
    def show_pov_characters(self):
        """Navigate to POV Characters."""
        pass

    def show_book_summary(self):
        """Navigate to Book Summary."""
        self.root.destroy()
        new_root = ctk.CTk()
        from Book_Summary import BookSummary_BookV
        BookSummary_BookV(new_root)
        new_root.mainloop()

    def show_character_profiles(self):
        """Navigate to Character Profiles."""
        pass

    def show_map(self):
        """Navigate to Maps."""
        pass

    def show_appendix(self):
        """Navigate to Appendix."""
        pass

    def getback(self):
        """Navigate Back to Main Menu."""
        self.switch_window("ASOIAF_APP", "MainMenuPage")

    def cancel_pending_callbacks(self):
        try:
            for widget in self.root.winfo_children():
                widget.after_cancel('all')  # Cancel animations for each widget
        except Exception as e:
            print(f"Error while canceling callbacks: {e}")

    # Window Management Helper
    def switch_window(self, module_name, class_name, customtkinter=False):
        """Destroy current window and open a new one."""
        self.cancel_pending_callbacks()
        self.root.destroy()
        if customtkinter:
            new_root = ctk.CTk()
        else:
            new_root = tk.Tk()
        module = __import__(module_name)
        getattr(module, class_name)(new_root)
        new_root.mainloop()

