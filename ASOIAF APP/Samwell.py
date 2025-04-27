import customtkinter as ctk
from PIL import Image

class SamwellBookIII(ctk.CTkFrame):
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
            from_=1, to=5, number_of_steps=4,
            command=self.slider_changed,
            width=400,
            progress_color="light blue",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Samwell {self.convert_to_roman(chapter_index)}"
        self.display_Samwell(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V"]
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

    def show_Samwell_chapter(self):
        return {
            "Samwell I": {
                "content": "Samwell I: Sam flees from the Fist of the First Men after the attack by the Others.",
                "image": "Samwell_Tarly.png"
            },
            "Samwell II": {
                "content": "Samwell II: Struggling in the wilderness, Sam tries to help the remaining members of the Night's Watch reach safety.",
                "image": "Samwell_Tarly.png"
            },
            "Samwell III": {
                "content": "Samwell III: Sam fights and kills a wight using dragonglass while escaping with Gilly and her baby.",
                "image": "Samwell_Tarly.png"
            },
            "Samwell IV": {
                "content": "Samwell IV: Sam returns to Castle Black and brings news of the horror beyond the Wall.",
                "image": "Samwell_Tarly.png"
            },
            "Samwell V": {
                "content": "Samwell V: Sam helps Maester Aemon maneuver the election of Jon Snow as the new Lord Commander of the Night's Watch.",
                "image": "Samwell_Tarly.png"
            }
        }

    def display_Samwell(self, samwell_name):
        profiles = self.show_Samwell_chapter()
        Samwell_chapter = profiles[samwell_name]
        chapter_text = f"{Samwell_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Samwell_chapter['image'])

    def update_text_box(self, text):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", ctk.END)
        self.text_box.insert(ctk.END, text)
        self.text_box.configure(state="disabled")

    def update_image(self, image_name):
        try:
            image_path = f"C:/Users/emuki/OneDrive/Desktop/ASOIAF APP/ASOIAF-App-1/ASOIAF APP/Png Files/{image_name}"
            pil_image = Image.open(image_path).resize((300, 390))
            ctk_image = ctk.CTkImage(pil_image, size=(300, 390))
            self.image_label.configure(image=ctk_image)
            self.image_label.image = ctk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.update_text_box("\n[Image could not be loaded.]")
