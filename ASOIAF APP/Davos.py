import customtkinter as ctk
from PIL import Image

class DavosBookII(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.place(x=130, y=10)  # Adjust placement  

        self.text_box = ctk.CTkTextbox(self, font=("Arial", 15), width=450, height=100, state="disabled")
        self.text_box.place(x=50, y=405)

        self.create_slider()
        self.create_buttons()

    def create_slider(self):
        self.slider = ctk.CTkSlider(self, 
            from_=1, to=3, number_of_steps=2,
            command=self.slider_changed, 
            width=400, 
            progress_color="dark blue",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Davos {self.convert_to_roman(chapter_index)}"
        self.display_Davos(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III"]
        return roman_numerals[num - 1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookII
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookII), width=80, height=30,
            corner_radius=8, bg_color="transparent", fg_color="transparent", hover_color="grey", font=("Arial", 18)
        )
        button_back.place(x=20, y=30)

    def show_Davos_Chapter(self):
        return {
            "Davos I": {
                "content": "Davos I:Stannis burns the statues of the Seven from Dragonstone’s sept and drafts a proclamation naming Joffrey a bastard.",
                "image": "Davos_Seaworth.png"
            },
            "Davos II": {
                "content": "Davos II:Stannis meets with Ser Cortnay Penrose, who refuses to yield Storm’s End. Davos takes Melisandre by boat under the walls of Storm’s End, where she births a creature of shadow.",
                "image": "Davos_Seaworth.png"
            },
            "Davos III": {
                "content": "Davos III:Stannis’s fleet engages Joffrey’s on the Blackwater Rush.",
                "image": "Davos_Seaworth.png"
            }
        }

    def display_Davos(self, chapter_name):
        profile = self.show_Davos_Chapter()
        chapter = profile[chapter_name]
        chapter_text = f"{chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(chapter['image'])

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


## book3

class DavosBookIII(ctk.CTkFrame):
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
            from_=1, to=6, number_of_steps=5,
            command=self.slider_changed,
            width=400,
            progress_color="navy",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Davos {self.convert_to_roman(chapter_index)}"
        self.display_Davos(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI"]
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

    def show_Davos_chapter(self):
        return {
            "Davos I": {"content": "Davos I: Davos survives the Battle of Blackwater and washes ashore.", "image": "Davos_Seaworth.png"},
            "Davos II": {"content": "Davos II: Davos plans to assassinate Melisandre but fails.", "image": "Davos_Seaworth.png"},
            "Davos III": {"content": "Davos III: Davos becomes Stannis’s Hand of the King.", "image": "Davos_Seaworth.png"},
            "Davos IV": {"content": "Davos IV: Davos advises Stannis as the northern strategy unfolds.", "image": "Davos_Seaworth.png"},
            "Davos V": {"content": "Davos V: Davos supports sending an envoy to the Night’s Watch.", "image": "Davos_Seaworth.png"},
            "Davos VI": {"content": "Davos VI: Davos prepares for his mission to White Harbor.", "image": "Davos_Seaworth.png"},
        }

    def display_Davos(self, davos_name):
        profiles = self.show_Davos_chapter()
        Davos_chapter = profiles[davos_name]
        chapter_text = f"{Davos_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Davos_chapter['image'])

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
