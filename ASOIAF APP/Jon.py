import customtkinter as ctk
from PIL import Image

class JonBookI(ctk.CTkFrame):
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
                from_=1, to=9, number_of_steps=10,
                command=self.slider_changed, 
                width=400, 
                progress_color="white",
                button_color="white",
                button_hover_color="white",
                height=30,
                
                )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Jon {self.convert_to_roman(chapter_index)}"
        self.display_Jon(chapter_name)
    def convert_to_roman(self, num):
        roman_numerals=["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        return roman_numerals[num-1]
    
    def create_buttons(self):
        from POV_Characters import POVCharactersBookI
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookI), width=80, height=30, 
            corner_radius=8,bg_color="transparent",fg_color="transparent",hover_color="grey",font=("Arial", 18)
        )
        button_back.place(x=20, y=30)
    def show_Jon_chapter(self):
        return {
        "Jon I": {
            "content": "Jon I:A feast is held in honor of the king. Tyrion Lannister, brother of the queen and a dwarf, speaks with Jon Snow about being Eddard Stark's bastard son. Jon declares that he wishes to join the Night's Watch.",
            "image": "Jon_Snow.png"
        },
        "Jon II": {
            "content": "Jon II:Before leaving with his uncle Benjen Stark for the Wall, Jon visits with Bran, Robb, and Arya. He gives Arya a small sword named Needle.",
            "image": "Jon_Snow.png"
        },
        "Jon III": {
            "content": "Jon III:Jon begins his training at Castle Black. Benjen Stark has gone missing on a ranging beyond the Wall.",
            "image": "Jon_Snow.png"
        },
        "Jon IV": {
            "content": "Jon IV:Samwell Tarly, a coward forced to join the Night's Watch by his father, arrives at the Wall. Jon convinces the trainees to help Sam avoid mistreatment at the hands of Ser Alliser Thorne.",
            "image": "Jon_Snow.png"
        },
        "Jon V": {
            "content": "Jon V:Jon and several of his friends learn they are to be raised to the Night's Watch. Jon sees Maester Aemon about raising Sam as well.",
            "image": "Jon_Snow.png"
        },
        "Jon VI": {
            "content": "Jon VI:Jon, Sam and several others are raised to the Night's Watch. Ghost discovers a rotting hand beyond the Wall.",
            "image": "Jon_Snow.png"
        },
        "Jon VII": {
            "content": "Jon VII:Lord Commander Mormont examines the corpses of two of Ben Stark's rangers and orders them brought back to Castle Black. Jon learns of Eddard's arrest and assaults Ser Alliser, which gets him arrested. Jon saves Lord Commander Mormont from a wight.",
            "image": "Jon_Snow.png"
        },
        "Jon VIII": {
            "content": "Jon VIII:Maester Aemon tells Jon about his past as Jon grapples with the decision of whether or not to desert to help his father.",
            "image": "Jon_Snow.png"
        },
        "Jon IX": {
            "content": "Jon IX:Jon deserts the Night's Watch to join Robb, but his friends are able to bring him back. Lord Commander Mormont declares his intention to lead a large expedition north to find Benjen Stark and Mance Rayder.",
            "image": "Jon_Snow.png"
        }
    }


    def display_Jon(self, Jon_name):
        profiles = self.show_Jon_chapter()
        Jon_chapter = profiles[Jon_name]
        chapter_text = f"{Jon_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Jon_chapter['image'])
        
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

class JonBookII(ctk.CTkFrame):
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
            progress_color="white",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Jon {self.convert_to_roman(chapter_index)}"
        self.display_Jon(chapter_name)

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

    def show_Jon_chapter(self):
        return {
            "Jon I": {
                "content": "Jon I: Jon prepares to join the Great Ranging north of the Wall led by Lord Commander Mormont.",
                "image": "Jon_Snow.png"
            },
            "Jon II": {
                "content": "Jon II: Jon and the Night's Watch stop at Craster's Keep, where Craster provides shelter in exchange for supplies.",
                "image": "Jon_Snow.png"
            },
            "Jon III": {
                "content": "Jon III: At Craster's, Jon realizes Craster sacrifices his sons to the Others.",
                "image": "Jon_Snow.png"
            },
            "Jon IV": {
                "content": "Jon IV: Mormont leads the Watch beyond the Wall in search of Benjen Stark and Mance Rayder.",
                "image": "Jon_Snow.png"
            },
            "Jon V": {
                "content": "Jon V: Jon scouts the Frostfangs and encounters Ghost acting strangely.",
                "image": "Jon_Snow.png"
            },
            "Jon VI": {
                "content": "Jon VI: Jon captures Ygritte but cannot bring himself to kill her, setting her free.",
                "image": "Jon_Snow.png"
            },
            "Jon VII": {
                "content": "Jon VII: Qhorin Halfhand and a group including Jon set off to kill Mance Rayder's scouts.",
                "image": "Jon_Snow.png"
            },
            "Jon VIII": {
                "content": "Jon VIII: Qhorin instructs Jon to infiltrate the wildlings by pretending to betray the Watch.",
                "image": "Jon_Snow.png"
            }
        }

    def display_Jon(self, jon_name):
        profiles = self.show_Jon_chapter()
        Jon_chapter = profiles[jon_name]
        chapter_text = f"{Jon_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Jon_chapter['image'])

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


## book III


class JonBookIII(ctk.CTkFrame):
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
            from_=1, to=12, number_of_steps=11,
            command=self.slider_changed,
            width=400,
            progress_color="white",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Jon {self.convert_to_roman(chapter_index)}"
        self.display_Jon(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
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

    def show_Jon_chapter(self):
        return {
            "Jon I": {"content": "Jon I: Jon struggles with loyalty after infiltrating the wildlings.", "image": "Jon_Snow.png"},
            "Jon II": {"content": "Jon II: Jon climbs the Wall with the wildlings.", "image": "Jon_Snow.png"},
            "Jon III": {"content": "Jon III: Jon and Ygritte grow closer as they travel south of the Wall.", "image": "Jon_Snow.png"},
            "Jon IV": {"content": "Jon IV: Jon witnesses the devastation caused by the wildlings.", "image": "Jon_Snow.png"},
            "Jon V": {"content": "Jon V: Jon and Ygritte continue their relationship.", "image": "Jon_Snow.png"},
            "Jon VI": {"content": "Jon VI: Jon struggles with the decision to betray the wildlings.", "image": "Jon_Snow.png"},
            "Jon VII": {"content": "Jon VII: Jon reveals his true loyalty and escapes the wildlings.", "image": "Jon_Snow.png"},
            "Jon VIII": {"content": "Jon VIII: Jon is pursued by wildlings and injured.", "image": "Jon_Snow.png"},
            "Jon IX": {"content": "Jon IX: Jon returns to Castle Black.", "image": "Jon_Snow.png"},
            "Jon X": {"content": "Jon X: Jon recovers from his wounds at the Wall.", "image": "Jon_Snow.png"},
            "Jon XI": {"content": "Jon XI: Jon helps prepare Castle Black for battle against Mance Rayder.", "image": "Jon_Snow.png"},
            "Jon XII": {"content": "Jon XII: Jon fights in the Battle for Castle Black.", "image": "Jon_Snow.png"},
        }

    def display_Jon(self, jon_name):
        profiles = self.show_Jon_chapter()
        Jon_chapter = profiles[jon_name]
        chapter_text = f"{Jon_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Jon_chapter['image'])

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
