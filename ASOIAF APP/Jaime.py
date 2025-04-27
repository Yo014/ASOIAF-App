import customtkinter as ctk
from PIL import Image

class JaimeBookIII(ctk.CTkFrame):
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
            from_=1, to=9, number_of_steps=8,
            command=self.slider_changed,
            width=400,
            progress_color="gold",
            button_color="white",
            button_hover_color="white",
            height=30
        )
        self.slider.set(1)
        self.slider.place(x=75, y=530)

    def slider_changed(self, value):
        chapter_index = int(value)
        chapter_name = f"Jaime {self.convert_to_roman(chapter_index)}"
        self.display_Jaime(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
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

    def show_Jaime_chapter(self):
        return {
            "Jaime I": {
                "content": "Jaime I: Jaime reflects on his captivity and confronts Catelyn Stark at Riverrun.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime II": {
                "content": "Jaime II: Jaime is freed by Catelyn Stark and Brienne of Tarth escorts him south.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime III": {
                "content": "Jaime III: Jaime fights Brienne, but they are captured by mercenaries.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime IV": {
                "content": "Jaime IV: Jaime's sword hand is cut off. He struggles to survive the loss.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime V": {
                "content": "Jaime V: Jaime and Brienne arrive at Harrenhal, and Roose Bolton treats Jaime’s wounds.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime VI": {
                "content": "Jaime VI: Jaime bathes with Brienne and opens up about the truth behind the 'Kingslayer' title.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime VII": {
                "content": "Jaime VII: Jaime is sent to King's Landing, but first rescues Brienne from a bear pit at Harrenhal.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime VIII": {
                "content": "Jaime VIII: Jaime returns to King's Landing and reunites with Cersei, finding their relationship changed.",
                "image": "Jaime_Lannister.png"
            },
            "Jaime IX": {
                "content": "Jaime IX: Jaime assumes his new role as Lord Commander of the Kingsguard, beginning a new path.",
                "image": "Jaime_Lannister.png"
            }
        }

    def display_Jaime(self, jaime_name):
        profiles = self.show_Jaime_chapter()
        Jaime_chapter = profiles[jaime_name]
        chapter_text = f"{Jaime_chapter['content']}"
        self.update_text_box(chapter_text)
        self.update_image(Jaime_chapter['image'])

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
