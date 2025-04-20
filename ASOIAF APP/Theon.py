import customtkinter as ctk
from PIL import Image

class TheonBookII(ctk.CTkFrame):
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
        self.slider = ctk.CTkSlider(self,
            from_=1, to=6, number_of_steps=5,
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
        chapter_name = f"Theon {self.convert_to_roman(chapter_index)}"
        self.display_Theon(chapter_name)

    def convert_to_roman(self, num):
        roman_numerals = ["I", "II", "III", "IV", "V", "VI"]
        return roman_numerals[num - 1]

    def create_buttons(self):
        from POV_Characters import POVCharactersBookII
        button_back = ctk.CTkButton(
            self, text="Back", command=lambda: self.controller.show_frame(POVCharactersBookII),
            width=80, height=30,
            corner_radius=8, bg_color="transparent", fg_color="transparent",
            hover_color="grey", font=("Arial", 18)
        )
        button_back.place(x=20, y=30)

    def show_Theon_Chapter(self):
        return {
            "Theon I": {
                "content": "Theon I:Theon arrives at Pyke and learns that Lord Balon means to invade the north.",
                "image": "Theon_Greyjoy.png"
            },
            "Theon II": {
                "content": "Theon II:Theon meets Asha, who makes a fool out of him. Lord Balon reveals his battle plan for attacking the north.",
                "image": "Theon_Greyjoy.png"
            },
            "Theon III": {
                "content": "Theon III:Theon ambushes and annihilates a force led by Benfred Tallhart. He plans to capture Winterfell.",
                "image": "Theon_Greyjoy.png"
            },
            "Theon IV": {
                "content": "Theon IV:Bran and Rickon escape from Winterfell. Theon and his men ride out to find them.",
                "image": "Theon_Greyjoy.png"
            },
            "Theon V": {
                "content": "Theon V:Asha comes to Winterfell, but refuses to aid Theon in holding the castle.",
                "image": "Theon_Greyjoy.png"
            },
            "Theon VI": {
                "content": "Theon VI:Ramsay Snow kills Ser Rodrik, scatters his army, and takes Winterfell from Theon.",
                "image": "Theon_Greyjoy.png"
            }
        }

    def display_Theon(self, chapter_name):
        profile = self.show_Theon_Chapter()
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
