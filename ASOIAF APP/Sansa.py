import customtkinter as ctk
from PIL import Image

class SansaBookI(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)  # Adjust placement  
        
        self.text_box=ctk.CTkTextbox(self,font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)
        
        self.create_slider()
        self.create_buttons()
    
    def create_slider(self):
        self.slider = ctk.CTkSlider(self, 
                from_=1, to=6, number_of_steps=6,
                command=self.slider_changed, 
                width=400, 
                progress_color="orange",
                button_color="white",
                button_hover_color="white",
                height=30,
                
                )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Sansa {self.convert_to_roman(chapter_index)}"
        self.display_Sansa(chapter_name)
    def convert_to_roman(self, num):
        roman_numerals=["I", "II", "III", "IV", "V", "VI"]
        return roman_numerals[num-1]
    
    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookI), width=80, height=30, 
            corner_radius=8,bg_color="transparent",fg_color="transparent",hover_color="grey",font=("Arial", 18)
        )
        button_back.place(x=20, y=30)
    
    def show_Sansa_chapter(self):
        return {
        "Sansa I": {
            "content": "Sansa I:Joffrey takes Sansa out riding, where they encounter Arya playing at swords with a boy. A drunken Joffrey challenges the boy, but is attacked by Arya and his arm is mangled by Arya's direwolf Nymeria.",
            "image": "Sansa_Stark.png"
        },
        "Sansa II": {
            "content": "Sansa II:Sansa attends the Hand’s tournament, where she witnesses the death of a young knight during a joust with Gregor Clegane. After the night’s feast, Sandor Clegane escorts Sansa back to the Red Keep.",
            "image": "Sansa_Stark.png"
        },
        "Sansa III": {
            "content": "Sansa III:Eddard tells Sansa and Arya he is sending them back to Winterfell for their own safety.",
            "image": "Sansa_Stark.png"
        },
        "Sansa IV": {
            "content": "Sansa IV:Sansa is brought before Cersei, who tells her to write a letter to Robb urging him not to take up arms.",
            "image": "Sansa_Stark.png"
        },
        "Sansa V": {
            "content": "Sansa V:Sansa comes to Joffrey’s first court to beg for mercy for Eddard.",
            "image": "Sansa_Stark.png"
        },
        "Sansa VI": {
            "content": "Sansa VI:Joffrey mocks and threatens Sansa and has his Kingsguard beat her.",
            "image": "Sansa_Stark.png"
        }
    }
    def display_Sansa(self, sansa_name):
        profiles = self.show_Sansa_chapter()
        Sansa_chapter = profiles[sansa_name]
        chapter_text = f"{Sansa_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Sansa_chapter['image'])
        
    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", ctk.END)
        self.text_box.insert(ctk.END, text)
        self.text_box.configure(state="disabled")
        
    def update_image(self, image_name):
        
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")

#book2
class SansaBookII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Initialize GUI components
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()

    def create_slider(self):
        self.slider = ctk.CTkSlider(
            self, 
            from_=1, to=8, number_of_steps=7,
            command=self.slider_changed, 
            width=400, 
            progress_color="orange",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Sansa {self.convert_to_roman(chapter_index)}"
        self.display_Sansa(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
        return roman_numerals[num-1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookII
        button_back = ctk.CTkButton(
            self, text="Back",
            command=lambda: self.controller.show_frame(POVCharactersBookII),
            width=80, height=30,
            corner_radius=8,
            bg_color="transparent",
            fg_color="transparent",
            hover_color="grey",
            font=("Arial", 18)
        )
        button_back.place(x=20, y=30)

    def show_Sansa_chapter(self):
        return {
            "Sansa I": {
                "content": "Sansa I: Sansa attends court with Joffrey and pleads for her brother Robb's life but is mocked.",
                "image": "Sansa_Stark.png"
            },
            "Sansa II": {
                "content": "Sansa II: Joffrey forces Sansa to look upon her father's head on a spike.",
                "image": "Sansa_Stark.png"
            },
            "Sansa III": {
                "content": "Sansa III: Sansa receives an invitation from Ser Dontos Hollard to meet in secret.",
                "image": "Sansa_Stark.png"
            },
            "Sansa IV": {
                "content": "Sansa IV: Sansa suffers Joffrey’s cruelty at court and prays for escape.",
                "image": "Sansa_Stark.png"
            },
            "Sansa V": {
                "content": "Sansa V: During Stannis's attack on King's Landing, Sansa prays in the holdfast.",
                "image": "Sansa_Stark.png"
            },
            "Sansa VI": {
                "content": "Sansa VI: Cersei reveals her grim outlook on their likely fate if King's Landing falls.",
                "image": "Sansa_Stark.png"
            },
            "Sansa VII": {
                "content": "Sansa VII: The battle concludes with Stannis defeated, and Sansa’s betrothal to Joffrey ends.",
                "image": "Sansa_Stark.png"
            },
            "Sansa VIII": {
                "content": "Sansa VIII: Ser Dantos offers Sansa a chance to escape King's Landing.",
                "image": "Sansa_Stark.png"
            }
        }

    def display_Sansa(self, sansa_name):
        profiles = self.show_Sansa_chapter()
        Sansa_chapter = profiles[sansa_name]
        chapter_text = f"{Sansa_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Sansa_chapter['image'])

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", ctk.END)
        self.text_box.insert(ctk.END, text)
        self.text_box.configure(state="disabled")

    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")


##Book III

class SansaBookIII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()

    def create_slider(self):
        self.slider = ctk.CTkSlider(
            self,
            from_=1, to=7, number_of_steps=6,
            command=self.slider_changed,
            width=400,
            progress_color="pink",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Sansa {self.convert_to_roman(chapter_index)}"
        self.display_Sansa(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
        return roman_numerals[num-1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookIII
        button_back = ctk.CTkButton(
            self, text="Back",
            command=lambda: self.controller.show_frame(POVCharactersBookIII),
            width=80, height=30,
            corner_radius=8,
            bg_color="transparent",
            fg_color="transparent",
            hover_color="grey",
            font=("Arial", 18)
        )
        button_back.place(x=20, y=30)

    def show_Sansa_chapter(self):
        return {
            "Sansa I": {"content": "Sansa I: Sansa adjusts to her role at court after Blackwater.", "image": "Sansa_Stark.png"},
            "Sansa II": {"content": "Sansa II: Sansa learns she is betrothed to Tyrion Lannister.", "image": "Sansa_Stark.png"},
            "Sansa III": {"content": "Sansa III: Sansa is married to Tyrion against her will.", "image": "Sansa_Stark.png"},
            "Sansa IV": {"content": "Sansa IV: Sansa struggles with her new marriage to Tyrion.", "image": "Sansa_Stark.png"},
            "Sansa V": {"content": "Sansa V: Sansa is manipulated by Olenna Tyrell and Petyr Baelish.", "image": "Sansa_Stark.png"},
            "Sansa VI": {"content": "Sansa VI: Sansa unwittingly becomes part of Joffrey's assassination plot.", "image": "Sansa_Stark.png"},
            "Sansa VII": {"content": "Sansa VII: Sansa flees King's Landing with Littlefinger after Joffrey's death.", "image": "Sansa_Stark.png"},
        }

    def display_Sansa(self, sansa_name):
        profiles = self.show_Sansa_chapter()
        Sansa_chapter = profiles[sansa_name]
        chapter_text = f"{Sansa_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Sansa_chapter['image'])

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", ctk.END)
        self.text_box.insert(ctk.END, text)
        self.text_box.configure(state="disabled")

    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")
